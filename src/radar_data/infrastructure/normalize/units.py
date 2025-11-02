"""Unit conversion utilities.

Provides functions for converting between different units
of measurement needed for normalization.
"""

from typing import Any


def convert_unit(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a value from one unit to another.

    Args:
        value: Value to convert.
        from_unit: Source unit (e.g., "USD", "ARS", "index_base_100").
        to_unit: Target unit.

    Returns:
        Converted value.

    Raises:
        ValueError: If conversion is not supported.

    TODO:
        - Implement unit conversion logic.
        - Add support for currency conversion (requires exchange rates).
        - Add support for index transformations.
        - Add unit validation.
    """
    # TODO: Implement unit conversion
    # if from_unit == to_unit:
    #     return value
    #
    # # Currency conversions would require exchange rate data
    # # Index transformations would require base period information
    # raise ValueError(f"Unit conversion from {from_unit} to {to_unit} not supported")
    pass


def validate_unit(unit: str) -> bool:
    """Validate that a unit string is recognized.

    Args:
        unit: Unit string to validate.

    Returns:
        True if unit is valid, False otherwise.

    TODO:
        - Define list of supported units.
        - Implement validation logic.
    """
    # TODO: Implement unit validation
    # supported_units = ["USD", "ARS", "index_base_100", "percentage", "count"]
    # return unit in supported_units
    pass

