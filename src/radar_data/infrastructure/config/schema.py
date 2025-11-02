"""Pydantic models for configuration validation.

These models define the schema for datasets.yml and quality.yml files,
ensuring type safety and validation of configuration data.
"""

from typing import Optional

from pydantic import BaseModel, Field


class SourceConfig(BaseModel):
    """Configuration for data source.

    Attributes:
        type: Source type (e.g., "static_url").
        url: URL or path to the source file.
        sheet: Optional sheet name for Excel files.
        start_cell: Optional starting cell (e.g., "A2").
        columns: Column mapping for date and value fields.
    """

    type: str = Field(..., description="Source type (e.g., 'static_url')")
    url: str = Field(..., description="URL or path to source file")
    sheet: Optional[str] = Field(None, description="Sheet name for Excel files")
    start_cell: Optional[str] = Field(None, description="Starting cell (e.g., 'A2')")
    columns: dict[str, str] = Field(..., description="Column mapping for date and value")


class NormalizeConfig(BaseModel):
    """Configuration for data normalization.

    Attributes:
        internal_series_code: Internal identifier for the series.
        unit: Unit of measurement (e.g., "USD", "index_base_100").
        frequency: Data frequency ("daily", "monthly", etc.).
    """

    internal_series_code: str = Field(..., description="Internal series identifier")
    unit: str = Field(..., description="Unit of measurement")
    frequency: str = Field(..., description="Data frequency")


class DatasetConfig(BaseModel):
    """Configuration for a dataset.

    Attributes:
        id: Unique identifier for the dataset.
        provider: Data provider identifier (e.g., "BCRA", "INDEC").
        name: Human-readable name of the dataset.
        source: Source configuration.
        normalize: Normalization configuration.
        quality_profile: Name of the quality profile to use.
    """

    id: str = Field(..., description="Dataset identifier")
    provider: str = Field(..., description="Data provider")
    name: str = Field(..., description="Dataset name")
    source: SourceConfig = Field(..., description="Source configuration")
    normalize: NormalizeConfig = Field(..., description="Normalization configuration")
    quality_profile: str = Field(..., description="Quality profile name")


class DatasetsConfig(BaseModel):
    """Root configuration model for datasets.yml.

    Attributes:
        datasets: List of dataset configurations.
    """

    datasets: list[DatasetConfig] = Field(..., description="List of datasets")


class ContinuityConfig(BaseModel):
    """Configuration for continuity checks.

    Attributes:
        enabled: Whether continuity checks are enabled.
        max_gap_days: Optional maximum allowed gap in days.
        max_gap_months: Optional maximum allowed gap in months.
    """

    enabled: bool = Field(..., description="Whether continuity checks are enabled")
    max_gap_days: Optional[int] = Field(None, description="Maximum allowed gap in days")
    max_gap_months: Optional[int] = Field(
        None, description="Maximum allowed gap in months"
    )


class OutliersConfig(BaseModel):
    """Configuration for outlier detection.

    Attributes:
        enabled: Whether outlier detection is enabled.
        method: Detection method (e.g., "iqr", "zscore").
        threshold: Threshold value for detection.
    """

    enabled: bool = Field(..., description="Whether outlier detection is enabled")
    method: Optional[str] = Field(None, description="Detection method")
    threshold: Optional[float] = Field(None, description="Detection threshold")


class RangeConfig(BaseModel):
    """Configuration for range validation.

    Attributes:
        enabled: Whether range validation is enabled.
        min_value: Optional minimum allowed value.
        max_value: Optional maximum allowed value.
    """

    enabled: bool = Field(..., description="Whether range validation is enabled")
    min_value: Optional[float] = Field(None, description="Minimum allowed value")
    max_value: Optional[float] = Field(None, description="Maximum allowed value")


class QualityProfileConfig(BaseModel):
    """Configuration for a quality profile.

    Attributes:
        continuity: Continuity check configuration.
        outliers: Outlier detection configuration.
        range: Range validation configuration.
    """

    continuity: ContinuityConfig = Field(..., description="Continuity check config")
    outliers: OutliersConfig = Field(..., description="Outlier detection config")
    range: RangeConfig = Field(..., description="Range validation config")


class QualityProfile(BaseModel):
    """Root configuration model for quality.yml.

    Attributes:
        profiles: Dictionary mapping profile names to configurations.
    """

    profiles: dict[str, QualityProfileConfig] = Field(
        ..., description="Quality profiles"
    )

