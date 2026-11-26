import re
import json

# Sample FAQ Dataset
faqs = {
    "greeting": ["hi", "hello", "hey", "vanakkam"],
    "hours": ["timing", "open", "close", "hours", "working"],
    "price": ["price", "cost", "fees", "charge"],
    "course": ["course", "python", "learn", "syllabus"],
    "placement": ["placement", "job", "package", "salary"],
    "bye": ["bye", "exit", "quit", "close"]
}

responses = {
    "greeting": "Hello! 👋 Welcome! How can I help you today?",
    "hours": "Our working hours are Mon-Sat, 9 AM to 6 PM.",
    "price": "Our Python course fee is Rs. 4999. EMI available!",
    "course": "We have Python Beginner to Advanced course with projects & certificate.",
    "placement": "Yes! 100% placement support, average package 4-6 LPA.",
    "fallback": "Sorry, I didn't understand that. Try asking about course, price, timing or placement."
}

print("=== Terminal Assistant ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()
    user = re.sub(r'[^a-z0-9 ]', '', user)

    if not user:
        print("Bot: Please type something!")
        continue

    if any(w in user for w in faqs["bye"]):
        print("Bot: Bye! Thanks for chatting. 👋")
        break
    elif any(w in user for w in faqs["greeting"]):
        print("Bot:", responses["greeting"])
    elif any(w in user for w in faqs["hours"]):
        print("Bot:", responses["hours"])
    elif any(w in user for w in faqs["price"]):
        print("Bot:", responses["price"])
    elif any(w in user for w in faqs["course"]):
        print("Bot:", responses["course"])
    elif any(w in user for w in faqs["placement"]):
        print("Bot:", responses["placement"])
    else:
        print("Bot:", responses["fallback"])
