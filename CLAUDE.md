# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing
- Run all tests: `pytest`
- Run unit tests only: `pytest tests/unit/`
- Run integration tests only: `pytest tests/integration/`
- Run specific test file: `pytest tests/unit/responses/funds/test_funds.py`
- Run with verbose output: `pytest -v`

### Development Setup
- Install dependencies: `pip install -r requirements.txt`
- Install dev dependencies: `pip install -r dev-requirements.txt`
- Build package: `python -m build`

### Environment Setup
- Integration tests require an API key from TASE (Tel Aviv Stock Exchange)
- Set API_KEY environment variable or create a `.env` file
- API key can also be loaded from YAML file (see `API key.yaml` template)

### Git Commit Guidelines
- **IMPORTANT**: Always use "claude" as the author/committer identity for all commits
- Use this exact commit command format:
```bash
GIT_COMMITTER_NAME="claude" GIT_COMMITTER_EMAIL="claude@anthropic.com" git commit --author="claude <claude@anthropic.com>" -m "$(cat <<'EOF'
[Your commit message here]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

## Architecture Overview

### Core Components

**Client Architecture**: Multi-layered client system with two main implementations:
- `clients/openapi3/`: OpenAPI 3.0 generated client
- `clients/tailored/`: Custom tailored client with domain-specific methods

**Tailored Client Structure**:
- `Client`: Main entry point with `funds` and `indices_basic` properties
- `Funds`: Handles all fund-related API calls (fund lists, classifications, exposures, etc.)
- `IndicesBasic`: Handles basic indices operations (list, components)
- `BaseClient`: Shared functionality for request handling and configuration

**Request/Response Pattern**:
- `requests_/`: Contains URL definitions, parameters, headers, and enums
- `responses/`: Pydantic models for API responses, organized by domain (funds, indices_basic)
- `endpoints/`: YAML-based endpoint configuration with factory pattern

**Settings & Configuration**:
- `SettingsBuilder`: Fluent API for configuration
- Supports API key from environment variables or YAML files
- `endpoints.yaml`: Centralized endpoint definitions

### Key Architectural Patterns

**Factory Pattern**: `YAMLFactory` creates endpoint models from YAML configuration<br>
**Repository Pattern**: Domain-specific classes (`Funds`, `IndicesBasic`) encapsulate API operations<br>
**Response Transformation**: All API responses are validated and transformed through Pydantic models<br>
**Flexible Authentication**: Multiple API key sources (environment, file, direct)

### Testing Strategy

**Unit Tests**: Focus on response parsing and model validation using JSON samples<br>
**Integration Tests**: Full API calls requiring valid API key<br>
**Test Fixtures**: Centralized client configuration in `tests/integration/client/conftest.py`<br>
**Sample Data**: JSON response samples stored in `tests/unit/responses/*/samples/`<br>

### Docstring Writing Guidelines

When writing docstrings for domain-specific client methods (e.g., in `Funds`, `IndicesBasic` classes) that return Pydantic models:

1. **Always examine sample JSON data** in `tests/unit/responses/*/samples/` to understand the data structure
2. **Use concise, descriptive language** following the pattern:
   - First line: "Get [classification/data type] for [domain]"
   - Second paragraph: Brief explanation of what the data represents and its purpose
   - Returns section: "[DataType] pydantic data model including [brief description of contents]"
3. **Sample JSON examination helps identify**:
   - Data structure and hierarchy
   - Available codes, classifications, or categories
   - Language used (Hebrew/English descriptions)
   - Total counts and result arrays

### Module vs Class Docstring Guidelines

**Avoid redundant documentation**: If a module contains a single primary class and both would have essentially the same docstring, document only the class. Only add module docstrings when they provide additional context beyond what the class docstring covers.

**Documentation Conciseness**:
- Each docstring should add unique value without restating concepts
- Documentation should be concise and focused

### Code Writing Guidelines

- When code is self-documenting, avoid adding docstrings.

### API Integration

This is a Python SDK for the TASE (Tel Aviv Stock Exchange) DataWise API:
- Base URL: `https://datawise.tase.co.il/v1`
- Two main domains: `funds` and `indices` (basic)
- Requires API key authentication
- Handles request validation and response parsing automatically