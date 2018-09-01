sample_dict = {1: 'a', 2: 'b', 3: 'c'}

def get_keys_sorted_by_value(adict):
    return sorted(adict, key=adict.get)


def get_sorted_values(adict):
    return sorted(adict.values())


def get_inverse_dict(adict):
    inverse = {}
    for key, value in adict.items():
        inverse[value] = key

    return inverse


def create_dict(keys, values):
    adict = {}
    for key, value in zip(keys, values):
        adict[key] = value
    return adict

if __name__ == '__main__':
    print("Variable __name__ is %s" % __name__)
    print("This is the dict_utils module. Use it for all your dictionary needs")
