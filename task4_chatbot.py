# ===== TASK 4: BASIC RULE-BASED CHATBOT =====

def get_reply(message):
    """User ke message ke hisaab se reply return karta hai."""
    message = message.lower().strip()    # lowercase + extra spaces hatao

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "Main ek simple chatbot hoon."
    elif message == "help":
        return "Aap likh sakte hain: hello, how are you, what is your name, bye"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, mujhe samajh nahi aaya. 'help' likh kar dekho."


def main():
    """Main chat loop."""
    print("=== CHATBOT === ('bye' likho exit karne ke liye)")
    while True:                          # chat tab tak chale jab tak user bye na kahe
        user = input("You: ")            # user ka input
        reply = get_reply(user)          # function se reply lo
        print("Bot:", reply)
        if user.lower().strip() == "bye":
            break                        # bye par loop khatam


main()                                   # program start karo
