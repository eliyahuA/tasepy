## Adding Domain Specific Client
Addition starts by adding domain's OpenAPI specs to `tasepy\tase openapi specs\`.
You have need to implement a domain client according to the OpenAPI spec file $ARGUMENTS 
Follow the following steps and act according to project guidelines in your memory.

### Extracting Endpoints
1. Update `tasepy\endpoints\endpoints.yaml` with the endpoints from the specs
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
3. When creating response models, thoroughly examine the actual JSON sample data to identify data quality issues 
   1. Check for null values: Scan the entire JSON file for any fields that contain null values and mark those fields as
  Optional[FieldType]
   2. Check array consistency: For fields nested under array items (result[]), examine multiple items (not just the first few) to see if some items are missing fields that others have - mark inconsistent fields as optional
   3. Use search tools: Use rg "null" or similar tools to systematically find all null values in the JSON samples rather than just reading the first few lines"
   4. Verify field naming: Compare JSON field names with current default alias generator for response modules, add Field(alias="originalName") for any mismatches (e.g., security_id will be converted to securityId by the alias generator, while securityID is the actual name in the JSON)
4. Follow existing response model patterns and inheritance from ResponseComponent
5. Replace ForgivingResponse with the new typed model in the domain client method
6. Update method docstring with proper return type documentation based on actual data structure

### Creating Response Tests
1. Read the existing tests for funds and indices in /tests/unit/responses/funds or /indices_basic
2. Create similar test package for the specific domain you are currently working on
3. Execute the tests

### Creating Domain Specific Integration Tests
1. Read the existing tests for funds and indices in /tests/integration/client/test_basic_indices and test_funds
2. Create similar test package for the specific domain you are currently working on
3. Execute the tests