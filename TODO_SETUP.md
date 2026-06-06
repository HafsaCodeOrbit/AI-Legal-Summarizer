# Setup Fixes

## Current issue
- Running `python app.py` fails with: `ModuleNotFoundError: No module named 'flask'`.

## Steps
1. Create/activate a project virtual environment.
2. Install dependencies from `requirements.txt` into that environment.
3. Re-run `python app.py` to confirm Flask imports successfully.

## Notes
- If you have multiple Python installations, ensure VSCode/terminal uses the same interpreter as the one where dependencies were installed.

