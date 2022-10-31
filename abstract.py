from abc import ABC, abstractmethod

class User:
    first_name = '',
    last_name = '',
    alias = '',
    password = ''

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

class UserManager(UserAbstract):
    def create_user(self, user: User):
        print("User Information")

user_manager = UserManager()
user_manager.get_all_user_by_id()

# Implement a product class called Product abstract and implement instasiation      of productManager