from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with specific parameters
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=100,
    temperature=1.7  # TODO: Set the temperature to 1.7
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)