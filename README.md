# KnowledgeMaster Chatbot (Terminal AI Chatbot)

## Project Overview

KnowledgeMaster Chatbot is a terminal-based conversational chatbot built using **Python** and the **ChatterBot** library. The chatbot uses machine learning and predefined conversational datasets to generate responses based on user input.

The system allows users to interact with the chatbot through a terminal interface where the chatbot can answer general questions, provide simple explanations, solve basic math expressions, and respond with conversational replies.

The chatbot is trained using both **predefined ChatterBot English corpora** and **custom conversation datasets** to improve its ability to respond to common queries.

---

# Features

* Terminal-based conversational chatbot
* Machine learning-based response generation
* Custom conversation training dataset
* General knowledge training using ChatterBot corpus
* Mathematical expression evaluation
* Time-based responses
* Interactive command-line interface
* Persistent learning using SQLite database
* Graceful exit commands

---

# Technologies Used

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| Python            | Core programming language   |
| ChatterBot        | Conversational AI framework |
| ChatterBot Corpus | Pre-built training datasets |
| spaCy             | Natural language processing |
| SQLite            | Local chatbot database      |
| Conda Environment | Dependency management       |

---

# Project Structure

```
AKhilchatbot/
│
├── chat.py
├── database.db
└── README.md
```

| File        | Description                               |
| ----------- | ----------------------------------------- |
| chat.py     | Main chatbot application                  |
| database.db | SQLite database storing chatbot knowledge |
| README.md   | Project documentation                     |

---

# How the Chatbot Works

The chatbot operates using the **ChatterBot framework**, which works on a **machine-learning conversational engine**.

### The chatbot training occurs in two stages:

### 1️⃣ Corpus Training

The chatbot is trained using predefined datasets:

* Greetings
* Conversations
* Science knowledge
* Historical information

These datasets come from the **ChatterBot English corpus**.

### 2️⃣ Custom Training

The chatbot is also trained using manually defined question-answer pairs to improve response accuracy.

Example:

```
User: what is python
Bot: Python is a popular programming language used for AI and web development.
```

---

# System Requirements

* Python **3.10** (recommended)
* Windows / Linux / macOS
* Conda or Python virtual environment
* Internet connection (for installing dependencies)

---

# Installation Guide

## Step 1 — Clone the Repository

```
git clone https://github.com/yourusername/knowledgemaster-chatbot.git
cd knowledgemaster-chatbot
```

---

# Step 2 — Create Conda Environment

```
conda create -n chatbot_env python=3.10
```

Activate the environment:

```
conda activate chatbot_env
```

---

# Step 3 — Install Required Libraries

```
pip install chatterbot chatterbot_corpus
```

---

# Step 4 — Install spaCy Language Model

ChatterBot requires the spaCy English model.

```
python -m spacy download en_core_web_sm
```

---

# Step 5 — Install YAML Dependency

The corpus training requires PyYAML.

```
pip install pyyaml
```

---

# Running the Chatbot

Start the chatbot by running:

```
python chat.py
```

---

# Example Output

```
=======================================================
        KNOWLEDGE MASTER CHATBOT
=======================================================
Type 'exit', 'quit', or 'bye' to stop the chat.

You : hello
Bot : Hi there!

You : how are you
Bot : I am doing well.

You : tell me a joke
Bot : Why do programmers prefer dark mode? Because light attracts bugs.
```

---

# Exit Commands

You can stop the chatbot using any of the following commands:

```
exit
quit
bye
```

---

# Database System

The chatbot stores its learned responses inside an **SQLite database**.

```
database.db
```

This database ensures that the chatbot does not need to retrain every time the program runs.

---

# Troubleshooting

### Problem: spaCy Model Missing

Error message:

```
Can't find model 'en_core_web_sm'
```

Solution:

```
python -m spacy download en_core_web_sm
```

---

### Problem: YAML Module Missing

Error message:

```
No module named 'yaml'
```

Solution:

```
pip install pyyaml
```

---

### Problem: Python Version Error

ChatterBot does not support **Python 3.13 or 3.14**.

Use Python **3.10**.

---

# Limitations

* ChatterBot uses **pattern-based response matching**
* It is not as powerful as modern LLM chatbots
* Some questions may return default responses

---

# Future Improvements

Possible enhancements include:

* Web interface using **Django or Flask**
* Chat memory system
* Integration with **LLM APIs**
* Voice interaction support
* GUI chatbot interface

---

