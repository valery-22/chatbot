# TODO: Instantiate the ChatManager
chat_manager = ChatManager()

# TODO: Define user_id and chat_id variables
# - Set user_id to a test value, e.g., "test_user"
# - Set chat_id to a test value, e.g., "test_chat"
user_id = "test_user1"
chat_id = "test_chat1"

# TODO: Use create_chat method to create a new chat
# - Call the create_chat method on the ChatManager instance
# - Pass user_id, chat_id, and system_prompt as arguments
chat_manager.create_chat(user_id, chat_id, system_prompt)

# TODO: Use get_chat method to check if the chat exists
chat = chat_manager.get_chat(user_id, chat_id)

# - Retrieve the chat using the get_chat method with user_id and chat_id
# - If the chat is found, print "Chat successfully created!"
# - If the chat is not found, print "Failed to create chat."
if chat:
    print("chat successfully created!")
else:
    print("Failed to create chat.")