import requests
import pandas as pd
from abc import ABC, abstractmethod
from typing import List, Tuple


class LLM_Detector(ABC):
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
        return """You are an ASL gloss generator for airport announcements. Follow STRICTLY:
1. Output ONLY the gloss text exactly as shown in examples
2. Maintain the SHORTENED grammar style from samples
3. Use LOWERCASE except for [Number]/[Location]/[DateTime]/[Person]
4. Number of specific tokens [Number]/[Location]/[DateTime]/[Person] should be the same as in the input
5. Keep the SPECIFIC phrase patterns from examples
6. NEVER add explanations or punctuation

Example transformations:"""

    def _load_dataset(self, path: str) -> List[Tuple[str, str]]:
        data = pd.read_csv(path)
        return list(zip(data['text'], data['gloss']))

    def _get_few_shot_examples(self, n: int) -> str:
        if not self.dataset or len(self.dataset) < n:
            return ""
        examples = []
        for text, gloss in self.dataset[:n]:
            examples.append(f"\nEnglish: {text}\nASL Gloss: {gloss}")
        return "\n".join(examples)

    def _add_to_history(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})

    def translate(self, english_text: str) -> str:
        self._add_to_history("user", f"Translate to ASL gloss: {english_text}")
        
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


