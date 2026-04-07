def flatten(dict_data:dict) -> dict:
    if dict_data is None:
        return None
    new_dict = {}
    for key,value in dict_data.items():
        if type(value) not in [list,dict]:
            new_dict[key] = value
        elif isinstance(value, list):
            for idx, elem in enumerate(value):
                new_prefix = f"{key}[{idx}]"

                if isinstance(elem, dict):
                    values = flatten(elem)
                    for k, v in values.items():
                        new_dict[f"{new_prefix}.{k}"] = v
                else:
                    new_dict[new_prefix] = elem
        else:
            values = flatten(value)
            for k,v in values.items():
                new_prefix = f"{key}.{k}"
                new_dict[new_prefix] = v

    return new_dict

if __name__ == "__main__":
    sample_input = {
    "user": {
        "id": 101,
        "profile": {
            "name": "Alice",
            "contact": {
                "email": "alice@example.com",
                "phones": ["123-456-7890", "987-654-3210"]
            }
        }
    },
    "settings": {
        "theme": "dark",
        "notifications": {
            "email": True,
            "sms": False,
            "push": {
                "enabled": True,
                "sound": "chime"
            }
        }
    },
    "projects": [
        {
            "title": "AI Research",
            "details": {
                "deadline": "2026-05-01",
                "tasks": ["literature review", "experiments", "report"]
            }
        },
        {
            "title": "Web App",
            "details": {
                "deadline": "2026-06-15",
                "tasks": ["frontend", "backend", "deployment"]
            }
        }
    ]
}
    
    print(flatten(sample_input))
    print("=" * 40)
    nested = {
    'fullname': 'Alessandra',
    'age': 41,
    'phone-numbers': ['+447421234567', '+447423456789'],
    'residence': {
        'address': {
            'first-line': 'Alexandra Rd',
            'second-line': 'Cool house',
        },
        'zip': 'N8 0PP',
        'city': 'London',
        'country': 'UK'
    }
}
    print(flatten(nested))
    