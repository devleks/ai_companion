# AI Companion

An intelligent AI companion that engages in natural conversations with long-term memory and personality customization. Built using OpenAI's GPT model, it features an advanced conversation memory system and customizable personality traits.

## Features

- 🤖 Natural language conversations using GPT
- 🧠 Long-term memory system for persistent context
- 👤 Customizable AI personality via JSON
- 💬 Comprehensive command system
- 📝 Conversation summarization
- ⚙️ User preferences management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai_companion.git
cd ai_companion
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Docker Setup

### Prerequisites
- Docker installed on your system
- Docker Compose installed on your system

### Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai_companion.git
cd ai_companion
```

2. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

3. Build and start the container:
```bash
docker-compose up -d --build
```

4. Access the container shell:
```bash
docker-compose exec ai_companion bash
```

5. Run the AI Companion inside the container:
```bash
python main.py
```

### Container Management

- Stop the container:
```bash
docker-compose down
```

- View container logs:
```bash
docker-compose logs -f
```

- Restart the container:
```bash
docker-compose restart
```

### Development with Docker

1. The `./data` directory is mounted to persist conversation history and memory
2. Code changes in your local directory are immediately reflected in the container
3. You can open multiple shell sessions to the same container
4. Use `ctrl + d` or type `exit` to leave the container shell (container keeps running)

### Troubleshooting

If you can't access the shell:

1. Check container status:
```bash
docker-compose ps
```

2. View container logs:
```bash
docker-compose logs ai_companion
```

3. Rebuild if necessary:
```bash
docker-compose up -d --build
```

## Usage

1. Run the AI Companion:
```bash
python main.py
```

2. Available Commands:
- `/save` - Save the current conversation
- `/load` - Load a previous conversation
- `/clear` - Clear conversation history
- `/preferences` - View/update preferences
- `/summary` - Get conversation summary
- `/help` - Show available commands
- Type 'exit' to end conversation

## Customization

### Personality Configuration
Modify `personality.json` to customize the AI's personality:
```json
{
  "name": "Alex",
  "traits": [
    "friendly",
    "knowledgeable",
    "helpful"
  ],
  "speaking_style": "conversational",
  "interests": [
    "technology",
    "science",
    "arts"
  ]
}
```

### Memory System
The AI Companion features two types of memory:
- Short-term (conversation) memory
- Long-term memory for persistent information

## Project Structure

```
ai_companion/
├── ai_companion.py      # Main AI implementation
├── conversation_memory.py# Memory system
├── main.py             # Application entry point
├── personality.json    # Personality configuration
├── requirements.txt    # Project dependencies
└── tests/
    ├── test_companion.py
    ├── test_errors.py
    └── final_test.py
```

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python test_companion.py  # Basic functionality tests
python test_errors.py     # Error handling tests
python final_test.py      # Comprehensive system test
```

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT API
- Contributors and users of this project
