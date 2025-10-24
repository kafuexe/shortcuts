from abc import ABC, abstractmethod

from common.script_arguments import ScriptArguments

class CompilerTypeBase(ABC):
    @abstractmethod
    def compile(self, arguments: list[ScriptArguments]) -> bytes:
        pass