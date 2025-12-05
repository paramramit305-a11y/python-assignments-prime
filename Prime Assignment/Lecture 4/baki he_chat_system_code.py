# chat_system.py

class Message:
    message_counter = 1  # simple counter

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        # sender might be a User object, show its username
        username = getattr(self.sender, "username", str(self.sender))
        return f"({self.id}) {username}: {self.content}"


class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom is not None:
            print(f"{self.username} is already in a chatroom ({self.chatroom.name}).")
            return
        chatroom.add_user(self)
        self.chatroom = chatroom
        print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if self.chatroom is None:
            print(f"{self.username} is not in any chatroom.")
            return
        # remove user from the chatroom
        self.chatroom.remove_user(self)
        print(f"{self.username} left {self.chatroom.name}")
        self.chatroom = None

    def send_message(self, content):
        if self.chatroom is None:
            print(f"{self.username} cannot send a message (not in a chatroom).")
            return
        self.chatroom.broadcast(self, content)


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user in self.users:
            return
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        # Create message and store it
        message = Message(sender, content)
        self.messages.append(message)
        # Print to console to simulate broadcasting
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        if not self.messages:
            print("  -- No messages yet --")
            return
        for msg in self.messages:
            print(msg)


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    # user3 joins later
    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    # Show chat history
    room.show_chat_history()

    # Users leave
    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
