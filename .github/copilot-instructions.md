# DeviceTest Guard repository instructions

- This is a fictional Python 3.11+ workshop project using only the standard library.
- Never invent or include Intel confidential information, customer data, real device specifications, credentials, or production endpoints.
- Treat temperature and voltage limits as fictional training constants defined in the repository.
- Preserve public function signatures unless a requirement explicitly changes them.
- Prefer small, readable functions with type hints and concise docstrings.
- Use `unittest`; add boundary, negative, empty-input, and duplicate-identifier tests where relevant.
- Run focused tests first, then `python -m unittest discover -s tests -v`.
- Explain assumptions, show the proposed plan before multi-file changes, and require human review of generated code.
