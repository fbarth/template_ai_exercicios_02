# AI Exercise Template - Elevator Search Problem

This repository contains a template for AI exercises focusing on search algorithms applied to an elevator problem. Students implement a search solution in `Elevador.py` that finds optimal paths for an elevator to move between floors using different search strategies.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Setup
- Verify Python 3.12+ is available: `python3 --version` -- takes < 1 second
- Install dependencies: `pip3 install -r requirements.txt` -- takes 1-3 seconds for fresh install, < 1 second if already installed
- Verify installation: `python3 -c "import pytest; import aigyminsper; print('Dependencies OK')"` -- takes < 1 second

### Testing
- Run tests: `python3 -m pytest test_elevador.py -v` -- takes < 1 second when working, < 1 second when failing
- Check test collection: `python3 -m pytest test_elevador.py --collect-only` -- takes < 1 second (will fail if Elevador.py missing)
- Run specific test: `python3 -m pytest test_elevador.py::test_2_bl -v` -- takes < 1 second

### Code Validation
- Check Python syntax: `python3 -m py_compile [filename.py]` -- takes < 1 second
- Validate test file: `python3 -m py_compile test_elevador.py` -- takes < 1 second

## Project Structure and Requirements

### Repository Contents
```
.
├── requirements.txt       # Dependencies: pytest, aigyminsper
├── test_elevador.py      # Test cases for elevator search algorithms
├── .gitignore           # Python gitignore (excludes __pycache__, .pytest_cache, etc.)
└── Elevador.py          # MISSING - Students must implement this file
```

### Implementation Requirements
Students must create `Elevador.py` with a `main(start_floor, target_floor, search_strategy)` function that:

1. **Input Parameters:**
   - `start_floor`: Starting floor (integer, typically 0)
   - `target_floor`: Destination floor (integer, > start_floor)
   - `search_strategy`: String indicating search algorithm ('BL', 'BP', 'BPI')

2. **Output Format:**
   - Must print to stdout in exact format: `"Solução: ; [action1] ; [action2] ; ..."`
   - Actions are either `"subir 1 andar"` (go up 1 floor) or `"subir 2 andares"` (go up 2 floors)
   - Note: Exact spacing is critical - `"Solução: "` (one space after colon, one space after each semicolon)

3. **Search Strategies:**
   - **BL**: Prefers 2-floor moves when possible, uses 1-floor moves only when necessary
   - **BP**: Only uses 1-floor moves
   - **BPI**: Mixed strategy - for 3-floor targets, starts with 1-floor move then uses 2-floor moves

### Example Expected Outputs
```python
main(0, 2, 'BL')   # → "Solução: ; subir 2 andares"
main(0, 3, 'BL')   # → "Solução: ; subir 2 andares ; subir 1 andar"
main(0, 2, 'BP')   # → "Solução: ; subir 1 andar ; subir 1 andar"
main(0, 3, 'BPI')  # → "Solução: ; subir 1 andar ; subir 2 andares"
```

## Validation and Testing

### Manual Validation Steps
After implementing `Elevador.py`, always run through this complete validation:

1. **Syntax Check:** `python3 -m py_compile Elevador.py`
2. **Import Test:** `python3 -c "from Elevador import main; print('Import successful')"`
3. **Manual Test:** `python3 -c "from Elevador import main; main(0, 2, 'BL')"`
4. **Full Test Suite:** `python3 -m pytest test_elevador.py -v`
5. **Specific Strategy Tests:**
   - BL tests: `python3 -m pytest test_elevador.py -k "bl" -v`
   - BP tests: `python3 -m pytest test_elevador.py -k "bp" -v`
   - BPI tests: `python3 -m pytest test_elevador.py -k "bpi" -v`

### Test Scenarios
The test suite includes 9 test cases covering:
- **BL Strategy:** Tests for 2, 3, and 10-floor targets
- **BP Strategy:** Tests for 2, 3, and 10-floor targets
- **BPI Strategy:** Tests for 2, 3, and 10-floor targets

When working correctly, all 9 tests should pass in < 1 second.

## Common Tasks and Troubleshooting

### Fresh Environment Setup
```bash
# Clean setup from scratch
python3 --version              # Verify Python 3.12+
pip3 install -r requirements.txt
python3 -c "import pytest; import aigyminsper"  # Verify dependencies
```

### Common Errors and Solutions

1. **ModuleNotFoundError: No module named 'Elevador'**
   - Missing `Elevador.py` file - students must implement this
   - Check: `ls -la Elevador.py`

2. **AssertionError in tests**
   - Output format doesn't match exactly
   - Check spacing in "Solução: " prefix
   - Verify action strings: "subir 1 andar" vs "subir 2 andares"

3. **Import errors in Elevador.py**
   - Run `python3 -m py_compile Elevador.py` to check syntax
   - Ensure `main` function is properly defined

### Development Tips
- Always test individual cases before running full suite
- Use `python3 -c "from Elevador import main; main(0, 2, 'BL')"` for quick validation
- Pay attention to Portuguese text - "andar" (singular) vs "andares" (plural)
- The output format is very strict - spaces and semicolons must match exactly

## Dependencies
- **pytest**: Testing framework
- **aigyminsper**: AI gym library for educational AI exercises

Both dependencies install quickly (< 3 seconds total) and have no complex build requirements.