from faker import Faker

fake = Faker("ru_RU")


def generate_password():
    random_sentence = fake.sentence()
    return random_sentence
