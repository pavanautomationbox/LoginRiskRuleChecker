
from bot import classify_login


# Test 1: Normal login
def test_valid_login():
    decision, reason = classify_login(False, 0, False)

    assert decision == "ALLOW"
    assert "acceptable" in reason.lower()


# Test 2: Disabled account
def test_disabled_account():
    decision, reason = classify_login(True, 0, False)

    assert decision == "DENY"
    assert "disabled" in reason.lower()


# Test 3: Failed attempts exceed limit
def test_account_lock():
    decision, reason = classify_login(False, 6, False)

    assert decision == "DENY"
    assert "temporarily locked" in reason.lower()


# Test 4: Unusual location
def test_location_challenge():
    decision, reason = classify_login(False, 1, True)

    assert decision == "CHALLENGE"
    assert "verification" in reason.lower()


# Test 5: Failed attempts exactly at limit
def test_attempts_equal_limit():
    decision, reason = classify_login(False, 5, False)

    assert decision == "ALLOW"


# Test 6: Failed attempts above limit
def test_attempts_above_limit():
    decision, reason = classify_login(False, 8, False)

    assert decision == "DENY"


# Test 7: Disabled account with unusual location
def test_disabled_and_unusual_location():
    decision, reason = classify_login(True, 1, True)

    assert decision == "DENY"
    assert "disabled" in reason.lower()


# Test 8: Unusual location with too many attempts
def test_unusual_location_and_many_attempts():
    decision, reason = classify_login(False, 7, True)

    assert decision == "DENY"
    assert "locked" in reason.lower()


# Test 9: Invalid negative attempts
def test_invalid_attempts():
    try:
        classify_login(False, -2, False)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


# Test 10: All reasons should be meaningful
def test_decision_has_reason():
    decision, reason = classify_login(False, 2, True)

    assert decision in ["ALLOW", "CHALLENGE", "DENY"]
    assert len(reason) > 0
