"""Smoke tests to verify repository setup and basic functionality.

These tests verify that:
- The package can be imported
- The CLI can be invoked
- Basic structure is intact
"""

import subprocess
import sys
from pathlib import Path


def test_import_package() -> None:
    """Test that the package can be imported."""
    import radar_data  # noqa: F401

    assert radar_data.__version__ == "0.1.0"


def test_cli_help() -> None:
    """Test that CLI help command works."""
    result = subprocess.run(
        [sys.executable, "-m", "radar_data.interface.cli.runner", "--help"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent,
    )

    assert result.returncode == 0
    assert "Radar Data Pipeline" in result.stdout
    assert "fetch" in result.stdout
    assert "parse" in result.stdout
    assert "normalize" in result.stdout
    assert "quality" in result.stdout
    assert "write" in result.stdout


def test_cli_fetch_help() -> None:
    """Test that fetch subcommand help works."""
    result = subprocess.run(
        [sys.executable, "-m", "radar_data.interface.cli.runner", "fetch", "--help"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent,
    )

    assert result.returncode == 0
    assert "fetch" in result.stdout.lower()


def test_config_files_exist() -> None:
    """Test that configuration files exist."""
    repo_root = Path(__file__).parent.parent
    datasets_config = repo_root / "configs" / "datasets.yml"
    quality_config = repo_root / "configs" / "quality.yml"

    assert datasets_config.exists(), "configs/datasets.yml should exist"
    assert quality_config.exists(), "configs/quality.yml should exist"

