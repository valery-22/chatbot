import openai
import os

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Define a simple user message to test the API 
prompt = "Hi, can you tell me a tip for a junior dev?"

# Create a chat completion request to get the AI response 
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

# Extract the AI's response
reply = response.choices[0].message["content"].strip()

# Show both sides of the conversation
print("prompt:", prompt)
print("response:", reply)
