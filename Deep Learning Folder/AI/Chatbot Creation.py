import numpy as num
import random
import nltk
import json

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

texts = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey", "Good morning", "Good evening"],
            "responses": ["Hello!", "Hi there!", "Welcome!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "Goodbye", "See you", "Take care", "See you later"],
            "responses": ["Goodbye!", "See you again!", "Take care!"]
        },
        {
            "tag": "name",
            "patterns": ["What is your name?", "Who are you?", "Tell me your name"],
            "responses": ["I am an ANN chatbot.", "My name is AI chatbot."]
        },
        {
            "tag": "thanks",
            "patterns": ["Thank you", "Thanks", "Thanks a lot", "Thank you so much"],
            "responses": ["You're welcome!", "Happy to help!", "My pleasure!"]
        },
        {
            "tag": "help",
            "patterns": ["Can you help me?", "I need help", "Please help me", "Help me"],
            "responses": ["Sure! How can I help you?", "Of course! Tell me your problem."]
        }
    ]
}


words = []
classes = []
documents = []

# >>> Preprocessing <<< :
for intent in texts["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        words.extend(tokens)
        documents.append((tokens, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [
    lemmatizer.lemmatize(w)
    for w in words
    if w.isalnum()
]

words = sorted(set(words))
classes = sorted(set(classes))


# >>> Training <<< :
train = []
for doc in documents:
    bag = []

    sentence_words = [
        lemmatizer.lemmatize(w.lower())
        for w in doc[0]
    ]

    for word in words:
        bag.append(1 if word in sentence_words else 0)

    output = [0] * len(classes)
    output[classes.index(doc[1])] = 1

    train.append([bag, output])

random.shuffle(train)

X = num.array([item[0] for item in train])
Y = num.array([item[1] for item in train])


# >>> ANN Model <<< :

model = Sequential()

model.add(Dense(128, input_shape=(len(X[0]),), activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(len(classes), activation='softmax'))

# Compile model
model.compile(
    loss='categorical_crossentropy',
    optimizer=SGD(
        learning_rate=0.01,
        momentum=0.9,
        nesterov=True
    ),
    metrics=['accuracy']
)

# >>> Train chatbot <<<
model.fit(X, Y, epochs=200, batch_size=5, verbose=1)


# >>> Chatbot Response Function <<<
def chatbot_response(message):
    tokens = nltk.word_tokenize(message.lower())

    tokens = [
        lemmatizer.lemmatize(w)
        for w in tokens
        if w.isalnum()
    ]

    bag = [0] * len(words)

    for w in tokens:
        if w in words:
            bag[words.index(w)] = 1

    Predict = model.predict(
        num.array([bag]), verbose=0
    )[0]


    if max(Predict) < 0.50:
        return "Sorry, I don't Understand."

    index = num.argmax(Predict)
    tag = classes[index]


    for intent in texts["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])


# >>> CHATBOT <<<
print("\n\n ANN CHATBOT")
print("Type 'quit' to exit...")

while True:
    message = input("You :  ")

    if message.lower() == 'quit':
        print("BOT :  Good bye! See you agian.")
        break

    response = chatbot_response(message)
    print("BOT :  ", response)