from bl.arguments_extractor.abstract.argument_extractor_base import ArgumentExtractorBase
from bl.arguments_extractor.ahk_argument_extractor import AHKArgumentExtractor


registry: dict[str, ArgumentExtractorBase] = {
"ahk": AHKArgumentExtractor
}


