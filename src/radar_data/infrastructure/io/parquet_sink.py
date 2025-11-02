"""Parquet writer adapter implementing SinkPort."""

from typing import Optional

from radar_data.domain.entities import Observation
from radar_data.domain.interfaces import SinkPort


class ParquetSink(SinkPort):
    """Adapter for writing observations to Parquet format.

    Implements the SinkPort interface for Parquet output using PyArrow.
    Supports partitioning by series_code or other columns.

    TODO:
        - Implement actual Parquet writing using PyArrow.
        - Add schema definition for observations.
        - Add partitioning support.
        - Add compression options.
        - Add metadata writing (schema, provenance).
    """

    def __init__(self, compression: str = "snappy") -> None:
        """Initialize the Parquet sink.

        Args:
            compression: Compression algorithm (e.g., "snappy", "gzip").
        """
        self.compression = compression

    def write_parquet(
        self,
        observations: list[Observation],
        output_path: str,
        partition_by: Optional[str] = None,
    ) -> str:
        """Write observations to a Parquet file.

        Args:
            observations: List of observations to write.
            output_path: Path where the Parquet file should be written.
            partition_by: Optional partition column (e.g., "series_code").

        Returns:
            Path to the written file.

        Raises:
            PermissionError: If output_path cannot be written to.
            ValueError: If observations list is empty.

        TODO:
            - Convert observations to PyArrow table.
            - Define schema (series_code: string, timestamp: timestamp, value: float).
            - Write to Parquet with specified compression.
            - Handle partitioning if partition_by is specified.
        """
        # TODO: Implement Parquet writing
        # import pyarrow as pa
        # import pyarrow.parquet as pq
        #
        # if not observations:
        #     raise ValueError("Cannot write empty observations list")
        #
        # # Convert observations to records
        # records = [
        #     {
        #         "series_code": obs.series_code,
        #         "timestamp": obs.timestamp,
        #         "value": obs.value,
        #     }
        #     for obs in observations
        # ]
        #
        # # Create PyArrow table with schema
        # schema = pa.schema([
        #     ("series_code", pa.string()),
        #     ("timestamp", pa.timestamp("us")),
        #     ("value", pa.float64()),
        # ])
        # table = pa.Table.from_pylist(records, schema=schema)
        #
        # # Write to Parquet
        # pq.write_table(table, output_path, compression=self.compression)
        # return output_path
        pass

    def write_csv(
        self,
        observations: list[Observation],
        output_path: str,
    ) -> str:
        """Write observations to a CSV file (not implemented for Parquet sink).

        This method is part of SinkPort interface but not implemented
        for ParquetSink. Use CsvSink instead.

        Raises:
            NotImplementedError: Always, as this sink only supports Parquet.
        """
        raise NotImplementedError("ParquetSink does not support CSV output")

