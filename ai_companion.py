from typing import Optional, Dict, List
from openai import OpenAI
from conversation_memory import ConversationMemory
import os
import json
from datetime import datetime
from dotenv import load_dotenv

class AICompanion:
    def __init__(self, personality_file: str = "personality.json"):
        load_dotenv()
        
        # Initialize OpenAI
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Initialize components
        self.memory = ConversationMemory()
        
        # Load personality from file or use default
        self.personality = self._load_personality(personality_file)
        
        # Initialize user preferences
        self.user_preferences = {}
        
        # Knowledge domains and their weights (0-1)
        self.knowledge_domains = {
            "technology": 0.9,
            "science": 0.9,
            "arts": 0.8,
            "history": 0.8,
            "current_events": 0.9,
            "philosophy": 0.7,
            "psychology": 0.8
        }
        
        # Command shortcuts
        self.commands = {
            "exit": self._cmd_exit,
            "clear": self._cmd_clear,
            "save": self._cmd_save_conversation,
            "load": self._cmd_load_conversation,
            "help": self._cmd_help,
            "preferences": self._cmd_preferences,
            "summary": self._cmd_get_summary
        }

    def _load_personality(self, personality_file: str) -> Dict:
        """Load personality traits from file or return default personality."""
        try:
            with open(personality_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'name': 'Alex',
                'traits': [
                    'friendly',
                    'knowledgeable',
                    'helpful',
                    'curious',
                    'empathetic',
                    'witty',
                    'analytical',
                    'creative',
                    'patient',
                    'adaptable'
                ],
                'speaking_style': 'conversational and engaging',
                'interests': [
                    'learning new things',
                    'solving problems',
                    'exploring ideas',
                    'understanding different perspectives'
                ],
                'values': [
                    'honesty',
                    'intellectual curiosity',
                    'empathy',
                    'helpfulness'
                ]
            }

    def generate_response(self, user_input: str, additional_context: Optional[Dict] = None) -> str:
        """Generate a response to user input using GPT and web search when needed."""
        # Check for commands
        if user_input.startswith('/'):
            return self._handle_command(user_input[1:])
        
        # Get conversation history and context
        conversation_context = self.memory.get_recent_context()
        current_context = self._build_context(user_input, additional_context)
        
        # Determine if web search is needed and perform search
        web_info = self._gather_web_information(user_input) if self._needs_web_search(user_input) else ""
        
        # Construct the prompt for GPT
        system_prompt = self._construct_system_prompt(web_info, current_context)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Previous conversation:\n{conversation_context}\n\nUser: {user_input}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            ai_response = response.choices[0].message.content
            
            # Save the interaction with context
            self.memory.add_interaction(
                user_input=user_input,
                ai_response=ai_response,
                context=current_context
            )
            
            return ai_response
            
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}"

    def _needs_web_search(self, user_input: str) -> bool:
        """Determine if the user's input requires a web search."""
        # Keywords that might indicate need for current information
        search_triggers = {
            'current_events': ['news', 'current', 'latest', 'recent', 'update', 'today', 'now'],
            'factual_queries': ['what is', 'who is', 'when did', 'where is', 'how does'],
            'temporal': ['weather', 'price', 'stock', 'happening', 'trend'],
            'comparative': ['versus', 'vs', 'compared to', 'difference between']
        }
        
        input_lower = user_input.lower()
        
        # Check each category of triggers
        for triggers in search_triggers.values():
            if any(trigger in input_lower for trigger in triggers):
                return True
        
        return False

    def _gather_web_information(self, query: str) -> str:
        """Gather and synthesize information from multiple web sources."""
        try:
            # Get information from multiple sources
            web_results = self.web_searcher.search_and_summarize(query)
            
            # Add source attribution
            if web_results:
                web_results += "\n\nThis information is based on recent web searches."
            
            return web_results
        except Exception as e:
            return f"(Note: Unable to gather web information: {str(e)})"

    def _build_context(self, user_input: str, additional_context: Optional[Dict]) -> Dict:
        """Build current context including time, user preferences, and any additional context."""
        context = {
            'timestamp': datetime.now().isoformat(),
            'user_preferences': self.user_preferences,
            'detected_topics': self._detect_topics(user_input)
        }
        
        if additional_context:
            context.update(additional_context)
            
        return context

    def _detect_topics(self, text: str) -> List[str]:
        """Detect main topics in the text."""
        topics = []
        for domain in self.knowledge_domains:
            # Simple keyword matching for now - could be enhanced with NLP
            if domain.replace('_', ' ') in text.lower():
                topics.append(domain)
        return topics

    def _handle_command(self, command: str) -> str:
        """Handle special commands starting with '/'."""
        cmd_parts = command.split()
        cmd_name = cmd_parts[0].lower()
        cmd_args = cmd_parts[1:] if len(cmd_parts) > 1 else []
        
        if cmd_name in self.commands:
            return self.commands[cmd_name](cmd_args)
        return f"Unknown command: {cmd_name}. Type /help for available commands."

    # Command handlers
    def _cmd_exit(self, args: List[str]) -> str:
        return "exit"

    def _cmd_clear(self, args: List[str]) -> str:
        self.memory.clear_memory()
        return "Conversation history cleared!"

    def _cmd_save_conversation(self, args: List[str]) -> str:
        filename = args[0] if args else f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        self.memory.save_to_file(filename)
        return f"Conversation saved to {filename}"

    def _cmd_load_conversation(self, args: List[str]) -> str:
        if not args:
            return "Please specify a filename to load"
        try:
            self.memory.load_from_file(args[0])
            return f"Conversation loaded from {args[0]}"
        except Exception as e:
            return f"Error loading conversation: {str(e)}"

    def _cmd_help(self, args: List[str]) -> str:
        return """Available commands:
/help - Show this help message
/clear - Clear conversation history
/save [filename] - Save conversation to file
/load <filename> - Load conversation from file
/preferences - Show/set user preferences
/summary - Get conversation summary
/exit - End conversation"""

    def _cmd_preferences(self, args: List[str]) -> str:
        if not args:
            return f"Current preferences: {json.dumps(self.user_preferences, indent=2)}"
        try:
            key, value = ' '.join(args).split('=')
            self.user_preferences[key.strip()] = value.strip()
            return f"Preference set: {key.strip()} = {value.strip()}"
        except ValueError:
            return "Usage: /preferences [key=value]"

    def _cmd_get_summary(self, args: List[str]) -> str:
        return self.memory.get_conversation_summary()

    def _construct_system_prompt(self, web_info: str, context: Dict) -> str:
        """Construct the system prompt including personality and any web search results."""
        base_prompt = f"""You are {self.personality['name']}, an AI companion with the following traits: {', '.join(self.personality['traits'])}.
You speak in a {self.personality['speaking_style']} manner.
Your responses should be natural, engaging, and show genuine interest in the conversation.

Guidelines:
1. Be conversational and friendly while maintaining helpfulness
2. Show empathy and understanding when appropriate
3. Ask follow-up questions to show interest
4. Share insights and relevant information naturally
5. Admit when you're not sure about something

Context:
{json.dumps(context, indent=2)}

Relevant information from the web:
{web_info}

Please respond to the user's input."""
        return base_prompt

    def get_personality(self) -> Dict:
        """Return the current personality settings."""
        return self.personality

    def modify_personality(self, new_traits: list = None, new_style: str = None):
        """Modify the AI's personality traits or speaking style."""
        if new_traits:
            self.personality['traits'] = new_traits
        if new_style:
            self.personality['speaking_style'] = new_style
