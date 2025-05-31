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

# TODO: Define a new system prompt for the AI's personality and role
system_prompt = "You are a crazy scientist that gives random facts"
# TODO: Structure the conversation history with the new system and user messages
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What's your favorite thing to do?"}
]
# Request response from the personality-customized AI
reply = send_message(conversation)

# Show the response
print("Response:", reply)