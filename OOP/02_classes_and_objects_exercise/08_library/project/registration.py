from project.user import User
from project.library import Library

class Registration:

    @staticmethod
    def add_user(user: User, library: Library) -> str or None:
        if user not in library.user_records:
            library.user_records.append(user)

        return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library) -> str:
        try:
            library.user_records.remove(user)
        except ValueError:
            return "We could not find such user to remove!"

        if user.username in library.rented_books:
            library.rented_books.pop(user.username)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        user = next((u for u in library.user_records if user_id == u.user_id), None)

        if user is None:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books[user.username]
            library.rented_books.pop(user.username)

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"

