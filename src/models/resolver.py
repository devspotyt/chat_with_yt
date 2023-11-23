from abc import ABC, abstractmethod
from typing import List, Dict


class AIChatResolverBase(ABC):
    def __init__(self, model: str, base_api: str):
        """ Initialize the resolver with a specific model. """
        self.model = model
        self.base_api = base_api

    @abstractmethod
    def query(self, messages: List[Dict[str, str]]) -> List[str]:
        """ Abstract method to query the AI model. """
        pass

