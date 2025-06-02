import uuid

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# TODO: Create a new function to generate a unique chat session
    # TODO: Generate a unique session identifier using UUID
    # TODO: Initialize an empty conversation list in chat_sessions using the chat_id
    # TODO: Add the system prompt to the conversation history
    # TODO: Return the unique identifier
def create_chat_session():
    chat_id = str(uuid.uuid4())
    chat_sessions[chat_id] = []
    chat_sessions[chat_id].append(system_prompt)
    return chat_id

# TODO: Create a new chat session using the function and print its ID and history
new_chat_id = create_chat_session()
print(f"New chat sesison ID: {new_chat_id}")
print("Chat history:")
for message in chat_sessions[new_chat_id]:
    print(message)