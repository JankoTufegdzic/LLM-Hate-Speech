import os
import requests
import pandas as pd
import torch
from abc import ABC, abstractmethod
from typing import List, Tuple
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer
from huggingface_hub import login
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

class LLM_Pufirier():
    def __init__(self, model_name: str, dataset_path: str = None, few_shot_examples: int = 3):
        self.model_name = model_name
        self.conversation_history = []
        self.system_prompt = self._build_base_prompt()

        if dataset_path:
            self.dataset = self._load_dataset(dataset_path)
            self.system_prompt += self._get_few_shot_examples(few_shot_examples)
        else:
            self.dataset = None

        self._add_to_history("system", self.system_prompt)

        login(token=os.getenv("HF_TOKEN"))
        device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2', device=device)

    def _build_base_prompt(self) -> str:
        # Base prompt

        return """  
            Zadatak:
Tvoj zadatak je da analiziraš unetu rečenicu i ispraviš je tako da ukloniš svaki govor mržnje, uvrede, predrasude ili diskriminatorni sadržaj, ali da zadržiš osnovnu poruku rečenice ako je moguće. Cilj je da rečenica ostane informativna, ali da bude kulturna, neutralna i nepristrasna.

Definicija govora mržnje:
Govor mržnje je svaka komunikacija koja napada, ponižava, diskriminiše ili preti pojedincima ili grupama ljudi na osnovu:
- rase ili etničke pripadnosti
- nacionalnosti
- vere ili uverenja
- pola ili rodnog identiteta
- seksualne orijentacije
- invaliditeta
- društvenog ili ekonomskog statusa

Takođe, govor mržnje može sadržati:
- generalizacije ili stereotipe o određenim grupama
- agresivne izjave koje podstiču mržnju ili nasilje
- uvredljive izraze, psovke i omalovažavanje

Uputstvo:
- Preformuliši rečenicu tako da bude prikladna za javnu upotrebu, uvažavajući različitosti i ljudska prava.
- Ne menjaš osnovnu temu ako nije nužno — samo uklanjaš uvredljive i neprimerene elemente.
- Ako rečenica u potpunosti sadrži govor mržnje bez informativne vrednosti, možeš umesto nje napisati neutralnu poruku (npr. poziv na toleranciju).
- Ton treba da bude neutralan, nenasilan, nenapadački, ali ne mora biti previše formalan.
- Ukoliko preformulišeš rečenicu dodaj na početku izlaza reč "Preformulisana". Ukoliko pišeš neutralnu poruku dodaj na početku izlaza frazu "Neutralna poruka"
Primeri:

Ulaz: „Ti cigani stalno kradu.“
Izlaz: „Neutralna poruka. Neprihvatljivo je da generalizujemo čitav narod zbog postupaka pojedinaca.“

Ulaz: „Mrzim gejeve, to nije prirodno.“
Izlaz: „Preformulisana. Smatram da su različiti načini života legitimni, i važno je poštovati tuđe izbore.“

Ulaz: „Žene nisu za programiranje.“
Izlaz: „Preformulisana. Verujem da sposobnosti u programiranju ne zavise od pola.“

Ulaz: „Svi Albanci su opasni.“
Izlaz: „Neutralna poruka. Nije ispravno donositi sud o ljudima na osnovu njihove nacionalnosti.“

           
        """

    def _load_dataset(self, path: str) -> List[Tuple[str, str]]:
        return None
        # data = pd.read_csv(path)
        # return list(zip(data['text'], data['gloss']))

    def _get_few_shot_examples(self, n: int) -> str:
        if not self.dataset or len(self.dataset) < n:
            return ""
        examples = []
        for text, gloss in self.dataset[:n]:
            examples.append(f"\nEnglish: {text}\nASL Gloss: {gloss}")
        return "\n".join(examples)

    def _add_to_history(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})

    def purify(self, hate_speech_text: str) -> str:

        # Agent prompt
        self._add_to_history("user", f"Ulaz: {hate_speech_text}")
        
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": self.model_name,
                "messages": self.conversation_history,
                "stream": False
            }
        )
        
        result = response.json()
        content = result.get("message", {}).get("content", "").strip()
        self._add_to_history("assistant", content)

        cleaned_content = content.replace("Izlaz: ", "")

        cosine_sim = self._compute_cosine_similarity(cleaned_content, hate_speech_text)
        
        return cleaned_content, cosine_sim

    def _compute_cosine_similarity(self, pred, truth):
        return cosine_similarity(self.model.encode([pred]), self.model.encode([truth]))[0][0]
