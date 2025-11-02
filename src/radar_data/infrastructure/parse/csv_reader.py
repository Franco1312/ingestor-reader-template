"""CSV reader adapter implementing ParserPort."""

from typing import Any

from radar_data.domain.interfaces import ParserPort


class CsvReader(ParserPort):
    """Adapter for parsing CSV files.

    Implements the ParserPort interface for CSV format.
    Uses Python's built-in csv module for reading.

    TODO:
        - Implement actual CSV parsing.
        - Add support for different delimiters.
        - Add support for header rows.
        - Add support for column selection based on config.
        - Add support for skipping rows.
        - Add encoding detection.
    """

    def parse(
        self,
        file_path: str,
        dataset_config: dict[str, Any],
    ) -> list[dict[str, str | float]]:
        """Parse a CSV file into a list of raw records.

        Args:
            file_path: Path to the CSV file.
            dataset_config: Configuration dict specifying columns, start_row, etc.

        Returns:
            List of dictionaries, each representing a raw record.

        Raises:
            ValueError: If config is invalid or file cannot be parsed.
            FileNotFoundError: If file_path does not exist.

        TODO:
            - Read CSV file with appropriate encoding.
            - Skip rows based on start_row config.
            - Select columns based on config.
            - Parse dates and numbers appropriately.
        """
        # TODO: Implement CSV parsing
        # import csv
        # from pathlib import Path
        #
        # file = Path(file_path)
        # if not file.exists():
        #     raise FileNotFoundError(f"CSV file not found: {file_path}")
        #
        # source_config = dataset_config.get("source", {})
        # columns = source_config.get("columns", {})
        # start_row = source_config.get("start_row", 0)
        #
        # records = []
        # with open(file, "r", encoding="utf-8-sig") as f:
        #     reader = csv.DictReader(f)
        #     for i, row in enumerate(reader):
        #         if i < start_row:
        #             continue
        #         record = {
        #             "date": row.get(columns.get("date", "date")),
        #             "value": row.get(columns.get("value", "value")),
        #         }
        #         records.append(record)
        #
        # return records
        pass

    def supports(self, file_path: str) -> bool:
        """Check if this parser supports the given file type.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if file is CSV, False otherwise.
        """
        return file_path.lower().endswith(".csv")

