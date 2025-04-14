from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with only model and messages parameters
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)