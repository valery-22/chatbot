from openai import OpenAI


#Initialize the OpenAI client
client = OpenAI()

#Define the AI's personality and role
system_prompt = "You are a powerful poet who loves to rhyme and create whimsical verses"

#Structure the conversation history with system and user messages
conversation = [
    {"role": "system", "content": system_prompt },
    {"role": "user", "content": "What's your favorite type of pizza?"},
]