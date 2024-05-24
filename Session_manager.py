class SessionManager:
    def __init__(self):
        self.sessions = {}  # Dictionary to store sessions

    def create_session(self, user_id):
        """Create a new session and store it in the sessions dictionary."""
        session = Session(user_id)
        self.sessions[session.get_session_id()] = session
        return session.get_session_id()

    def get_session(self, session_id):
        """Retrieve a session by session ID."""
        return self.sessions.get(session_id)

    def update_session_data(self, session_id, key, value):
        """Update data in an existing session."""
        session = self.get_session(session_id)
        if session:
            session.set_data(key, value)
        else:
            print("Session not found")

    def delete_session(self, session_id):
        """Delete a session by session ID."""
        if session_id in self.sessions:
            del self.sessions[session_id]
        else:
            print("Session not found")

    def clear_all_sessions(self):
        """Clear all sessions."""
        self.sessions.clear()

# Example usage
if __name__ == "__main__":
    session_manager = SessionManager()

    # Create a new session
    user_id = 1
    session_id = session_manager.create_session(user_id)
    print(f"New session created: {session_id}")

    # Update session data
    session_manager.update_session_data(session_id, 'last_page_visited', 'home')
    session_manager.update_session_data(session_id, 'cart_items', ['item1', 'item2'])

    # Retrieve and display session
    session = session_manager.get_session(session_id)
    if session:
        session.display()

    # Delete the session
    session_manager.delete_session(session_id)
    print(f"Session {session_id} deleted")

