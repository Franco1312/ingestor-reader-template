"""Empty parser plugin skeleton for INDEC IPC dataset.

This is a placeholder for dataset-specific parsing logic.
Implement this when adding INDEC IPC parsing support.
"""

from typing import Any

from radar_data.domain.interfaces import ParserPort


class IndecIpcParser(ParserPort):
    """Dataset-specific parser for INDEC Consumer Price Index.

    TODO:
        - Implement INDEC-specific parsing logic.
        - Handle INDEC's Excel/CSV format and structure.
        - Extract date and value columns according to INDEC schema.
        - Handle any INDEC-specific edge cases.
    """

    def parse(
        self,
        file_path: str,
        dataset_config: dict[str, Any],
    ) -> list[dict[str, str | float]]:
        """Parse INDEC IPC file into raw records.

        Args:
            file_path: Path to the INDEC file.
            dataset_config: Dataset configuration.

        Returns:
            List of raw records.

        TODO:
            - Implement INDEC-specific parsing.
        """
        # TODO: Implement INDEC-specific parsing logic
        pass

    def supports(self, file_path: str) -> bool:
        """Check if this parser supports the given file type.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if file is INDEC IPC format, False otherwise.

        TODO:
            - Implement file type detection.
        """
        # TODO: Implement INDEC file detection
        pass

