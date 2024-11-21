from ai_companion import AICompanion
import time

def test_ai_companion():
    # Create AI Companion instance
    companion = AICompanion()
    
    print("\n=== Testing Basic Conversation ===")
    
    # Test 1: Basic greeting
    print("\nTest 1: Basic greeting")
    response = companion.generate_response("Hello! How are you today?")
    print(f"AI: {response}")
    
    # Test 2: Follow-up question
    print("\nTest 2: Follow-up question")
    response = companion.generate_response("What are your main interests?")
    print(f"AI: {response}")
    
    print("\n=== Testing Commands ===")
    
    # Test 3: Preferences command
    print("\nTest 3: Preferences command")
    response = companion.generate_response("/preferences")
    print(f"AI: {response}")
    
    # Test 4: Save conversation
    print("\nTest 4: Save conversation")
    response = companion.generate_response("/save")
    print(f"AI: {response}")
    
    # Test 5: Clear conversation
    print("\nTest 5: Clear conversation")
    response = companion.generate_response("/clear")
    print(f"AI: {response}")
    
    # Test 6: Load conversation
    print("\nTest 6: Load conversation")
    response = companion.generate_response("/load")
    print(f"AI: {response}")
    
    print("\n=== Testing Memory and Context ===")
    
    # Test 7: Start a topic
    print("\nTest 7: Start a topic")
    response = companion.generate_response("Let's talk about artificial intelligence. What do you think about its future?")
    print(f"AI: {response}")
    
    # Test 8: Follow-up on topic
    print("\nTest 8: Follow-up on topic")
    response = companion.generate_response("How might AI impact jobs in the next decade?")
    print(f"AI: {response}")
    
    # Test 9: Get conversation summary
    print("\nTest 9: Get conversation summary")
    response = companion.generate_response("/summary")
    print(f"AI: {response}")

if __name__ == "__main__":
    print("Starting AI Companion Tests...")
    test_ai_companion()
    print("\nTests completed!")
