# Rule-based Chatbot

A simple rule-based chatbot implemented in Python, designed to respond to specific inputs with predefined answers. This chatbot can be used in applications that require a basic automated response system without the need for machine learning or NLP.

![Screenshot1](https://github.com/user-attachments/assets/caffb979-87c3-4143-b141-2941ac6a3a5f)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Knowledge Base Structure](#knowledge-base-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Customizable rules:** Define custom rules and responses easily.
- **Efficient handling:** Responses are triggered by specific keywords or phrases.
- **Easy to extend:** Add more rules and responses as needed.
- **Python-based:** Lightweight and easily integrable into larger Python applications.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MJTech46/PY-rule-based-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PY-rule-based-chatbot
   ```

## Usage

1. Run the main Python script:
   ```bash
   python main.py
   ```
2. Enter input prompts to interact with the chatbot.

## Knowledge Base Structure

The knowledge base is stored in a JSON file named `knowledge_base.json`, containing a list of questions and answers:

```json
{
  "questions": [
    {
      "question": "Hello",
      "answer": "Hai, How is your day going?"
    },
    {
      "question": "help",
      "answer": "I am a simple chatbot. Ask me something related to my programmed responses."
    },
    {
      "question": "bye",
      "answer": "Goodbye! Have a nice day!"
    }
  ]
}
```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Please ensure any code you submit is well-documented and tested.

## License

This project is licensed under the MIT License.
