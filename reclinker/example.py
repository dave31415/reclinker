import recordlinkage
from recordlinkage.datasets import load_febrl4


def get_data():
    data_ba, data_b = load_febrl4()
    return data_ba, data_b


def get_indexer(data_a, data_b):
    # Indexation step
    indexer = recordlinkage.Index()
    indexer.block('given_name')
    candidate_links = indexer.index(data_a, data_b)
    return candidate_links


def get_comparison():
    # Comparison step
    compare_cl = recordlinkage.Compare()

    compare_cl.exact('given_name', 'given_name', label='given_name')
    compare_cl.string('surname', 'surname', method='jarowinkler', threshold=0.85, label='surname')
    compare_cl.exact('date_of_birth', 'date_of_birth', label='date_of_birth')
    compare_cl.exact('suburb', 'suburb', label='suburb')
    compare_cl.exact('state', 'state', label='state')
    compare_cl.string('address_1', 'address_1', threshold=0.85, label='address_1')
    return compare_cl


def compute(compare_cl, candidate_links, data_a, data_b):
    features = compare_cl.compute(candidate_links, data_a, data_b)
    print(features)
    return features


def classify_by_hand(features):
    # Classification step
    matches = features[features.sum(axis=1) > 3]
    n_matches = len(matches)
    print('n_matches_by_hand: %s' % n_matches)
    return matches


def classify_ecm(features):
    ecm = recordlinkage.ECMClassifier()
    matches = ecm.fit_predict(features)
    n_matches = len(matches)
    print('n_matches_ecm: %s' % n_matches)
    return matches


def main():
    data_a, data_b = get_data()
    print(data_a)
    candidate_links = get_indexer(data_a, data_b)
    compare_cl = get_comparison()
    features = compute(compare_cl, candidate_links, data_a, data_b)
    matches = classify_by_hand(features)
    print('matches')
    print(matches)

    matches_ecm = classify_ecm(features)
    print('matches_ecm')
    print(matches_ecm)


if __name__ == "__main__":
    main()
