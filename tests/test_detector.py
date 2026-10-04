from backend.detector import detect_scam, get_warning

def test_red_message():
    risk, reasons = detect_scam("Your account is blocked. Share your OTP.")
    assert risk == "RED"

def test_orange_message():
    risk, reasons = detect_scam("Urgent! Click here to claim your prize.")
    assert risk == "ORANGE"

def test_green_message():
    risk, reasons = detect_scam("Hello, how are you?")
    assert risk == "GREEN"

def test_capital_letters():
    risk, reasons = detect_scam("URGENT! CLICK HERE to claim your PRIZE.")
    assert risk == "ORANGE"

def test_multiple_red_flags():
    risk, reasons = detect_scam(
        "Share your OTP and verify your bank details."
    )
    assert risk == "RED"
    assert "share your otp" in reasons
    assert "verify your bank" in reasons

def test_no_false_warning():
    risk, reasons = detect_scam("Good morning! Have a nice day.")
    assert risk == "GREEN"
    assert reasons == []

def test_red_warning():
    assert "Danger!" in get_warning("RED")

def test_orange_warning():
    assert "Caution!" in get_warning("ORANGE")

def test_green_warning():
    assert "No known warning signs" in get_warning("GREEN")  

def test_multiple_orange_flags():
    risk, reasons = detect_scam(
        "Urgent! Click here for a limited time prize."
    )
    assert risk == "ORANGE"
    assert "urgent" in reasons
    assert "click here" in reasons
    assert "limited time" in reasons      

def test_hindi_otp_scam():
    risk, reasons = detect_scam(
        "Apna OTP share karein"
    )
    assert risk == "RED"
    assert "apna otp share karein" in reasons


def test_hinglish_account_block():
    risk, reasons = detect_scam(
        "Aapka account block ho gaya"
    )
    assert risk == "RED"
    assert "aapka account block ho gaya" in reasons


def test_hindi_lottery_scam():
    risk, reasons = detect_scam(
        "Aapne lottery jeeti hai"
    )
    assert risk == "ORANGE"
    assert "aapne lottery jeeti hai" in reasons


def test_hinglish_normal_message():
    risk, reasons = detect_scam(
        "Kal milte hain, shaam ko 6 baje."
    )
    assert risk == "GREEN"
    assert reasons == []