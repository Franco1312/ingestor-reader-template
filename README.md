# Radar Data Pipeline

A data engineering service for fetching, parsing, normalizing, cleaning, and writing structured data files (CSV, Excel, ZIP) to normalized outputs (Parquet/CSV). This is a **scaffold/template** repository with Clean Architecture principles, providing a solid foundation for building production data pipelines.

## Overview

Radar Data Pipeline is designed as a file-first data ingestion service that:

- **Fetches** files from remote sources (HTTP/HTTPS) or local filesystems
- **Parses** files in various formats (CSV, XLS, XLSX, XLSM, ZIP)
- **Normalizes** raw data into domain entities (Series, Observations)
- **Cleans** data using configurable quality checks (continuity, outliers, range validation)
- **Writes** normalized data to output formats (Parquet, CSV)

## Architecture

The repository follows **Clean Architecture** principles with clear layer boundaries:

- **Domain Layer**: Core entities (Series, Observation, Provenance) and interfaces (ports)
- **Application Layer**: Use cases orchestrating domain ports
- **Infrastructure Layer**: Adapters implementing domain interfaces (HTTP, filesystem, parsers, sinks)
- **Interface Layer**: CLI entrypoints for pipeline operations

## Installation

### Prerequisites

- Python 3.11+
- pip or uv

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd radar-data-pipeline
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
pip install -r requirements-dev.txt
```

4. Setup development tools:
```bash
make setup
```

Or manually:
```bash
pre-commit install
```

## Usage

### CLI Commands

The pipeline provides five main commands for the data processing pipeline:

#### 1. Fetch

Download files from remote sources:

```bash
python -m radar_data.interface.cli.runner fetch <dataset_id> --config configs/datasets.yml --output data/raw
```

**Note**: Currently prints "TODO: implement fetch" - implementation pending.

#### 2. Parse

Parse raw files into structured data:

```bash
python -m radar_data.interface.cli.runner parse <dataset_id> --config configs/datasets.yml --input data/raw --output data/parsed
```

**Note**: Currently prints "TODO: implement parse" - implementation pending.

#### 3. Normalize

Normalize parsed data into domain entities:

```bash
python -m radar_data.interface.cli.runner normalize <dataset_id> --config configs/datasets.yml --input data/parsed --output data/normalized
```

**Note**: Currently prints "TODO: implement normalize" - implementation pending.

#### 4. Quality

Apply quality checks and cleaning:

```bash
python -m radar_data.interface.cli.runner quality <dataset_id> --config configs/datasets.yml --input data/normalized --output data/quality
```

**Note**: Currently prints "TODO: implement quality checks" - implementation pending.

#### 5. Write

Write normalized data to output formats:

```bash
python -m radar_data.interface.cli.runner write <dataset_id> --config configs/datasets.yml --input data/normalized --output data/output --format parquet
```

**Note**: Currently prints "TODO: implement write" - implementation pending.

### Help

View available commands:

```bash
python -m radar_data.interface.cli.runner --help
```

View help for a specific command:

```bash
python -m radar_data.interface.cli.runner fetch --help
```

## Configuration

### Dataset Configuration (`configs/datasets.yml`)

Defines datasets to process, including source URLs, parsing settings, and normalization rules:

```yaml
datasets:
  - id: example_bcra_reservas
    provider: BCRA
    name: "BCRA International Reserves"
    source:
      type: static_url
      url: ""  # TODO: Add real URL
      sheet: ""
      start_cell: ""
      columns:
        date: ""
        value: ""
    normalize:
      internal_series_code: "BCRA_RESERVES"
      unit: "USD"
      frequency: "daily"
    quality_profile: "default_daily"
```

### Quality Configuration (`configs/quality.yml`)

Defines quality profiles for data validation:

```yaml
profiles:
  default_daily:
    continuity:
      enabled: true
    outliers:
      enabled: true
    range:
      enabled: false
```

## Extending the Pipeline

### Adding a New Parser Plugin

1. Create a new parser class in `src/radar_data/infrastructure/parse/plugins/`:

```python
from radar_data.domain.interfaces import ParserPort

class MyDatasetParser(ParserPort):
    def parse(self, file_path: str, dataset_config: dict) -> list[dict]:
        # Implementation here
        pass

    def supports(self, file_path: str) -> bool:
        return file_path.endswith(".myformat")
```

2. Register the parser in the parser registry (when implemented).

3. Update `configs/datasets.yml` with dataset-specific configuration.

### Adding a New Use Case

1. Create a new use case in `src/radar_data/application/use_cases/`:

```python
from radar_data.domain.interfaces import SomePort

class MyUseCase:
    def __init__(self, adapter: SomePort):
        self.adapter = adapter

    def execute(self, ...):
        # Implementation here
        pass
```

2. Add CLI handler in `src/radar_data/interface/cli/runner.py`.

## Development

### Makefile Targets

- `make setup`: Install dev dependencies and setup pre-commit
- `make lint`: Run ruff linter
- `make type`: Run mypy type checker
- `make test`: Run pytest tests
- `make format`: Format code with ruff
- `make run`: Example CLI invocation (prints help)
- `make build`: Build Docker image
- `make clean`: Remove cache and build artifacts

### Linting and Type Checking

```bash
make lint   # Run ruff
make type   # Run mypy
make format # Auto-format code
```

### Running Tests

```bash
make test
```

Or with coverage:

```bash
pytest tests/ --cov=radar_data --cov-report=html
```

### Docker

Build the Docker image:

```bash
make build
```

Or use docker-compose:

```bash
docker-compose up
```

## Project Structure

```
radar-data-pipeline/
├── configs/                    # Configuration files
│   ├── datasets.yml            # Dataset definitions
│   └── quality.yml             # Quality profiles
├── src/
│   └── radar_data/
│       ├── domain/             # Domain layer (entities, interfaces)
│       ├── application/        # Application layer (use cases)
│       ├── infrastructure/     # Infrastructure layer (adapters)
│       └── interface/          # Interface layer (CLI)
├── tests/                      # Test suite
├── Makefile                    # Development commands
├── pyproject.toml             # Package configuration
├── requirements.txt           # Runtime dependencies
└── requirements-dev.txt       # Development dependencies
```

## TODO

This is a scaffold repository. The following components need implementation:

### Core Functionality
- [ ] Implement file fetching (HTTP fetcher with ETag/Last-Modified support)
- [ ] Implement file parsing (CSV, Excel readers)
- [ ] Implement data normalization (column mapping, date parsing, unit conversion)
- [ ] Implement quality checks (continuity, outliers, range validation)
- [ ] Implement data writing (Parquet, CSV writers)

### Infrastructure
- [ ] Add S3 filesystem support
- [ ] Add ZIP file extraction
- [ ] Add parser registry/discovery for plugins
- [ ] Add configuration caching
- [ ] Add retry logic for network operations

### Domain
- [ ] Implement domain invariants and validation
- [ ] Add provenance tracking
- [ ] Add data lineage tracking

### Developer Experience
- [ ] Add comprehensive tests
- [ ] Add integration tests
- [ ] Add logging configuration
- [ ] Add error handling and recovery

## License

MIT License (or as specified in your repository)

## Contributing

This is a template/scaffold repository. When implementing business logic, follow these guidelines:

1. Keep domain logic in the domain layer
2. Use dependency injection for ports/adapters
3. Add comprehensive tests for new features
4. Follow Clean Architecture principles
5. Maintain type hints and docstrings
