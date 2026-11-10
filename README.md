# API Testing Lab — QuickPizza

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KppysN/api-lab.git
   cd api-lab
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run all tests:
   ```bash
   pytest -v
   ```

5. Generate the HTML test report:
   ```bash
   pytest -v --html=report.html --self-contained-html
   ```

## Input Space Partitioning — Part A

**API:** `POST /api/ratings`

### Input Domain Model

| Characteristic | Blocks | Values in the tests | Test Cases |
|---|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 | `test_stars_out_of_range[0]`, `test_base_choice_is_saved`, `test_stars_out_of_range[6]` |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field | `test_base_choice_is_saved`, `test_stars_decimal_is_refused`, `test_stars_text_is_refused`, `test_stars_missing_is_refused` |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 | `test_base_choice_is_saved`, `test_pizza_does_not_exist` |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short | `test_base_choice_is_saved`, `test_rating_without_token_is_refused`, `test_rating_with_wrong_token_is_refused` |

### Test Coverage

Base Choice Coverage uses 9 tests:
- 1 base test
- 2 additional tests for C1
- 3 additional tests for C2
- 1 additional test for C3
- 2 additional tests for C4

All Combinations Coverage would require 72 tests (3 × 4 × 2 × 3).

## Test Files

- `test_names.py` — Tests pizza names.
- `test_tools.py` — Tests available pizza tools.
- `test_pizza.py` — Tests pizza creation and authentication.
- `test_users.py` — Tests new user ratings.
- `test_ratings.py` — Tests creating, reading, updating and deleting ratings.
- `test_refused.py` — Tests invalid user registration and login.
- `test_excluded_tools.py` — Tests excluded tools and the known defect.
- `test_create_rating.py` — Tests rating input partitions.
- `test_update_rating.py` — Tests rating update boundary values.
- `test_rating_owner.py` — Tests rating ownership and access control.

## Notes

- Tests use separate users and sessions to isolate test data.
- The test suite includes an expected failure (`xfail`) for the known defect when all pizza tools are excluded.
- Do not use the public token to create, update or delete data.