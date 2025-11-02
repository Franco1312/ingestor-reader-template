"""Custom domain error types.

These errors represent domain-specific failure modes
that can occur during data processing.
"""


class DomainError(Exception):
    """Base exception for all domain errors."""

    pass


class InvalidSeriesError(DomainError):
    """Raised when a Series entity is invalid or malformed.

    Args:
        message: Error message describing what is invalid.
        series_code: Optional series code that failed validation.
    """

    def __init__(self, message: str, series_code: str | None = None) -> None:
        super().__init__(message)
        self.series_code = series_code


class InvalidObservationError(DomainError):
    """Raised when an Observation entity is invalid or malformed.

    Args:
        message: Error message describing what is invalid.
        observation_index: Optional index of the observation that failed.
    """

    def __init__(self, message: str, observation_index: int | None = None) -> None:
        super().__init__(message)
        self.observation_index = observation_index


class ConfigurationError(DomainError):
    """Raised when configuration is invalid or missing required fields.

    Args:
        message: Error message describing the configuration issue.
        config_key: Optional configuration key that caused the error.
    """

    def __init__(self, message: str, config_key: str | None = None) -> None:
        super().__init__(message)
        self.config_key = config_key

