from ai_companion import AICompanion
import os
from dotenv import load_dotenv

def test_error_handling():
    print("\n=== Testing Error Handling ===")
    
    # Test 1: Empty input
    print("\nTest 1: Empty input")
    companion = AICompanion()
    response = companion.generate_response("")
    print(f"Response: {response}")
    
    # Test 2: Very long input
    print("\nTest 2: Very long input")
    long_input = "test " * 1000  # Very long input
    response = companion.generate_response(long_input)
    print(f"Response: {response}")
    
    # Test 3: Invalid command
    print("\nTest 3: Invalid command")
    response = companion.generate_response("/invalidcommand")
    print(f"Response: {response}")
    
    # Test 4: Load non-existent conversation
    print("\nTest 4: Load non-existent conversation")
    response = companion.generate_response("/load nonexistent_file.json")
    print(f"Response: {response}")
    
    # Test 5: Special characters
    print("\nTest 5: Special characters")
    response = companion.generate_response("Hello! 🌟 @#$%^&*")
    print(f"Response: {response}")
    
    # Test 6: Missing personality file
    print("\nTest 6: Missing personality file")
    companion_no_personality = AICompanion(personality_file="nonexistent.json")
    response = companion_no_personality.generate_response("Hello!")
    print(f"Response: {response}")
    
    print("\nError handling tests completed!")

if __name__ == "__main__":
    print("Starting Error Handling Tests...")
    test_error_handling()
