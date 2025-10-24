import os
from pathlib import Path

from bl.compiler_types.Flow_Launcher_compiler_type import FlowLauncherCompilerType
from common.file_type_to_script_argument_extractor import registry as FileTypeToScriptArgumentExtractor
from common.script_arguments import ScriptArguments


## ------- Configuration -------
scripts_folder = f"{os.getcwd()}/scripts"
compiler = FlowLauncherCompilerType()
output_path = Path(f"{os.getcwd()}/.output/Favorites.conf")
## -----------------------------
 
def main():
    all_arguments: list[ScriptArguments] = []
    
    for script in os.listdir(scripts_folder):
        file_path = Path(scripts_folder) /Path(script)
        if not file_path.is_file():
            continue
        file_type = script.split(".")[-1].lower()
        
        if file_type not in FileTypeToScriptArgumentExtractor.keys():
            print(f"⚠️ Unsupported file type: {file_type} ({script})")
            continue

        extractor = FileTypeToScriptArgumentExtractor[file_type]()
        extracted = extractor.extract(str(file_path))
        all_arguments.extend(extracted)
    
    if all_arguments:
        result = compiler.compile(all_arguments)
        output_path.exists() or output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"\n✅ Compiled {len(all_arguments)} script functions into: {output_path}")
    else:
        print("No valid script functions found.")

if __name__ == "__main__":
    main()