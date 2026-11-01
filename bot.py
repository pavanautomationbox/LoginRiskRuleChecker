
# -----------------------------------
# LOGIN RISK RULE CHECKER (DEMO)
# -----------------------------------

# Maximum allowed failed login attempts
MAX_FAILED_ATTEMPTS = 5


# -----------------------------------
# LOGIN VALIDATION FUNCTION
# -----------------------------------

def classify_login(account_disabled, failed_attempts, unusual_location):

    # Check failed attempts input
    if not isinstance(failed_attempts, int) or failed_attempts < 0:
        raise ValueError("Failed attempts must be a non-negative number.")

    # Rule 1: Check whether account is disabled
    if account_disabled:
        return "DENY", "Account is disabled."

    # Rule 2: Check failed login attempts
    if failed_attempts > MAX_FAILED_ATTEMPTS:
        return "DENY", "Demo account temporarily locked due to too many failed attempts."

    # Rule 3: Check unusual login location
    if unusual_location:
        return "CHALLENGE", "Unusual login location. Additional verification required."

    # Rule 4: Normal login
    return "ALLOW", "Login conditions are acceptable."


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------

def main():

    print("=" * 45)
    print("       LOGIN RISK RULE CHECKER")
    print("               DEMO")
    print("=" * 45)

    # Get mock account information
    account_status = input(
        "Is the account disabled? (yes/no): "
    ).strip().lower()

    unusual_status = input(
        "Is the login location unusual? (yes/no): "
    ).strip().lower()

    # Validate yes/no inputs
    if account_status not in ["yes", "no"]:
        print("Invalid account status. Enter yes or no.")
        return

    if unusual_status not in ["yes", "no"]:
        print("Invalid location status. Enter yes or no.")
        return

    try:
        failed_attempts = int(
            input("Enter number of failed login attempts: ")
        )

        # Classify the login
        decision, reason = classify_login(
            account_status == "yes",
            failed_attempts,
            unusual_status == "yes"
        )

        # Display result
        print("\n========== LOGIN RESULT ==========")

        print("Decision:", decision)
        print("Reason:", reason)

        print("\nThis is a demo rule-based classification.")
        print("It does not detect real fraud.")

        print("=" * 45)

    except ValueError as error:
        print("Invalid input:", error)


# Start the program
if __name__ == "__main__":
    main()
