def chatbot():
    print("Customer Support Chatbot")
    print("Type 'exit' to end chat\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I help you today?")

        elif "order" in user_input:
            print("Bot: Please provide your Order ID to check status.")

        elif "refund" in user_input:
            print("Bot: Refunds are processed within 5-7 business days.")

        elif "price" in user_input:
            print("Bot: Please tell me the product name to check the price.")

        elif "complaint" in user_input:
            print("Bot: Sorry for the inconvenience. Please describe your issue.")

        elif "thank" in user_input:
            print("Bot: You're welcome!")

        elif user_input == "exit":
            print("Bot: Thank you for contacting support. Goodbye!")
            break

        else:
            print("Bot: I'm not sure about that. Can you rephrase?")

chatbot()