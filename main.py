from ai_companion import AICompanion
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'sk-your-openai-api-key-here':
        print("\nError: Please set your OpenAI API key in the .env file.")
        print("1. Open the .env file")
        print("2. Replace 'sk-your-openai-api-key-here' with your actual OpenAI API key")
        print("3. Save the file and try again")
        return
    
    try:
        # Create AI Companion instance
        companion = AICompanion()
        
        print(f"\nAI Companion {companion.personality['name']} is ready to chat!")
        print("Type 'exit' to end the conversation.")
        print("Type 'clear' to clear conversation history.")
        print("-" * 50)

        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for exit command
                if user_input.lower() == 'exit':
                    print("\nGoodbye! Have a great day!")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    companion.memory.clear_memory()
                    print("\nConversation history cleared!")
                    continue
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Generate and print AI response
                response = companion.generate_response(user_input)
                print(f"\n{companion.personality['name']}: {response}")
                
            except EOFError:
                print("\nDetected EOF error. Press Ctrl+C to exit.")
                break
            except KeyboardInterrupt:
                print("\n\nGoodbye! Have a great day!")
                break
            except Exception as e:
                print(f"\nAn error occurred: {str(e)}")
                print("Please try again or type 'exit' to quit.")
    
    except Exception as e:
        print(f"\nFailed to initialize AI Companion: {str(e)}")
        print("Please check your API keys and try again.")

if __name__ == "__main__":
    main()
