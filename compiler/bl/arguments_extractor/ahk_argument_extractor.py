from pathlib import Path
import re
from bl.arguments_extractor.abstract.argument_extractor_base import ArgumentExtractorBase
from common.script_arguments import ScriptArguments


class AHKArgumentExtractor(ArgumentExtractorBase):
    def extract(self,file_path: str) -> list[ScriptArguments]:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"AHK file not found: {file_path}")
        
        content = file_path.read_text(encoding="utf-8")

        # Find the Functions := { ... } block
        match = re.search(r"Functions\s*:=\s*\{([\s\S]*)\}", content)
        if not match:
            raise ValueError("No 'Functions := { ... }' block found in file.")

        block_content = match.group(1)

        # Extract function names (keys before ':')
        # Example: PlayPause: () => Send("{Media_Play_Pause}")
        function_names = re.findall(r"(\w+):", block_content)
        script_args = [
            ScriptArguments(
                script_source_file=str(file_path),
                script_source_file_type="ahk",
                script_name=name,
                script=f"{file_path} {name}"
            )
            for name in function_names
        ]

        return script_args
            
    