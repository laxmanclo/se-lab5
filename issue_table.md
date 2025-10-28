# Issues Found and Fixed

| Issue Type | Tool | Line(s) | Description | Fix Approach |
|------------|------|---------|-------------|--------------|
| Mutable default argument | Pylint (W0102) | 10 | `logs=[]` is dangerous - same list reused across function calls causing bugs | Changed to `logs=None` and initialize as empty list inside function |
| Dangerous eval() usage | Bandit (B307) | 60 | `eval()` allows arbitrary code execution - major security vulnerability | Removed eval() and replaced with safe print statement |
| Bare exception catch | Pylint/Bandit | 22 | `except:` catches ALL exceptions including system exits | Changed to `except KeyError:` to catch specific exception only |
| File not closed properly | Bandit (B110) | 29, 36 | Files opened with `open()` but might not close if error occurs | Used context manager `with open()` to ensure files always close |
| Old string formatting | Flake8 | 16 | Using old `%s` style formatting instead of modern f-strings | Changed to f-string: `f"{datetime.now()}: Added {qty} of {item}"` |
| Missing docstrings | Pylint (C0116) | All functions | No documentation for functions | Added docstrings to all functions explaining parameters and returns |
| No type validation | Custom | 13, 47 | Functions accept any type without checking, causing crashes | Added `isinstance()` checks for item (string) and qty (integer) |
| Global variable misuse | Pylint (W0603) | Throughout | Using global keyword unnecessarily | Kept minimal global usage, documented why it's needed |
| Variable naming | Flake8 (N806) | 44, 51 | Using `i` instead of descriptive names | Changed to `item` and `quantity` for clarity |
| Missing error handling | Custom | 27, 38 | `getQty()` can crash on missing item, `loadData()` can crash on missing file | Added try-except blocks with specific exceptions and error messages |
