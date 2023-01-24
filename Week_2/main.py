from utils import *


class User:
    def __init__(self, user_id: int, username, user_created_time):
        self.user_id = user_id
        self.username = username
        self.user_created_time = user_created_time

    @property
    def add_new_user(self):
        values = {"user_id": self.user_id, "username": self.username, "created_at": self.user_created_time}
        write_data(file_name="Users.txt", content=values)
        print(f'ID добавленного пользователя: {self.user_id}')
        return values


class Chat:
    def __init__(self, chat_id: int, chat_name, chat_users: list, chat_created_time):
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.chat_users = chat_users
        self.chat_created_time = chat_created_time

    @property
    def add_new_chat(self):
        values = {"chat_id": self.chat_id, "chat_name": self.chat_name, "users": self.chat_users, "created_at": self.chat_created_time}
        write_data(file_name="Chats.txt", content=values)
        print(f'ID созданного чата: {self.chat_id}')
        return values


class Message:
    def __init__(self, message_id, message_chat, message_author, message_text, message_created_time):
        self.message_id = message_id
        self.message_chat = message_chat
        self.message_author = message_author
        self.message_text = message_text
        self.message_created_time = message_created_time


if __name__ == "__main__":
    """username = input("Введите Ваш username: ")
    user_id = get_id(username)
    created_at = get_created_time()
    request = User(user_id=user_id, username=username, user_created_time=created_at).add_new_user"""
    """created_at = get_created_time()
    chat_users = how_users()
    chat_name = get_name()
    chat_id = get_id(chat_name)
    request = Chat(chat_id=chat_id, chat_name=chat_name, chat_users=chat_users, chat_created_time=created_at).add_new_chat"""
    get_users_chats()
