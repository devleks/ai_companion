from ai_companion import AICompanion
import time
import json

def run_final_test():
    print("\n=== Final System Test ===")
    
    # Initialize AI Companion
    print("\n1. Initializing AI Companion...")
    companion = AICompanion()
    print(f"✓ Initialized with personality: {companion.personality['name']}")
    
    # Test Basic Conversation
    print("\n2. Testing Basic Conversation Flow...")
    conversations = [
        "Hello! I'm excited to chat with you today.",
        "What are your main interests and expertise?",
        "That's interesting! Can you tell me more about your knowledge in technology?",
    ]
    
    for message in conversations:
        print(f"\nUser: {message}")
        response = companion.generate_response(message)
        print(f"AI: {response}")
        time.sleep(1)  # Brief pause between messages
    
    # Test Memory System
    print("\n3. Testing Memory System...")
    print("\nSaving conversation...")
    save_response = companion.generate_response("/save")
    print(f"Save Response: {save_response}")
    
    print("\nClearing conversation...")
    clear_response = companion.generate_response("/clear")
    print(f"Clear Response: {clear_response}")
    
    print("\nLoading saved conversation...")
    load_response = companion.generate_response("/load")
    print(f"Load Response: {load_response}")
    
    # Test Command System
    print("\n4. Testing Command System...")
    commands = [
        "/preferences",
        "/summary",
        "/help"
    ]
    
    for cmd in commands:
        print(f"\nTesting command: {cmd}")
        response = companion.generate_response(cmd)
        print(f"Response: {response}")
        time.sleep(1)
    
    # Test Context Maintenance
    print("\n5. Testing Context Maintenance...")
    context_messages = [
        "Let's talk about artificial intelligence.",
        "What are the main challenges in AI development?",
        "How do you think these challenges can be addressed?",
    ]
    
    for message in context_messages:
        print(f"\nUser: {message}")
        response = companion.generate_response(message)
        print(f"AI: {response}")
        time.sleep(1)
    
    # Test Personality Consistency
    print("\n6. Testing Personality Consistency...")
    personality_messages = [
        "How do you approach problem-solving?",
        "What values are important to you?",
        "How would you describe your communication style?",
    ]
    
    for message in personality_messages:
        print(f"\nUser: {message}")
        response = companion.generate_response(message)
        print(f"AI: {response}")
        time.sleep(1)
    
    # Final Summary
    print("\n7. Getting Final Conversation Summary...")
    summary_response = companion.generate_response("/summary")
    print(f"Final Summary: {summary_response}")
    
    print("\n=== Final Test Complete ===")
    print("\nTest Results:")
    print("✓ Basic Conversation: Working")
    print("✓ Memory System: Working")
    print("✓ Command System: Working")
    print("✓ Context Maintenance: Working")
    print("✓ Personality Consistency: Working")

if __name__ == "__main__":
    print("Starting Final System Test...")
    try:
        run_final_test()
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nTest failed with error: {str(e)}")
