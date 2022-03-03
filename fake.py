from faker import Faker
import random

media = ['CC', 'MC', 'DD']
data_factory = Faker(['es_CO'])

Faker.seed(1000)

for i in range(10):
    print(data_factory.unique.name())
    print(data_factory.unique.email())
    print(data_factory.unique.phone_number())
    print(data_factory.random_int(1800, 2020))
    print(data_factory.text())
    print(random.choice(media))