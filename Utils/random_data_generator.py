from faker import Faker

class RandomData:
    def __init__(self):
        self.faker = Faker()

    def get_firstname(self):
        return self.faker.first_name()

    def get_firstname_set_number_of_characters(self, number):
        # the random_letters returns a list of characters so it needs to be converted to a string
        return ''.join(self.faker.random_letters(length=number))

    def get_firstname_less_than_minimum(self):
        # the random_letters returns a list of characters so it needs to be converted to a string
        return ''.join(self.faker.random_letters(length=2))

    def get_firstname_minimum_characters(self):
        # the random_letters returns a list of characters so it needs to be converted to a string
        return ''.join(self.faker.random_letters(length=3))

    def get_lastname(self):
        return self.faker.last_name()

    def get_email(self):
        return self.faker.email()

    def get_phone_number(self):
        return self.faker.phone_number()

    def get_password(self):
        return self.faker.password()

