import uuid
from openai import OpenAI

#Initialize the OpenAI client
client = OpenAI()

#Store all active chat sessions
chat_sessions = {}

#Define a common system for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assite customers."
}

#create a new chat session with a unique identifier
def create_chat():
    chat_id = str(uuid.uuid4()) #Create unique identifier
    chat_sessions[chat_id] = [] #initialize empty conversation history
    chat_sessions[chat_id].append(system_prompt) #Add systems propmt to cinversation histoty
    return chat_id