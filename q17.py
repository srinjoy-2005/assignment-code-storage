def flatten(d, parent=''):
    return {
        k: v
        for key, val in d.items()
        for k, v in (
            flatten(val, f"{parent}.{key}" if parent else key).items()
            if isinstance(val, dict)
            else {
                f"{parent}.{key}" if parent else key: val
            }.items()
        )
    }

nested = {
    'fullname': 'Alessandra',
    'age': 41,
    'phone-numbers': ['+447421234567', '+447423456789'],
    'residence': {
    'address': {
    'first-line': 'Alexandra Rd',
    'second-line': '',
    },
    'zip': 'N8 0PP',
    'city': 'London',
    'country': 'UK',

    },
}

flattened = flatten(nested)
for(key, value) in flattened.items():
    print(f"{key}: {value}")