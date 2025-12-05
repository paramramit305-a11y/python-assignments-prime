class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


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
            print(f"{self.username} is not in a chatroom.")
            return
        self.chatroom.remove_user(self)
        print(f"{self.username} left {self.chatroom.name}")
        self.chatroom = None

    def send_message(self, content):
        if self.chatroom is None:
            print(f"{self.username} cannot send message (not in any chatroom).")
            return
        self.chatroom.broadcast(self, content)


class Chatroom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user in self.users:
            # already present -> ignore
            return
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        msg = Message(sender, content)
        self.messages.append(msg)
        print(msg)    # simulate delivering to all users

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        if not self.messages:
            print("  -- No messages yet --")
            return
        for m in self.messages:
            print(m)


# ------------ quick test -------------
if __name__ == "__main__":
    room = Chatroom("Python Lounge")
    a = User("Amit")
    b = User("Asif")

    a.join_chatroom(room)
    b.join_chatroom(room)

    a.send_message("Hello everyone!")
    b.send_message("Hi Amit!")

    room.show_chat_history()

    a.leave_chatroom()
    b.leave_chatroom()
