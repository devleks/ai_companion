from typing import List, Dict, Optional
import json
from datetime import datetime
from collections import deque
import os

class ConversationMemory:
    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.conversations = deque(maxlen=max_history)
        self.long_term_memory = []
        self.memory_file = "long_term_memory.json"
        self._load_long_term_memory()

    def add_interaction(self, user_input: str, ai_response: str, context: Optional[Dict] = None):
        """Add a new interaction to the conversation history."""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'user_input': user_input,
            'ai_response': ai_response,
            'context': context or {}
        }
        
        self.conversations.append(interaction)
        
        # If this seems like an important interaction, save to long-term memory
        if self._is_important_interaction(interaction):
            self._add_to_long_term_memory(interaction)

    def get_recent_context(self, num_messages: int = 5) -> str:
        """Get the most recent conversation context."""
        recent = list(self.conversations)[-num_messages:]
        context_str = ""
        
        for interaction in recent:
            context_str += f"User: {interaction['user_input']}\n"
            context_str += f"AI: {interaction['ai_response']}\n"
        
        return context_str

    def get_conversation_summary(self) -> str:
        """Generate a summary of the current conversation."""
        if not self.conversations:
            return "No conversation history available."
        
        summary = "Conversation Summary:\n\n"
        
        # Add basic statistics
        summary += f"Total messages: {len(self.conversations)}\n"
        if self.conversations:
            start_time = datetime.fromisoformat(self.conversations[0]['timestamp'])
            end_time = datetime.fromisoformat(self.conversations[-1]['timestamp'])
            duration = end_time - start_time
            summary += f"Duration: {duration}\n\n"
        
        # Add key topics discussed
        topics = self._extract_topics()
        if topics:
            summary += "Main topics discussed:\n"
            for topic in topics:
                summary += f"- {topic}\n"
        
        return summary

    def clear_memory(self):
        """Clear the conversation history."""
        self.conversations.clear()

    def save_to_file(self, filename: str):
        """Save the current conversation to a file."""
        data = {
            'timestamp': datetime.now().isoformat(),
            'conversations': list(self.conversations)
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str):
        """Load a conversation from a file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.conversations = deque(data['conversations'], maxlen=self.max_history)

    def _is_important_interaction(self, interaction: Dict) -> bool:
        """Determine if an interaction should be saved to long-term memory."""
        important_keywords = [
            'remember', 'important', 'don\'t forget', 'note',
            'preference', 'always', 'never', 'favorite'
        ]
        
        text = f"{interaction['user_input']} {interaction['ai_response']}".lower()
        return any(keyword in text for keyword in important_keywords)

    def _add_to_long_term_memory(self, interaction: Dict):
        """Add an interaction to long-term memory and save to file."""
        self.long_term_memory.append(interaction)
        self._save_long_term_memory()

    def _load_long_term_memory(self):
        """Load long-term memory from file."""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r') as f:
                    self.long_term_memory = json.load(f)
        except Exception as e:
            print(f"Error loading long-term memory: {e}")
            self.long_term_memory = []

    def _save_long_term_memory(self):
        """Save long-term memory to file."""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.long_term_memory, f, indent=2)
        except Exception as e:
            print(f"Error saving long-term memory: {e}")

    def _extract_topics(self) -> List[str]:
        """Extract main topics from the conversation."""
        # This is a simple implementation - could be enhanced with NLP
        topics = set()
        for interaction in self.conversations:
            # Extract topics from context if available
            if 'context' in interaction and 'detected_topics' in interaction['context']:
                topics.update(interaction['context']['detected_topics'])
        return list(topics)

    def get_relevant_memories(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Retrieve relevant memories based on a query.
        This is a simple implementation - could be enhanced with embeddings and semantic search.
        """
        relevant = []
        query_terms = query.lower().split()
        
        for memory in self.long_term_memory:
            relevance_score = 0
            memory_text = f"{memory['user_input']} {memory['ai_response']}".lower()
            
            for term in query_terms:
                if term in memory_text:
                    relevance_score += 1
            
            if relevance_score > 0:
                relevant.append({
                    'memory': memory,
                    'score': relevance_score
                })
        
        # Sort by relevance and return top matches
        relevant.sort(key=lambda x: x['score'], reverse=True)
        return [item['memory'] for item in relevant[:limit]]
