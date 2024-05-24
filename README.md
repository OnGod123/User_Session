SessionManager
This class manages user sessions within an application. It provides methods for creating, retrieving, updating, and deleting sessions.

Usage
python
Copy code
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
Methods
create_session(user_id): Create a new session for the specified user ID.
get_session(session_id): Retrieve a session by session ID.
update_session_data(session_id, key, value): Update data in an existing session.
delete_session(session_id): Delete a session by session ID.
clear_all_sessions(): Clear all sessions.
Example Usage
python
Copy code
session_manager = SessionManager()

# Create a new session
user_id = 1
session_id = session_manager.create_session(user_id)

# Update session data
session_manager.update_session_data(session_id, 'last_page_visited', 'home')
session_manager.update_session_data(session_id, 'cart_items', ['item1', 'item2'])

# Retrieve and display session
session = session_manager.get_session(session_id)
if session:
    session.display()

# Delete the session
session_manager.delete_session(session_id)
This README provides a brief overview of the SessionManager class and its usage. For more details on each method, please refer to the docstrings within the code.
