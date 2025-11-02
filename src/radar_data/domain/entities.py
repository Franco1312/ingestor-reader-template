"""Domain entities: Series, Observation, Provenance.

These are the core domain objects representing data series,
individual observations, and data provenance metadata.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Series:
    """Represents a time series dataset.

    Attributes:
        code: Internal series identifier (e.g., "BCRA_RESERVES").
        name: Human-readable name of the series.
        unit: Unit of measurement (e.g., "USD", "index_base_100").
        frequency: Data frequency ("daily", "monthly", "quarterly", "annual").
        provider: Data provider identifier (e.g., "BCRA", "INDEC").

    TODO:
        - Add domain invariants (e.g., frequency must be valid enum).
        - Add validation logic for code format.
        - Consider making this a value object vs entity.
    """

    code: str
    name: str
    unit: str
    frequency: str
    provider: str

    def __post_init__(self) -> None:
        """TODO: Add domain validation logic."""
        pass


@dataclass(frozen=True)
class Observation:
    """Represents a single data point in a time series.

    Attributes:
        series_code: Identifier of the series this observation belongs to.
        timestamp: Date/time of the observation.
        value: Numeric value of the observation.
        provenance: Optional provenance metadata about the data source.

    TODO:
        - Add domain invariants (e.g., timestamp must be valid, value must be numeric).
        - Add validation logic for value types.
        - Consider timezone handling for timestamps.
    """

    series_code: str
    timestamp: datetime
    value: float
    provenance: Optional["Provenance"] = None

    def __post_init__(self) -> None:
        """TODO: Add domain validation logic."""
        pass


@dataclass(frozen=True)
class Provenance:
    """Metadata about the source and lineage of data.

    Attributes:
        source_url: Original URL or path where data was fetched.
        fetched_at: Timestamp when data was fetched.
        dataset_id: Identifier of the dataset configuration used.
        file_hash: Optional hash of the source file for integrity checking.

    TODO:
        - Add domain invariants.
        - Consider adding transformation history/lineage tracking.
        - Add validation for URL format.
    """

    source_url: str
    fetched_at: datetime
    dataset_id: str
    file_hash: Optional[str] = None

    def __post_init__(self) -> None:
        """TODO: Add domain validation logic."""
        pass

