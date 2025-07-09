import openai


def chatbot_response(user_input):

    user_input = user_input.lower()
    

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today? my name uis new chatbot"
    elif "how are you" in user_input:
        return "I'm your friend!, so I'm always good! How about you?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot, here to help you with anything you need."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "explain about api" in user_input:
        return "API is application programming interface."
    elif "what is ai" in user_input:
        return "AI stands for artificial intelligence .it is basically of two types ."
    elif "introduce yourself" in user_input:
        return "chatbot"
    else:
        return "I'm sorry, I don't understand that. Can you please ask something else?"


def main():
    print("Welcome to the Simple Chatbot!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
