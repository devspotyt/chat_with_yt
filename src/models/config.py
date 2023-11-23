from json import load
from typing import Dict
from pydantic import BaseModel, field_validator
from src.models.resolver import AIChatResolverBase
from src.handlers.ollama_resolver import OllamaResolver
from src.handlers.hf_resolver import HuggingFaceResolver


class ResolverConfig(BaseModel):
    model: str
    base_api: str
    resolver_type: str

    class Config:
        arbitrary_types_allowed = True

    @field_validator('resolver_type')
    def validate_resolver_type(cls, v):
        if v not in ['huggingface', 'ollama']:
            raise ValueError("Unsupported resolver type")
        return v

    # Method to instantiate the appropriate resolver
    def to_resolver(self):
        if self.resolver_type == 'huggingface':
            return HuggingFaceResolver(self.model, self.base_api)
        elif self.resolver_type == 'ollama':
            return OllamaResolver(self.model, self.base_api)
        else:
            raise ValueError(
                f"Unsupported resolver type: {self.resolver_type}")


# Configuration model
class Config(BaseModel):
    resolvers: Dict[str, Dict]

    def to_resolvers_config(self):
        return {k: ResolverConfig(**v) for k, v in self.resolvers.items()}


def load_resolvers(file_path: str) -> Dict[str, AIChatResolverBase]:
    with open(file_path, 'r') as fp:
        data = load(fp)
    config = Config(resolvers=data).to_resolvers_config()

    resolver_instances: Dict[str, HuggingFaceResolver | OllamaResolver] = {
        name: resolver_config.to_resolver() for name, resolver_config in
        config.items()
    }
    return resolver_instances
