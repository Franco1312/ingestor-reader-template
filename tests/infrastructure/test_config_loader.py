"""Tests for configuration loader.

TODO: Implement actual config loader tests when loader logic is added.
"""

from pathlib import Path

from radar_data.infrastructure.config.loader import load_configs


def test_config_loader_import() -> None:
    """Test that config loader can be imported.

    TODO: Add actual loader tests when loader logic is implemented.
    """
    assert load_configs is not None

    # This test just verifies the function exists
    # Actual loading tests will be added when logic is implemented
    # repo_root = Path(__file__).parent.parent.parent
    # datasets_config = repo_root / "configs" / "datasets.yml"
    # quality_config = repo_root / "configs" / "quality.yml"
    #
    # datasets, quality_profiles = load_configs(datasets_config, quality_config)
    # assert len(datasets) > 0
    # assert len(quality_profiles) > 0

