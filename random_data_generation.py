from faker import Faker


fake = Faker()


def generate_first_name():
    return fake.first_name()


def generate_last_name():
    return fake.last_name()


first_name = generate_first_name()
last_name = generate_last_name()
