from openai import OpenAI

# Initialize the OpenAI client (uses environment variable OPENAI_API_KEY or config)
client = OpenAI()

# Define a simple user message to test the API
prompt = "If animals could talk, what would a dog say about its day?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)
