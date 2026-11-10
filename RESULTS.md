# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Mad Siciliana
- Step 0.12, results of the three runs without a session (optional): Run 1 - FAILED (401), Run 2 - FAILED (401), Run 3 - FAILED (401)
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, 3

## Defect report
- Title: API returns 500 when all tools are excluded
- Request: POST /api/pizza with {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: HTTP 400 Bad Request with a JSON error message
- Actual result: HTTP 500 Internal Server Error with an empty response body
- Severity: Medium


## Part A: Input Space Partitioning for Ratings

POST /api/ratings

| Characteristic | Blocks | Values in the tests | Test Cases |
|---|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 | `test_stars_out_of_range[0]`, `test_base_choice_is_saved`, `test_stars_out_of_range[6]` |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field | `test_base_choice_is_saved`, `test_stars_decimal_is_refused`, `test_stars_text_is_refused`, `test_stars_missing_is_refused` |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 | `test_base_choice_is_saved`, `test_pizza_does_not_exist` |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short | `test_base_choice_is_saved`, `test_rating_without_token_is_refused`, `test_rating_with_wrong_token_is_refused` |

## Part A: Step A4, status codes when the other user reads, changes and deletes:
- Read: 404
- Update: 400
- Delete: 400

## Part B: Reflection

**1.** API tests can find integration failures between the client and the real server, and problems with authentication or network communication. Unit tests with stubs cannot detect these because they use simulated responses. Unit tests are still useful because they are faster and test individual functions independently.

**2.** Each test creates a unique user to avoid conflicts and keep test data isolated. In Project 2, I would create separate test accounts and use data owned by each account to prevent tests from interfering with one another.

**3.** Using one session keeps cookies between requests, which helps maintain the same connection context. In Step 0.12, all three runs failed with status code 401 because the requests did not share the session cookies.

**4.** The block where all three tools were excluded revealed the defect. A 500 error with an empty body is worse because the client cannot understand what went wrong. A 400 error with a message explains the problem. The test stays as xfail to document the defect and detect when it is fixed.

**5.** Base Choice Coverage needs 9 tests:
- 1 base test
- (3 - 1) + (4 - 1) + (2 - 1) + (3 - 1) = 8 additional tests
- Total = 1 + 8 = 9 tests

All Combinations Coverage needs 3 × 4 × 2 × 3 = 72 tests.

**6.** The actual status codes were:
- Read: 404
- Update: 400
- Delete: 400

I would expect 403 Forbidden when another user tries to access someone else's rating. A 404 for reading can also be acceptable to hide the resource. The difference is not necessarily a defect because all three requests were refused and the owner's rating remained unchanged.

**7.** The API returned a list of ratings even though I used a made-up token. This is a security defect because anyone could access rating data without proper authentication. On a real system, a stranger could read private user data. I only used the token to read data and did not create or modify anything.

**8.** API tests are better for checking response status codes, data formats and authentication. Web UI tests are needed to check the visual layout, usability and user interactions.