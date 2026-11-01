
import bot


# Test 1: Application should not ask for a password
def test_password_not_requested(monkeypatch, capsys):

    inputs = iter(["no", "no", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(inputs)
    )

    bot.main()

    output = capsys.readouterr()

    assert "password" not in output.out.lower()


# Test 2: Application should not create files
def test_no_files_created(monkeypatch, tmp_path):

    monkeypatch.chdir(tmp_path)

    inputs = iter(["no", "no", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(inputs)
    )

    bot.main()

    files = list(tmp_path.iterdir())

    assert files == []


# Test 3: Application should not write logs
def test_no_sensitive_logging(monkeypatch, caplog):

    inputs = iter(["no", "no", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(inputs)
    )

    bot.main()

    assert caplog.text == ""


# Test 4: Negative failed attempts should be rejected
def test_negative_attempts_rejected():

    try:
        bot.classify_login(False, -5, False)
        assert False, "Negative attempts should not be accepted"
    except ValueError:
        assert True


# Test 5: Invalid attempt data should be rejected
def test_invalid_attempt_data():

    try:
        bot.classify_login(False, "five", False)
        assert False, "Invalid attempts should not be accepted"
    except ValueError:
        assert True
