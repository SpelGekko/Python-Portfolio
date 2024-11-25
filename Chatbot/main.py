## Made by Gekko

import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Gekko.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I want to help you with your queries.",]
    ],
    [
        r"(.*) created?",
        ["I was created by Gekko.", "Gekko created me using Python's NLTK library.",]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm in the cloud, I don't have a physical location.",]
    ],
    [
        r"how (.*) weather?",
        ["I don't have access to weather information, but you can check online.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day.",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
def chatbot_interface():
    print("Hi, I'm a chatbot created by Gekko. How can I help you today?")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    chatbot_interface()