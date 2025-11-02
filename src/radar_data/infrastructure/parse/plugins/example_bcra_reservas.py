"""Empty parser plugin skeleton for BCRA Reservas dataset.

This is a placeholder for dataset-specific parsing logic.
Implement this when adding BCRA Reservas parsing support.
"""

from typing import Any

from radar_data.domain.interfaces import ParserPort


class BcraReservasParser(ParserPort):
    """Dataset-specific parser for BCRA International Reserves.

    TODO:
        - Implement BCRA-specific parsing logic.
        - Handle BCRA's Excel format and structure.
        - Extract date and value columns according to BCRA schema.
        - Handle any BCRA-specific edge cases.
    """

    def parse(
        self,
        file_path: str,
        dataset_config: dict[str, Any],
    ) -> list[dict[str, str | float]]:
        """Parse BCRA Reservas file into raw records.

        Args:
            file_path: Path to the BCRA file.
            dataset_config: Dataset configuration.

        Returns:
            List of raw records.

        TODO:
            - Implement BCRA-specific parsing.
        """
        # TODO: Implement BCRA-specific parsing logic
        pass

    def supports(self, file_path: str) -> bool:
        """Check if this parser supports the given file type.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if file is BCRA Reservas format, False otherwise.

        TODO:
            - Implement file type detection.
        """
        # TODO: Implement BCRA file detection
        pass

