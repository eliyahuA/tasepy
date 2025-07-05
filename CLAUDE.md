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

#### Progressive Extension Pattern and DRY Principle Implementation
- **Progressive Extension Pattern**: Build inheritance hierarchies where each class adds specific functionality while reusing parent logic via `super()`
- **DRY Principle Implementation**: Eliminate code duplication through inheritance - each class should only define its additional fields and extend parent behavior rather than duplicate it

### Domain-Agnostic Documentation Principles

**Keep architectural documentation domain-neutral**:
- ❌ **Avoid**: Hardcoding specific domains/endpoints in foundational component docs
- ✅ **Do**: Focus on system capabilities and architectural patterns
- **Example**: Instead of "for funds and indices endpoints" → "for API endpoints"

**Why domain-agnostic documentation matters**:
- **Future-proofing**: APIs naturally expand beyond initial scope
- **Maintenance**: Avoids updating docs every time domains are added  
- **Accuracy**: Prevents misleading scope limitations on general-purpose systems
- **Focus**: Keeps architectural docs on patterns, not current usage

**Proper domain documentation placement**:
- ✅ Domain-specific packages (`funds/__init__.py`, `indices_basic/__init__.py`)
- ✅ Client method docstrings (where specific endpoints are used)
- ❌ Base classes and architectural foundation components

**Red flags to avoid**:
- "for X and Y endpoints" → use "for API endpoints"
- "handles A, B, C data" → use "handles API response data" 
- Listing current domains in architectural documentation

### Code Examination Guidelines

**CRITICAL: Always examine actual code implementation before writing documentation or making assumptions**

#### Pre-Documentation Checklist
Before writing any documentation, docstrings, or making claims about functionality:

1. **Read the actual implementation**:
   - Use Read tool to examine relevant source files
   - Check constants, default values, and configuration
   - Verify method signatures and parameters

2. **Examine usage patterns**:
   - Look at existing tests and examples in the codebase
   - Check how functions/classes are actually used
   - Review sample data and configuration files

3. **Verify assumptions with code**:
   - Never assume default values - check constants and code
   - Never assume data structures - examine models and schemas
   - Never assume naming conventions - verify in actual implementations

#### Documentation Anti-Patterns to Avoid
- ❌ **Assuming environment variable names** without checking constants
- ❌ **Guessing data model structures** without reading Pydantic models
- ❌ **Making up configuration formats** without examining actual config files
- ❌ **Copying patterns from other projects** without verifying local implementation

#### Fact-Based Documentation Process
1. **Examine first**: Read relevant source code files
2. **Verify second**: Check tests, examples, and sample data
3. **Document third**: Write documentation based on observed facts
4. **Cross-reference**: Ensure consistency with existing documentation

**Remember**: Documentation should reflect what the code actually does, not what we think it should do.

## Adding Domain Specific Client
Addition starts by adding domain's OpenAPI specs to `tase openapi specs`.
You will be told the file name with the new specs.

### Extracting Endpoints
1. Update `endpoints.yaml` with the endpoints from the specs
2. Follow existing patterns
3. If you cannot implement with existing patterns, holt and ask the user how to proceed

### Adding Domain Specific Client
  1. **Examine existing implementations first** - Read funds.py and indices_basic.py to understand the patterns                 
  2. **Check parameter handling** - Look at requests_/ folder to understand how headers, query params, and path params are handled
  3. **Extract all securities endpoints** from securities-basic.yaml OpenAPI spec
  4. **Follow exact patterns** - Same structure, imports, error handling as existing domain clients
  5. **Use ForgivingResponse** for all response models
  6. **Add any missing infrastructure** - Create new resource parameters or headers classes if needed for path parameters
  7. **Update client.py** to expose the new domain client
  8. **Update urls.py** to include the new endpoints 
  9. **Include comprehensive docstrings** following project guidelines. Do not document the `Returns` part for domain client methods because you haven't studies samples of return data yet.

### Implement Endpoints
The following actions should be repeated per an endpoint of the domain specific client you have prepared in the last stage

#### Retrieving Data Samples
1. Choose the next domain specific endpoint that wasn't processed yet
2. Use `dev-tools\data-sample-fetcher.py` script to retrieve a json sample fot the endpoint
3. You can change the code in the script file as necessary to achieve your goal of getting the data sample

#### Creating Typed Response Models
1. Analyze the JSON response structure and data patterns
2. Create proper Pydantic response model in the appropriate responses/ subdirectory
3. Follow existing response model patterns and inheritance from ResponseComponent
4. Replace ForgivingResponse with the new typed model in the domain client method
5. Update method docstring with proper return type documentation based on actual data structure


## API Integration

This is a Python SDK for the TASE (Tel Aviv Stock Exchange) DataWise API:
- Base URL: `https://datawise.tase.co.il/v1`
- Two main domains: `funds` and `indices` (basic)
- Requires API key authentication
- Handles request validation and response parsing automatically