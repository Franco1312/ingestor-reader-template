"""Domain interfaces (ports) for external adapters.

These Protocols define the contracts that infrastructure adapters
must implement. They follow Clean Architecture principles where
the domain layer defines interfaces, and infrastructure implements them.
"""

from typing import Optional, Protocol, runtime_checkable

from radar_data.domain.entities import Observation, Series


@runtime_checkable
class FetcherPort(Protocol):
    """Port for fetching files from remote sources.

    Implementations should handle HTTP GET, ETag/Last-Modified headers,
    file downloads, and potentially S3/local filesystem access.
    """

    def fetch(self, source_url: str, destination_path: str) -> str:
        """Fetch a file from source_url and save to destination_path.

        Args:
            source_url: URL or path of the source file.
            destination_path: Local path where the file should be saved.

        Returns:
            Path to the downloaded file (may differ from destination_path
            if caching or deduplication is used).

        Raises:
            FileNotFoundError: If source_url cannot be accessed.
            PermissionError: If destination_path cannot be written to.
        """
        ...

    def fetch_with_metadata(
        self,
        source_url: str,
        destination_path: str,
    ) -> tuple[str, dict[str, str]]:
        """Fetch a file and return metadata (ETag, Last-Modified, etc.).

        Args:
            source_url: URL or path of the source file.
            destination_path: Local path where the file should be saved.

        Returns:
            Tuple of (file_path, metadata_dict) where metadata contains
            HTTP headers like ETag, Last-Modified, Content-Type, etc.
        """
        ...


@runtime_checkable
class ParserPort(Protocol):
    """Port for parsing raw files into structured data.

    Implementations should handle CSV, Excel, ZIP, and other formats,
    extracting rows/columns based on configuration.
    """

    def parse(
        self,
        file_path: str,
        dataset_config: dict,
    ) -> list[dict[str, str | float]]:
        """Parse a file into a list of raw records.

        Args:
            file_path: Path to the file to parse.
            dataset_config: Configuration dict specifying sheet, columns,
                start_cell, etc.

        Returns:
            List of dictionaries, each representing a raw record from the file.
            Keys should match column names/indices from config.

        Raises:
            ValueError: If file format is not supported or config is invalid.
            FileNotFoundError: If file_path does not exist.
        """
        ...

    def supports(self, file_path: str) -> bool:
        """Check if this parser supports the given file type.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if this parser can handle the file, False otherwise.
        """
        ...


@runtime_checkable
class NormalizerPort(Protocol):
    """Port for normalizing raw parsed data into domain entities.

    Implementations should map external column names to internal schema,
    handle unit conversions, date parsing, and create Series/Observation
    entities.
    """

    def normalize(
        self,
        raw_records: list[dict[str, str | float]],
        dataset_config: dict,
    ) -> tuple[Series, list[Observation]]:
        """Normalize raw records into domain entities.

        Args:
            raw_records: List of raw dictionaries from parser.
            dataset_config: Configuration dict with normalize section
                (internal_series_code, unit, frequency).

        Returns:
            Tuple of (Series, list[Observations]) representing the normalized data.

        Raises:
            ValueError: If normalization fails (e.g., missing required fields).
        """
        ...


@runtime_checkable
class CleanerPort(Protocol):
    """Port for data quality checks and cleaning.

    Implementations should perform continuity checks, outlier detection,
    range validation, and other quality rules.
    """

    def clean(
        self,
        observations: list[Observation],
        quality_profile: dict,
    ) -> tuple[list[Observation], dict[str, int]]:
        """Apply quality checks and cleaning rules to observations.

        Args:
            observations: List of observations to clean.
            quality_profile: Configuration dict specifying which checks
                to run (continuity, outliers, range, etc.).

        Returns:
            Tuple of (cleaned_observations, report_dict) where report_dict
            contains counts of issues found (e.g., {"outliers": 5, "gaps": 2}).
        """
        ...

    def check_continuity(
        self,
        observations: list[Observation],
        config: dict,
    ) -> list[tuple[Observation, Observation]]:
        """Identify gaps in time series continuity.

        Args:
            observations: List of observations (should be sorted by timestamp).
            config: Configuration for continuity checks (max_gap_days, etc.).

        Returns:
            List of tuples representing gap boundaries (start, end observations).
        """
        ...

    def detect_outliers(
        self,
        observations: list[Observation],
        config: dict,
    ) -> list[Observation]:
        """Detect outlier observations based on statistical methods.

        Args:
            observations: List of observations to analyze.
            config: Configuration for outlier detection (method, threshold).

        Returns:
            List of observations identified as outliers.
        """
        ...


@runtime_checkable
class SinkPort(Protocol):
    """Port for writing normalized data to output formats.

    Implementations should handle Parquet, CSV, and potentially other formats.
    """

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
        """
        ...

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
        """
        ...

