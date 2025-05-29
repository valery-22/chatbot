#Create the first chat and send message
chat_id1 = create_chat()

#send the first message and print the response
fisrt message_response = send_message(
    chat_id1,
    "I'm having trouble with my recent order. can you help me track it?"

)
print("Chat 1, First Message:", first_message_response)

#send a folllow- up message ans print the response 
follow_up_response = send_message(
    chat_id1,
    "It was suppose to arrive yesterday but hasnt't, What sould I do next?"
)

print("Chat 1, Follow-do Message", follow_up_response)