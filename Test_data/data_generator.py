from faker import Faker

class FakeData:
    def __init__(self):
        self.fake = Faker()

    def get_username(self):
        return self.fake.user_name()

    def get_password(self):
        return self.fake.password()