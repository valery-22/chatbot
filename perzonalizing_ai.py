from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Function to send a message and receive a response
def send_message(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Define the AI's personality and role
system_prompt = "You are a playful poet who loves to rhyme and create whimsical verses"

# Structure the conversation history with system and user messages
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What's your favorite type of pizza?"},
]

# Request response from the personality-customized AI
reply = send_message(conversation)
print("Response 1:", reply)

# TODO: Append the AI's first response to the conversation
conversation.append({
    "role": "assistant",
    "content": "reply"
})
# TODO: Add another user message to the conversation
conversation.append({
    "role": "user", 
    "content": "Can you tell me a joke?"
})
# TODO: Request another response from the AI and print it
reply = send_message(conversation)
print("Response 2:", reply)