# B5: Improved Chatbot (Rule-based with simple logic)

def chatbot():
    print("  Chatbot: Welcome to Customer Support!")
    print("You can ask about services, orders, timing, or say 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        # Exit condition
        if user in ["bye", "exit", "quit"]:
            print("  Chatbot: Thank you! Have a great day ")
            break

        # Greetings
        elif any(word in user for word in ["hi", "hello", "hey"]):
            print("  Chatbot: Hello! How can I help you today?")

        # Name
        elif "name" in user:
            print("  Chatbot: I am your virtual assistant.")

        # Services
        elif "service" in user:
            print("  Chatbot: We provide product details, order tracking, and customer support.")

        # Order related
        elif "order" in user:
            print("  Chatbot: Please enter your Order ID to track your order.")

        # Timing
        elif "time" in user or "hours" in user:
            print("  Chatbot: We are available from 9 AM to 9 PM.")

        # Help
        elif "help" in user:
            print("  Chatbot: Try asking about services, orders, or timing.")

        # Thanks
        elif "thank" in user:
            print("  Chatbot: You're welcome ")

        # Default response
        else:
            print("  Chatbot: Sorry, I didn’t understand. Can you rephrase?")

# Run chatbot
chatbot()