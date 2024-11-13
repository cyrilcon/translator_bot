# Build stage
FROM python:3.12-slim AS builder

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir poetry

WORKDIR /usr/src/app/translator_bot

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Final stage
FROM python:3.12-slim

WORKDIR /usr/src/app/translator_bot

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Command to run the bot
CMD ["python", "-m", "main"]