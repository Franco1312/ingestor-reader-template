"""CSV writer adapter implementing SinkPort."""

from csv import DictWriter
from pathlib import Path
from typing import Optional

from radar_data.domain.entities import Observation
from radar_data.domain.interfaces import SinkPort


class CsvSink(SinkPort):
    """Adapter for writing observations to CSV format.

    Implements the SinkPort interface for CSV output.
    Uses Python's built-in csv module for writing.

    TODO:
        - Implement actual CSV writing.
        - Add proper date formatting.
        - Add header row.
        - Add quoting/escaping for special characters.
        - Add support for different delimiters.
    """

    def __init__(self, delimiter: str = ",", include_header: bool = True) -> None:
        """Initialize the CSV sink.

        Args:
            delimiter: CSV delimiter character.
            include_header: Whether to include a header row.
        """
        self.delimiter = delimiter
        self.include_header = include_header

    def write_csv(
        self,
        observations: list[Observation],
        output_path: str,
    ) -> str:
        """Write observations to a CSV file.

        Args:
            observations: List of observations to write.
            output_path: Path where the CSV file should be written.

        Returns:
            Path to the written file.

        Raises:
            PermissionError: If output_path cannot be written to.
            ValueError: If observations list is empty.

        TODO:
            - Convert observations to CSV rows.
            - Write with proper formatting (dates, numbers).
            - Include header row if include_header is True.
        """
        # TODO: Implement CSV writing
        # from datetime import datetime
        #
        # if not observations:
        #     raise ValueError("Cannot write empty observations list")
        #
        # output_file = Path(output_path)
        # output_file.parent.mkdir(parents=True, exist_ok=True)
        #
        # fieldnames = ["series_code", "timestamp", "value"]
        # with open(output_file, "w", newline="") as f:
        #     writer = DictWriter(f, fieldnames=fieldnames, delimiter=self.delimiter)
        #     if self.include_header:
        #         writer.writeheader()
        #     for obs in observations:
        #         writer.writerow({
        #             "series_code": obs.series_code,
        #             "timestamp": obs.timestamp.isoformat(),
        #             "value": obs.value,
        #         })
        # return str(output_file)
        pass

    def write_parquet(
        self,
        observations: list[Observation],
        output_path: str,
        partition_by: Optional[str] = None,
    ) -> str:
        """Write observations to a Parquet file (not implemented for CSV sink).

        This method is part of SinkPort interface but not implemented
        for CsvSink. Use ParquetSink instead.

        Raises:
            NotImplementedError: Always, as this sink only supports CSV.
        """
        raise NotImplementedError("CsvSink does not support Parquet output")

