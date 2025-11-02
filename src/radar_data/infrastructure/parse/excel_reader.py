"""Excel reader adapter implementing ParserPort.

Supports .xlsx, .xlsm, .xls, and potentially .xlsb formats.
Uses openpyxl for .xlsx/.xlsm and pyxlsb for .xlsb.
"""

from typing import Any

from radar_data.domain.interfaces import ParserPort


class ExcelReader(ParserPort):
    """Adapter for parsing Excel files.

    Implements the ParserPort interface for Excel formats (.xlsx, .xlsm, .xls, .xlsb).
    Uses openpyxl for modern Excel formats and pyxlsb for binary formats.

    TODO:
        - Implement actual Excel parsing using openpyxl/pyxlsb.
        - Add support for multiple sheets.
        - Add support for start_cell configuration.
        - Add support for column selection.
        - Add support for date/number parsing.
        - Handle merged cells.
        - Add support for .xls (legacy) format using xlrd.
    """

    def parse(
        self,
        file_path: str,
        dataset_config: dict[str, Any],
    ) -> list[dict[str, str | float]]:
        """Parse an Excel file into a list of raw records.

        Args:
            file_path: Path to the Excel file.
            dataset_config: Configuration dict specifying sheet, start_cell, columns, etc.

        Returns:
            List of dictionaries, each representing a raw record.

        Raises:
            ValueError: If config is invalid or file cannot be parsed.
            FileNotFoundError: If file_path does not exist.
            ImportError: If required libraries (openpyxl, pyxlsb) are not installed.

        TODO:
            - Load Excel file with openpyxl or pyxlsb.
            - Select sheet based on config.
            - Parse from start_cell if specified.
            - Extract columns based on config.
            - Convert to list of dictionaries.
        """
        # TODO: Implement Excel parsing
        # from pathlib import Path
        # try:
        #     import openpyxl
        # except ImportError:
        #     raise ImportError("openpyxl is required for Excel parsing")
        #
        # file = Path(file_path)
        # if not file.exists():
        #     raise FileNotFoundError(f"Excel file not found: {file_path}")
        #
        # source_config = dataset_config.get("source", {})
        # sheet_name = source_config.get("sheet", None)
        # start_cell = source_config.get("start_cell", "A1")
        # columns = source_config.get("columns", {})
        #
        # wb = openpyxl.load_workbook(file, data_only=True)
        # if sheet_name:
        #     ws = wb[sheet_name]
        # else:
        #     ws = wb.active
        #
        # # Parse from start_cell
        # # Extract records based on columns
        # # Return list of dictionaries
        # records = []
        # # ... implementation ...
        #
        # return records
        pass

    def supports(self, file_path: str) -> bool:
        """Check if this parser supports the given file type.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if file is Excel format, False otherwise.
        """
        return file_path.lower().endswith((".xlsx", ".xlsm", ".xls", ".xlsb"))

