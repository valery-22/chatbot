# Dictionary to store chat sessions
chat_sessions = {}

# Import and initialize the OpenAI client
from openai import OpenAI
client = OpenAI()

def send_message(chat_id, user_message):
    #Verify chat session exists
    if chat_id not in chat_sessions:
        raise ValueError("Chat session not found!")
    #Add user's message to history 
    chat_sessions[chat_id].append({"role": "user", "content": user_message})
    #Get Ai response using conversation history
    response = client.chat.completions.create(
        model="gpt-4",
        messages=chat_sessions[chat_id]

    )
    #Extract and clean AI's response
    answer = response.choices[0].message.content.strip()

    #Add AI's response to history 
    chat_sessions[chat_id].append({"role": "assistant","content":answer})
    # return AI's response
    return answer