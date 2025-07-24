import requests
import pandas as pd
from abc import ABC, abstractmethod
from typing import List, Tuple


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

    def _build_base_prompt(self) -> str:
        # Base prompt

        return """  
            Ti si agent koji služi da modifikuje rečenicu na srpskom jeziku koja sadrži govor mržnje tako da ta rečenica ima isto značenje ali da nema govor mržnje.
            Govor mržnje uključuje uvrede, diskriminaciju ili agresivni govor na osnovu rase, vere, pola, nacionalnosti, seksualne orijentacije, invaliditeta itd.
            Odgovor treba da bude samo izmenjena rečenica, bez dodatnih komentara ili objašnjenja.
            Vodi računa da ne izmeniš značenje rečenice.
             - Ako slučajno ne možeš da izmeniš rečenicu, onda neka tvoj odgovor bude da "To nije moguće". 
             - Ako u rečenici nema govora mržnje onda samo konstatuj "U ovoj rečenici nema govora mržnje"
           
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
        self._add_to_history("user", f"Modifikuj ovu rečenicu: {hate_speech_text}")
        
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
        return content


