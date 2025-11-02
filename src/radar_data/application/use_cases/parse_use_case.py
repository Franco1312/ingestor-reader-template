"""Use case for parsing raw files into structured data."""

from radar_data.domain.interfaces import ParserPort


class ParseUseCase:
    """Orchestrates file parsing operations.

    This use case coordinates the parsing of files into structured data
    using the ParserPort interface. It handles format detection, parser
    selection, and result formatting.

    TODO:
        - Implement parse logic using ParserPort.
        - Add parser registry/discovery for plugin parsers.
        - Add format detection (CSV, Excel, ZIP).
        - Add validation of parsed records against schema.
    """

    def __init__(self, parser: ParserPort) -> None:
        """Initialize the parse use case.

        Args:
            parser: Implementation of ParserPort to use for parsing.
        """
        self.parser = parser

    def execute(self, file_path: str, dataset_config: dict) -> list[dict[str, str | float]]:
        """Execute the file parsing operation.

        Args:
            file_path: Path to the file to parse.
            dataset_config: Configuration dict specifying sheet, columns,
                start_cell, etc.

        Returns:
            List of dictionaries, each representing a raw record from the file.

        Raises:
            ValueError: If file format is not supported or config is invalid.
            FileNotFoundError: If file_path does not exist.
        """
        # TODO: Implement parse logic
        # if not self.parser.supports(file_path):
        #     raise ValueError(f"Parser does not support file: {file_path}")
        # return self.parser.parse(file_path, dataset_config)
        pass

