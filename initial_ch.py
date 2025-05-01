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

# TODO: Pass the conversation to send_message and store the response in a variable
reply = send_message(conversation)
# TODO: Print the assistant's response
print("Assiatant:",reply)