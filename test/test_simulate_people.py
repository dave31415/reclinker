from reclinker.simulate_people import stream_fake_people
from reclinker.util.util import take


def test_simulate_people():
    people = stream_fake_people(n_max=10)
    class_gen = (i for i in range(5)).__class__
    assert isinstance(people, class_gen)

    people_list = list(people)
    assert len(people_list) == 10

    people = stream_fake_people()
    peeps = take(people, 123)
    assert isinstance(peeps, list)
    assert len(peeps) == 123

    first = peeps[1]
    assert isinstance(first, dict)
    keys = set(first.keys())
    expected = {'last_name', 'address', 'ssn', 'first_name',
                'date_of_birth', 'phone_number'}

    assert keys == expected


def test_simulate_can_be_deterministic():
    # set the seed and expect determinism
    people = stream_fake_people(n_max=10, seed=420)
    first = next(people)
    print(first)
    assert first['first_name'] == 'Anthony'
    assert first['last_name'] == 'Harrington'
