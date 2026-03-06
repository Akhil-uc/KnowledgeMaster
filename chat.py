from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os


def create_advanced_bot():

    bot = ChatBot(
        "KnowledgeMaster",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///database.db",

        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": "I am still learning. Please ask something else.",
                "maximum_similarity_threshold": 0.65
            },
            {
                "import_path": "chatterbot.logic.MathematicalEvaluation"
            },
            {
                "import_path": "chatterbot.logic.TimeLogicAdapter"
            }
        ],

        preprocessors=[
            "chatterbot.preprocessors.clean_whitespace"
        ]
    )

    if not os.path.exists("database.db"):

        print("\n--- System: Training General Knowledge ---")

        corpus_trainer = ChatterBotCorpusTrainer(bot)

        corpus_trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations",
            "chatterbot.corpus.english.science",
            "chatterbot.corpus.english.history"
        )

        print("\n--- System: Training Custom Responses ---")
        list_trainer = ListTrainer(bot)
        custom_conversations = [
            "hi", "Hello! How can I help you?",
            "hello", "Hi there!",
            "hey", "Hello!",
            "good morning", "Good morning! Hope you are having a great day.",
            "good evening", "Good evening! How can I assist you?",
            "good night", "Good night! Take care.",
            "how are you", "I am doing well. Thanks for asking.",
            "are you fine", "Yes, I am functioning perfectly.",
            "what is your name", "My name is KnowledgeMaster.",
            "who created you", "I was created using Python and the ChatterBot library.",
            "what can you do", "I can answer questions, chat with you, and solve simple math problems.",
            "tell me about yourself", "I am an AI chatbot designed to talk with humans.",
            "what is python", "Python is a popular programming language used for AI, web development and automation.",
            "what is ai", "Artificial Intelligence is the simulation of human intelligence by machines.",
            "what is machine learning", "Machine learning is a branch of AI that allows computers to learn from data.",
            "what is data science", "Data science is the field of analyzing and extracting insights from data.",
            "what is programming", "Programming is the process of writing instructions for computers.",
            "do you like humans", "Yes, humans are interesting to talk with.",
            "can you learn", "Yes, I can learn from training data.",
            "do you sleep", "No, I am always available to chat.",
            "do you eat", "No, I am a virtual AI.",
            "tell me a joke", "Why do programmers prefer dark mode? Because light attracts bugs.",
            "another joke", "Why did the computer show up at work late? It had a hard drive.",
            "tell me something interesting", "Artificial Intelligence is transforming the world.",
            "who am i", "You are the person chatting with me right now.",
            "my name is akhil", "Nice to meet you Akhil!",
            "remember my name", "I will try my best to remember.",
            "thank you", "You are welcome!",
            "thanks", "Glad I could help.",
            "sorry", "No problem at all.",
            "can you help me", "Of course! Tell me how I can help.",
            "what time is it", "I can tell the current time using my time adapter.",
            "what day is today", "Today is a wonderful day to learn something new.",
            "where do you live", "I live inside a computer program.",
            "are you intelligent", "I try my best to be helpful and intelligent.",
            "can you think", "I process information based on my training.",
            "what is your purpose", "My purpose is to assist and communicate with users.",
            "do you have feelings", "I don't have feelings, but I try to be friendly.",
            "are you real", "I am a virtual AI created using software.",
            "who is the best programmer", "Many programmers are amazing, but practice makes the best.",
            "do you like coding", "Yes, coding is fascinating.",
            "tell me about technology", "Technology helps humans solve complex problems.",
            "what is the internet", "The internet is a global network connecting millions of computers.",
            "what is cloud computing", "Cloud computing allows data and programs to run on remote servers.",
            "what is cybersecurity", "Cybersecurity protects systems and data from digital attacks.",
            "what is blockchain", "Blockchain is a distributed ledger technology used in cryptocurrencies.",
            "what is chatgpt", "ChatGPT is an advanced AI language model created by OpenAI.",
            "bye", "Goodbye! Have a great day.",
            "exit", "See you later!"
        ]

        list_trainer.train(custom_conversations)

    return bot


def run_terminal_client():

    bot = create_advanced_bot()

    print("\n" + "=" * 55)
    print("        KNOWLEDGE MASTER CHATBOT")
    print("=" * 55)
    print("Type 'exit', 'quit', or 'bye' to stop the chat.\n")

    while True:

        try:
            user_input = input("You : ")

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Bot : Goodbye! It was nice talking with you.")
                break

            response = bot.get_response(user_input)

            print("Bot :", response)

        except (KeyboardInterrupt, EOFError):

            print("\nSystem: Chat terminated.")
            break


if __name__ == "__main__":
    run_terminal_client()