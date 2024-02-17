import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

# Define some reflections (pronouns)
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define some patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about you ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.",]
    ],
    [
        r"(.*) (hungry|sleepy|groggy)",
        ["I can understand. What can I assist you with to make you feel better?",]
    ],
    [
        r"(.*) your name ?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to help you. Please feel free to ask me anything.",]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by OpenAI using Python's NLTK library.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem. Feel free to ask if you have any more questions.",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!", "It was nice talking to you. Goodbye!"]
    ],
]

# Create a Chatbot with the defined patterns and reflections
def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Invoke the chatbot function
if __name__ == "__main__":
    chatbot()
