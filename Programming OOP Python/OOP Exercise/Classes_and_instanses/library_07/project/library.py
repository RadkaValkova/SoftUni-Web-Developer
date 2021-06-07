
class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self,user):
        if user not in self.user_records:
            self.user_records.append(user)
        return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self,user):
        if user not in self.user_records:
            return 'We could not find such user to remove!'
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        if user_id not in [el.user_id for el in self.user_records]:
            return f'There is no user with id = {user_id}!'
        current_user = [el for el in self.user_records if el.user_id == user_id][0]
        if current_user.username == new_username:
            return 'Please check again the provided username - it should be different than the username used so far!'
        current_user.username = new_username
        return f'Username successfully changed to: {new_username} for userid: {user_id}'



