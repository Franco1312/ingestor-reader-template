"""Use case for normalizing raw parsed data into domain entities."""

from radar_data.domain.entities import Observation, Series
from radar_data.domain.interfaces import NormalizerPort


class NormalizeUseCase:
    """Orchestrates data normalization operations.

    This use case coordinates the normalization of raw parsed data into
    domain entities using the NormalizerPort interface. It handles
    column mapping, unit conversions, date parsing, and entity creation.

    TODO:
        - Implement normalize logic using NormalizerPort.
        - Add validation of normalized entities.
        - Add support for batch normalization.
        - Add provenance tracking for normalized data.
    """

    def __init__(self, normalizer: NormalizerPort) -> None:
        """Initialize the normalize use case.

        Args:
            normalizer: Implementation of NormalizerPort to use for normalization.
        """
        self.normalizer = normalizer

    def execute(
        self,
        raw_records: list[dict[str, str | float]],
        dataset_config: dict,
    ) -> tuple[Series, list[Observation]]:
        """Execute the normalization operation.

        Args:
            raw_records: List of raw dictionaries from parser.
            dataset_config: Configuration dict with normalize section
                (internal_series_code, unit, frequency).

        Returns:
            Tuple of (Series, list[Observations]) representing the normalized data.

        Raises:
            ValueError: If normalization fails (e.g., missing required fields).
        """
        # TODO: Implement normalize logic
        # return self.normalizer.normalize(raw_records, dataset_config)
        pass

