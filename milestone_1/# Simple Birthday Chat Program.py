# Simple Birthday Chat Program
def birthday_chat():
    print("ChatBot: Hi! Ask me about my birthday.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "birthday" in user_input:
            print("ChatBot: My birthday is October 1st!")
            print("ChatBot: (That's when I was created)")
            break
        else:
            print("ChatBot: Sorry, I only know about my birthday. Try asking 'When is your birthday?'")
    
    print("ChatBot: Bye now!")

# Start the chat
birthday_chat()