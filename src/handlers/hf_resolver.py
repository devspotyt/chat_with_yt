from src.models.resolver import AIChatResolverBase
from litellm import completion
from typing import List, Dict


class HuggingFaceResolver(AIChatResolverBase):
    RESOLVER_PREFIX = "huggingface"

    def query(self, messages: List[Dict[str, str]]) -> List[str]:
        response = completion(
            model=f"{self.RESOLVER_PREFIX}/{self.model}",
            messages=messages,
            api_base=f"{self.base_api}/{self.model}",
            max_new_tokens=512
        )
        return [x.message.content for x in response.choices]
