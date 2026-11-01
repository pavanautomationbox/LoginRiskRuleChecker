
# Login Risk Rule Checker (Demo)

## 1. Project Description

The Login Risk Rule Checker is a simple Python application that classifies mock login events using predefined security rules.

It checks account status, failed login attempts, and unusual login locations.

Based on these conditions, the application returns one of three decisions:

- ALLOW
- CHALLENGE
- DENY

This is an educational demo. It does not detect real fraud or verify actual user identities.

---

## 2. Project Structure

```text
LoginRiskRuleChecker/
│
├── bot.py
├── test_bot.py
├── test_functional.py
├── test_security.py
└── README.md
```

### File Description

- bot.py: Main Python application.
- test_bot.py: Contains unit test cases.
- test_functional.py: Contains functional test cases.
- test_security.py: Contains security test cases.
- README.md: Project documentation.

---

## 3. Technologies Used

- Python 3
- Pytest
- VS Code

No external Python libraries are required except pytest for testing.

---

## 4. Login Security Rules

The application follows these rules:

1. If the account is disabled, deny login.
2. If failed login attempts exceed 5, deny login and classify the demo account as temporarily locked.
3. If the login location is unusual, request additional verification.
4. If all conditions are normal, allow login.

### Expected Output

ALLOW:
Login conditions are acceptable.

CHALLENGE:
Additional verification is required.

DENY:
Login is rejected because of a security rule.

---

# 5. Unit Testing

## What is Unit Testing?

Unit testing checks individual functions or small parts of a Python application.

In this project, unit testing checks the classify_login() function separately.

## Tool Used

Pytest is used to execute automated unit tests.

## File Used

test_bot.py

## Unit Test Cases

| Test Case | Expected Result |
|---|---|
| Normal login | ALLOW |
| Disabled account | DENY |
| Too many failed attempts | DENY |
| Unusual login location | CHALLENGE |
| Exactly 5 failed attempts | ALLOW |
| Zero failed attempts | ALLOW |
| Disabled account takes priority | DENY |
| Negative failed attempts | ValueError |

## Expected Result

All 8 unit tests should pass.

---

# 6. Functional Testing

## What is Functional Testing?

Functional testing checks whether the application performs its expected functions correctly.

In this project, functional testing verifies whether the correct login decision is returned based on the mock login information.

## Tool Used

Pytest is used for automated functional testing.

## File Used

test_functional.py

## Functional Test Cases

| Test Case | Expected Result |
|---|---|
| Valid login | ALLOW |
| Disabled account | DENY |
| Failed attempts exceed limit | DENY |
| Unusual location | CHALLENGE |
| Failed attempts equal limit | ALLOW |
| Failed attempts above limit | DENY |
| Disabled account with unusual location | DENY |
| Unusual location with too many attempts | DENY |
| Negative failed attempts | ValueError |
| Decision contains a reason | Valid decision and reason |

## Expected Result

All 10 functional tests should pass.

---

# 7. Security Testing

## What is Security Testing?

Security testing checks whether an application follows basic security practices and handles information safely.

In this project, security testing checks that mock login information is not unnecessarily stored or logged.

## Tools and Python Features Used

### 1. monkeypatch

- Temporarily replaces functions during testing.
- Used to simulate user input.
- Helps test the application automatically.

### 2. capsys

- Captures terminal output.
- Used to check that the application does not display password prompts or password information.

### 3. tmp_path

- Creates a temporary directory.
- Used to check whether the application creates unwanted files.

### 4. caplog

- Captures application log messages.
- Used to check that no application logs are generated during the test.

### 5. ValueError

- Handles invalid input.
- Used to reject negative or non-numeric failed login attempts.

## Security Test Cases

| Test Case | Expected Result |
|---|---|
| Password should not be requested | No password prompt |
| Application should not create files | No files created |
| Application should not write logs | No logs generated |
| Negative attempts should be rejected | ValueError |
| Invalid attempt data should be rejected | ValueError |

## Expected Result

All 5 security tests should pass.

The application should not request, store, or log passwords.

---

# 8. Install Pytest

Open the terminal in VS Code.

Run:

pip install pytest

Check installation:

pytest --version

---

# 9. How to Run the Application

Open the project folder in VS Code.

Run:

python bot.py

Enter the mock login information when requested.

---

# 10. How to Run the Tests

### Run all tests

pytest -v

### Run unit tests

pytest -v test_bot.py

### Run functional tests

pytest -v test_functional.py

### Run security tests

pytest -v test_security.py

---

# 11. Expected Testing Summary

| Testing Type | Test Cases | Expected Result |
|---|---:|---|
| Unit Testing | 8 | 8 Passed |
| Functional Testing | 10 | 10 Passed |
| Security Testing | 5 | 5 Passed |
| Total | 23 | 23 Passed |

---

# 12. Project Conclusion

The Login Risk Rule Checker successfully classifies mock login events using predefined security rules.

Unit testing verifies individual login classification rules.

Functional testing verifies that the application returns the correct login decisions.

Security testing checks basic safe handling of mock login information.

Pytest helps automate testing and identify errors.

This project demonstrates basic Python programming, conditional statements, rule-based login classification, and automated software testing.

## Important Limitation

The temporary lock is only a simulated decision. This demo does not implement an actual timed account lock or persistent account status.

The application is not a real fraud detection system.
