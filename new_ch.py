from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Function to send a message and receive a response
def send_message(user_message):
    
    if not hasattr(send_message, "conversation"):
        send_message.conversation = []
        
    send_message.conversation.append({"role": "user", "content": user_message})    
    
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=send_message.conversation
    )
    
    reply = response.choices[0].message.content.strip()

# Start a conversation history with an initial message
    send_message.conversation.append({"role": "user", "content": reply})
    return reply

reply1 = send_message("What is the main ingridient in guacamole?")
print("Assistant:", reply1)

reply2 = send_message("Can you name popular dish that uses guacamole?")
print("Assistant follow-up", reply2)