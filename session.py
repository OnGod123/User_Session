import uuid
import time

class Session:
    def __init__(self, user_id):
        self.__session_id = str(uuid.uuid4())  # Private instance variable
        self.__user_id = user_id               # Private instance variable
        self.__data = {}                       # Private instance variable
        self.creation_time = time.time()       # Public instance variable

    def get_session_id(self):
        """Public method to access the session ID."""
        return self.__session_id

    def get_user_id(self):
        """Public method to access the user ID."""
        return self.__user_id

    def get_data(self, key):
        """Public method to access session data."""
        return self.__data.get(key)

    def set_data(self, key, value):
        """Public method to update session data."""
        self.__data[key] = value

    def clear_data(self):
        """Public method to clear session data."""
        self.__data.clear()

    def __str__(self):
        """Private method to return a string representation of the session."""
        return f"Session(session_id={self.__session_id}, user_id={self.__user_id}, data={self.__data})"

    def display(self):
        """Public method to display session details."""
        print(self.__str__())

