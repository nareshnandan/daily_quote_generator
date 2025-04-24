import random

def get_random_quote():
    quotes = [
        "Believe in yourself and all that you are.",
        "Every day is a second chance.",
        "Your only limit is your mind.",
        "Push yourself, because no one else is going to do it for you.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Small steps every day lead to big results.",
        "Wake up with determination, go to bed with satisfaction."
    ]
    return random.choice(quotes)

print("Today's Quote is: ")
print(get_random_quote())