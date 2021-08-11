from faker import Faker


def stream_fake_people(n_max=None, seed=None):
    fake = Faker('en-US')
    if seed is not None:
        Faker.seed(seed)

    n = 0
    while True:
        person = {'first_name': fake.first_name(),
                  'last_name': fake.last_name(),
                  'ssn': fake.ssn(),
                  'address': fake.address(),
                  'date_of_birth': fake.date_of_birth().strftime('%Y%m%d'),
                  'phone_number': fake.phone_number()}

        yield person

        n += 1

        if n_max is not None:
            if n == n_max:
                break
