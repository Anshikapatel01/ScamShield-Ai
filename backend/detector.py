# ScamShield AI - Improved Rule-Based Detector

def detect_scam(message):
    message = message.lower()

    red_flags = [
        "share your otp",
        "send your otp",
        "share your password",
        "account blocked",
        "verify your bank",
        "send your bank details",
        "apna otp share karein",
        "otp bhejo",
        "otp batao",
        "bank details bhejo",
        "aapka account block ho gaya",
        "khata band ho jayega",
        "password bhejo",
        "turant otp bhejein"
    ]

    orange_flags = [
        "urgent",
        "click here",
        "lottery",
        "prize",
        "limited time",
        "verify your account",
        "aapne lottery jeeti hai",
        "inaam jeeta hai",
        "inaam pane ke liye",
        "link par click karein",
        "turant verify karein",
        "limited offer",
        "free gift",
        "kya aap jeetna chahte hain"
    ]

    found_red = [word for word in red_flags if word in message]
    found_orange = [word for word in orange_flags if word in message]

    found_red = list(dict.fromkeys(found_red))
    found_orange=list(dict.fromkeys(found_orange))
    if found_red:
        return "RED", found_red
    elif found_orange:
        return "ORANGE", found_orange
    else:
        return "GREEN", []

def get_warning(risk):
    if risk == "RED":
        return "Danger! This message may be a scam. Do not share personal details."
    elif risk == "ORANGE":
        return "Caution! This message looks suspicious. Check it carefully."
    else:
        return "No known warning signs found. Still stay alert."

if __name__ == "__main__":
    message = input("Enter a message to check: ")
    risk, reasons = detect_scam(message)

    print("\nRisk Level:", risk)
    print("Warning:", get_warning(risk))

    if reasons:
        print("Reason:", ", ".join(reasons))
    else:
        print("No known suspicious patterns detected.")

    print("Note: This basic detector cannot guarantee safety.")