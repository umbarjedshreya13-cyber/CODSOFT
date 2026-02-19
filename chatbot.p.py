import re
from datetime import datetime

def clean_input(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

memory = {
    "last_intent": None
}

def greet():
    memory["last_intent"] = "greeting"
    return "Hello! Nice to talk with you. How can I assist?"

def chatbot_name():
    memory["last_intent"] = "identity"
    return "I am a custom-built rule-based chatbot created for NLP learning."

def tell_time():
    memory["last_intent"] = "time"
    return f"The time is {datetime.now().strftime('%H:%M:%S')}"

def tell_date():
    memory["last_intent"] = "date"
    return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

def help_user():
    return (
        "Try asking things like:\n"
        "- Hello\n"
        "- What is your name?\n"
        "- Time or Date\n"
        "- Help\n"
        "- Bye to exit"
    )

def fallback():
    if memory["last_intent"]:
        return "I'm not sure about that. Maybe try something related to our last topic."
    return "I didn't understand. Type 'help' to see what I can do."

rules = [
    (r"\b(hi|hello|hey)\b", greet),
    (r"\b(name|who are you)\b", chatbot_name),
    (r"\btime\b", tell_time),
    (r"\b(date|day)\b", tell_date),
    (r"\bhelp\b", help_user),
]

exit_pattern = r"\b(bye|exit|quit)\b"

def get_response(user_text):
    for pattern, action in rules:
        if re.search(pattern, user_text):
            return action()
    return fallback()

def run_chatbot():
    print("🤖 Chatbot Started! (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        cleaned = clean_input(user_input)

        if re.search(exit_pattern, cleaned):
            print("🤖 Chatbot: Goodbye! Conversation ended.")
            break

        response = get_response(cleaned)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    run_chatbot()
