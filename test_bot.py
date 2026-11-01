
import pytest
from bot import classify_login


# Test 1: Normal login should be allowed
def test_normal_login():
    decision, reason = classify_login(False, 2, False)

    assert decision == "ALLOW"


# Test 2: Disabled account should be denied
def test_disabled_account():
    decision, reason = classify_login(True, 1, False)

    assert decision == "DENY"


# Test 3: Too many failed attempts
def test_too_many_attempts():
    decision, reason = classify_login(False, 6, False)

    assert decision == "DENY"


# Test 4: Unusual location should require verification
def test_unusual_location():
    decision, reason = classify_login(False, 2, True)

    assert decision == "CHALLENGE"


# Test 5: Exactly 5 failed attempts should be allowed
def test_attempts_at_limit():
    decision, reason = classify_login(False, 5, False)

    assert decision == "ALLOW"


# Test 6: Zero failed attempts
def test_zero_attempts():
    decision, reason = classify_login(False, 0, False)

    assert decision == "ALLOW"


# Test 7: Disabled account takes priority
def test_disabled_account_priority():
    decision, reason = classify_login(True, 10, True)

    assert decision == "DENY"
    assert "disabled" in reason.lower()


# Test 8: Negative attempts should be rejected
def test_negative_attempts():
    with pytest.raises(ValueError):
        classify_login(False, -1, False)
