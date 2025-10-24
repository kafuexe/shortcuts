from collections import defaultdict
from pathlib import Path
from bl.compiler_types.abstract.compiler_type_base import CompilerTypeBase
from common.script_arguments import ScriptArguments


class FlowLauncherCompilerType(CompilerTypeBase):
    def compile(self, arguments: list[ScriptArguments]) -> str:
        if not arguments:
            return ""

        grouped: dict[str, list[ScriptArguments]] = defaultdict(list)
        for arg in arguments:
            grouped[arg.script_source_file].append(arg)

        sections = []
        for file_path, funcs in grouped.items():
            filename = Path(file_path).stem
            sections.append(f"[{filename}]")

            for func in sorted(funcs, key=lambda x: x.script_name.lower()):
                sections.append(f"{func.script_name}= {func.script}")

            sections.append("")  

        return "\n".join(sections).strip() + "\n"