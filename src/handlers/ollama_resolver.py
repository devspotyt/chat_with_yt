from src.models.resolver import AIChatResolverBase
from litellm import completion
from typing import List, Dict


class OllamaResolver(AIChatResolverBase):
    RESOLVER_PREFIX = "ollama"

    def query(self, messages: List[Dict[str, str]]) -> List[str]:
        response = completion(
            model=self.model,
            messages=messages,
            api_base=self.base_api
        )
        return [x.message.content for x in response.choices]
