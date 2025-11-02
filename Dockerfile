FROM python:3.11-slim

WORKDIR /app

# Install minimal system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -e . && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY configs/ ./configs/

# Set Python path
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Default command: print CLI help
CMD ["python", "-m", "radar_data.interface.cli.runner", "--help"]

