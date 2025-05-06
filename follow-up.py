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

# Start a conversation history with an initial message
conversation = [
    {"role": "user", "content": "Can you tell me a fun fact about space?"}
]

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)

# TODO: Append the assistant's response to conversation history
conversation.append({
    "role": "assistant",
    "content": "reply"
})
# TODO: Append a follow-up question to conversation history
conversation.append({
    "role": "user",
    "content": "Who studied about this?"
})
# TODO: Call send_message with the updated conversation history and print the response
follow_up_reply = send_message(conversation)
print("Assistant follow-up:", follow_up_reply)