"""Tests for domain entities.

TODO: Implement actual entity tests when domain logic is added.
"""

from datetime import datetime

from radar_data.domain.entities import Observation, Provenance, Series


def test_series_creation() -> None:
    """Test creating a Series entity.

    TODO: Add validation tests when domain invariants are implemented.
    """
    series = Series(
        code="TEST_SERIES",
        name="Test Series",
        unit="USD",
        frequency="daily",
        provider="TEST_PROVIDER",
    )

    assert series.code == "TEST_SERIES"
    assert series.name == "Test Series"
    assert series.unit == "USD"
    assert series.frequency == "daily"
    assert series.provider == "TEST_PROVIDER"


def test_observation_creation() -> None:
    """Test creating an Observation entity.

    TODO: Add validation tests when domain invariants are implemented.
    """
    series = Series(
        code="TEST_SERIES",
        name="Test Series",
        unit="USD",
        frequency="daily",
        provider="TEST_PROVIDER",
    )

    observation = Observation(
        series_code=series.code,
        timestamp=datetime(2024, 1, 1),
        value=100.0,
    )

    assert observation.series_code == "TEST_SERIES"
    assert observation.timestamp == datetime(2024, 1, 1)
    assert observation.value == 100.0


def test_provenance_creation() -> None:
    """Test creating a Provenance entity.

    TODO: Add validation tests when domain invariants are implemented.
    """
    provenance = Provenance(
        source_url="https://example.com/data.csv",
        fetched_at=datetime(2024, 1, 1),
        dataset_id="test_dataset",
        file_hash="abc123",
    )

    assert provenance.source_url == "https://example.com/data.csv"
    assert provenance.dataset_id == "test_dataset"
    assert provenance.file_hash == "abc123"

