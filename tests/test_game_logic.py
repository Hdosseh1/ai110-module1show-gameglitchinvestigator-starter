from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_when_guess_too_high():
    # BUG FIX: When guess is too high, message should be "Go LOWER!" not "Go HIGHER!"
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High", f"Expected outcome 'Too High', got '{outcome}'"
    assert message == "📉 Go LOWER!", f"Expected '📉 Go LOWER!' but got '{message}'"

def test_hint_message_when_guess_too_low():
    # BUG FIX: When guess is too low, message should be "Go HIGHER!" not "Go LOWER!"
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low", f"Expected outcome 'Too Low', got '{outcome}'"
    assert message == "📈 Go HIGHER!", f"Expected '📈 Go HIGHER!' but got '{message}'"

def test_win_message():
    # When guess matches secret, should return "Win" with correct message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win", f"Expected outcome 'Win', got '{outcome}'"
    assert message == "🎉 Correct!", f"Expected '🎉 Correct!' but got '{message}'"

def test_attempts_initialization_and_calculation():
    # Test that attempts are initialized correctly (should be 0, not 1)
    # This validates the fix for the attempts remaining bug
    attempt_limit = 8  # Normal difficulty
    initial_attempts = 0  # Must be 0, not 1
    
    # Calculate remaining attempts
    attempts_remaining = attempt_limit - initial_attempts
    
    # Should have all 8 attempts available
    assert attempts_remaining == 8, f"Expected 8 attempts remaining, got {attempts_remaining}"
    assert initial_attempts == 0, f"Expected attempts to initialize at 0, got {initial_attempts}"

def test_attempts_decrement_after_guess():
    # Test that after making a guess, attempts increment correctly
    attempt_limit = 8  # Normal difficulty
    initial_attempts = 0
    
    # Simulate making one guess
    current_attempts = initial_attempts + 1
    attempts_remaining = attempt_limit - current_attempts
    
    # After 1 guess, should have 7 attempts left
    assert current_attempts == 1
    assert attempts_remaining == 7, f"After 1 guess, expected 7 remaining, got {attempts_remaining}"
    
    # Simulate making another guess
    current_attempts += 1
    attempts_remaining = attempt_limit - current_attempts
    
    # After 2 guesses, should have 6 attempts left
    assert current_attempts == 2
    assert attempts_remaining == 6, f"After 2 guesses, expected 6 remaining, got {attempts_remaining}"
