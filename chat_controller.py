import uuid

class ChatController:
    def __init__(self):
        self.test_session = {}

    # TODO: Define the ensure_user_session method
    # - Check if 'user_id' is in the test_session dictionary
    # - Generate and store a new user_id using uuid if it doesn't exist
    # - Return the user_id from the test_session
    def ensure_user_session(self):
       """Ensure user has a session ID in the test session."""
       if 'user_id' not in self.test_session:
        self.test_session['user_id'] = str(uuid.uuid4())
       return self.test_session['user_id']