from dataclasses import dataclass

@dataclass
class ScriptArguments:
    script_source_file: str
    script_source_file_type: str
    script_name: str
    script: str
     
    