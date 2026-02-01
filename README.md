# my_utils

A lightweight, reusable Python utility package providing common validation and formatting helpers.  
Designed for educational purposes and portfolio demonstration, with a focus on clean architecture, reusability, and documentation.

---

## Features

- Email validation utility
- Dictionary-to-log string formatter
- Clean, modular design following best practices
- Fully documented and installable Python package

---

## Project Structure

```text
my_utils/
├── setup.py
├── README.md
├── test_script.py
└── my_utils/
    ├── __init__.py
    ├── validators.py
    └── formatters.py
```

---

## Installation
Clone the repository and install locally:
git clone https://github.com/cherryaugusta/my_utils-sdgla3.git
cd my_utils
pip install .

---

## Usage
Email Validation
from my_utils import is_valid_email

is_valid_email("user@example.com")
Dictionary Formatting for Logs
from my_utils import format_dict_for_log

data = {"status": "ERROR", "code": 500}
print(format_dict_for_log(data))
Output:
status => ERROR
code => 500

---

## Design Principles
•	Single Responsibility Principle (SRP)
Each module serves one clearly defined purpose.
•	Don't Repeat Yourself (DRY)
Shared logic is centralized in a reusable package.
•	Explicit Public API
Public functions are exposed via __init__.py.
•	Documentation First
Every function includes clear docstrings.

---

## Disclaimer
This repository is intended strictly for educational purposes and portfolio demonstration.
The email validation logic is intentionally simplified and should not be used in production systems requiring full RFC-compliant validation. No warranties are provided, express or implied, and the author assumes no responsibility for misuse or reliance on this code in real-world applications.
