"""Use case for writing normalized data to output formats."""

from radar_data.domain.entities import Observation
from radar_data.domain.interfaces import SinkPort


class WriteUseCase:
    """Orchestrates data writing operations.

    This use case coordinates the writing of normalized data to output
    formats using the SinkPort interface. It handles format selection,
    partitioning, and file management.

    TODO:
        - Implement write logic using SinkPort.
        - Add format selection (Parquet vs CSV).
        - Add partitioning support.
        - Add output validation.
    """

    def __init__(self, sink: SinkPort) -> None:
        """Initialize the write use case.

        Args:
            sink: Implementation of SinkPort to use for writing.
        """
        self.sink = sink

    def execute(
        self,
        observations: list[Observation],
        output_path: str,
        format: str = "parquet",
        partition_by: str | None = None,
    ) -> str:
        """Execute the write operation.

        Args:
            observations: List of observations to write.
            output_path: Path where the file should be written.
            format: Output format ("parquet" or "csv").
            partition_by: Optional partition column (e.g., "series_code").

        Returns:
            Path to the written file.

        Raises:
            ValueError: If format is not supported.
            PermissionError: If output_path cannot be written to.
        """
        # TODO: Implement write logic
        # if format == "parquet":
        #     return self.sink.write_parquet(observations, output_path, partition_by)
        # elif format == "csv":
        #     if partition_by:
        #         raise ValueError("CSV format does not support partitioning")
        #     return self.sink.write_csv(observations, output_path)
        # else:
        #     raise ValueError(f"Unsupported format: {format}")
        pass

