from typing import List, Tuple
import requests
from .helper import highlight_prompt_map

class LLM_Highlighter():
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

        # login(token=os.getenv("HF_TOKEN"))
        # device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
        # self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2', device=device)

    def _build_base_prompt(self) -> str:
        return highlight_prompt_map[self.model_name]

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

    def highlight(self, hate_speech_text: str) -> str:
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

        cleaned_content=content.replace("Izlaz:","")
        cleaned_content=cleaned_content.replace("Ulaz:","")

        return cleaned_content