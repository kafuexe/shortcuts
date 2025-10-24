from abc import ABC, abstractmethod

from common.script_arguments import ScriptArguments


class ArgumentExtractorBase(ABC):
    @abstractmethod
    def extract(file_path: str) -> list[ScriptArguments]:
        pass