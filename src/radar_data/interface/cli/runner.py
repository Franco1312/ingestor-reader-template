"""CLI entrypoint for radar-data-pipeline.

This module provides the command-line interface for the pipeline,
with subcommands for each stage: fetch, parse, normalize, quality, write.
"""

import argparse
import sys
from pathlib import Path


def main() -> None:
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="Radar Data Pipeline - Data ingestion, normalization, and cleaning service",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--config",
        type=str,
        default="configs/datasets.yml",
        help="Path to datasets configuration file (default: configs/datasets.yml)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Fetch command
    fetch_parser = subparsers.add_parser("fetch", help="Fetch files from remote sources")
    fetch_parser.add_argument(
        "dataset_id",
        type=str,
        help="Dataset ID to fetch",
    )
    fetch_parser.add_argument(
        "--output",
        type=str,
        default="data/raw",
        help="Output directory for fetched files (default: data/raw)",
    )

    # Parse command
    parse_parser = subparsers.add_parser("parse", help="Parse raw files into structured data")
    parse_parser.add_argument(
        "dataset_id",
        type=str,
        help="Dataset ID to parse",
    )
    parse_parser.add_argument(
        "--input",
        type=str,
        default="data/raw",
        help="Input directory for raw files (default: data/raw)",
    )
    parse_parser.add_argument(
        "--output",
        type=str,
        default="data/parsed",
        help="Output directory for parsed files (default: data/parsed)",
    )

    # Normalize command
    normalize_parser = subparsers.add_parser(
        "normalize", help="Normalize parsed data into domain entities"
    )
    normalize_parser.add_argument(
        "dataset_id",
        type=str,
        help="Dataset ID to normalize",
    )
    normalize_parser.add_argument(
        "--input",
        type=str,
        default="data/parsed",
        help="Input directory for parsed files (default: data/parsed)",
    )
    normalize_parser.add_argument(
        "--output",
        type=str,
        default="data/normalized",
        help="Output directory for normalized files (default: data/normalized)",
    )

    # Quality command
    quality_parser = subparsers.add_parser(
        "quality", help="Apply quality checks and cleaning to normalized data"
    )
    quality_parser.add_argument(
        "dataset_id",
        type=str,
        help="Dataset ID to check",
    )
    quality_parser.add_argument(
        "--input",
        type=str,
        default="data/normalized",
        help="Input directory for normalized files (default: data/normalized)",
    )
    quality_parser.add_argument(
        "--output",
        type=str,
        default="data/quality",
        help="Output directory for quality reports (default: data/quality)",
    )

    # Write command
    write_parser = subparsers.add_parser(
        "write", help="Write normalized data to output formats (Parquet/CSV)"
    )
    write_parser.add_argument(
        "dataset_id",
        type=str,
        help="Dataset ID to write",
    )
    write_parser.add_argument(
        "--input",
        type=str,
        default="data/normalized",
        help="Input directory for normalized files (default: data/normalized)",
    )
    write_parser.add_argument(
        "--output",
        type=str,
        default="data/output",
        help="Output directory for output files (default: data/output)",
    )
    write_parser.add_argument(
        "--format",
        type=str,
        choices=["parquet", "csv"],
        default="parquet",
        help="Output format (default: parquet)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Validate config file exists
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Error: Configuration file not found: {args.config}", file=sys.stderr)
        sys.exit(1)

    # Route to appropriate handler
    if args.command == "fetch":
        handle_fetch(args)
    elif args.command == "parse":
        handle_parse(args)
    elif args.command == "normalize":
        handle_normalize(args)
    elif args.command == "quality":
        handle_quality(args)
    elif args.command == "write":
        handle_write(args)
    else:
        print(f"Error: Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)


def handle_fetch(args: argparse.Namespace) -> None:
    """Handle fetch command.

    Args:
        args: Parsed command-line arguments.

    TODO:
        - Load dataset configuration.
        - Initialize FetchUseCase with FetcherPort adapter.
        - Execute fetch operation.
    """
    print(f"TODO: implement fetch for dataset '{args.dataset_id}'")
    print(f"  Config: {args.config}")
    print(f"  Output: {args.output}")
    # TODO: Implement fetch logic
    # from radar_data.infrastructure.config.loader import load_configs
    # from radar_data.infrastructure.net.http_fetcher import HttpFetcher
    # from radar_data.application.use_cases.fetch_use_case import FetchUseCase
    #
    # datasets, _ = load_configs(args.config)
    # dataset = next((d for d in datasets if d["id"] == args.dataset_id), None)
    # if not dataset:
    #     print(f"Error: Dataset '{args.dataset_id}' not found", file=sys.stderr)
    #     sys.exit(1)
    #
    # fetcher = HttpFetcher()
    # use_case = FetchUseCase(fetcher)
    # use_case.execute(dataset["source"]["url"], args.output)
    sys.exit(0)


def handle_parse(args: argparse.Namespace) -> None:
    """Handle parse command.

    Args:
        args: Parsed command-line arguments.

    TODO:
        - Load dataset configuration.
        - Initialize ParseUseCase with ParserPort adapter.
        - Execute parse operation.
    """
    print(f"TODO: implement parse for dataset '{args.dataset_id}'")
    print(f"  Config: {args.config}")
    print(f"  Input: {args.input}")
    print(f"  Output: {args.output}")
    # TODO: Implement parse logic
    sys.exit(0)


def handle_normalize(args: argparse.Namespace) -> None:
    """Handle normalize command.

    Args:
        args: Parsed command-line arguments.

    TODO:
        - Load dataset configuration.
        - Initialize NormalizeUseCase with NormalizerPort adapter.
        - Execute normalize operation.
    """
    print(f"TODO: implement normalize for dataset '{args.dataset_id}'")
    print(f"  Config: {args.config}")
    print(f"  Input: {args.input}")
    print(f"  Output: {args.output}")
    # TODO: Implement normalize logic
    sys.exit(0)


def handle_quality(args: argparse.Namespace) -> None:
    """Handle quality command.

    Args:
        args: Parsed command-line arguments.

    TODO:
        - Load dataset and quality configuration.
        - Initialize QualityUseCase with CleanerPort adapter.
        - Execute quality checks.
    """
    print(f"TODO: implement quality checks for dataset '{args.dataset_id}'")
    print(f"  Config: {args.config}")
    print(f"  Input: {args.input}")
    print(f"  Output: {args.output}")
    # TODO: Implement quality logic
    sys.exit(0)


def handle_write(args: argparse.Namespace) -> None:
    """Handle write command.

    Args:
        args: Parsed command-line arguments.

    TODO:
        - Load dataset configuration.
        - Initialize WriteUseCase with SinkPort adapter.
        - Execute write operation.
    """
    print(f"TODO: implement write for dataset '{args.dataset_id}'")
    print(f"  Config: {args.config}")
    print(f"  Input: {args.input}")
    print(f"  Output: {args.output}")
    print(f"  Format: {args.format}")
    # TODO: Implement write logic
    sys.exit(0)


if __name__ == "__main__":
    main()

