def get_data() -> dict:
    return {
        "data": {
            "users": [
                {
                    'name': 'admin1',
                    'id': '10',
                },
                {
                    'name': 'user1',
                    'id': '11',
                },
                {
                    'name': 'user2',
                    'id': '12',
                },
                {
                    'name': 'user3',
                    'id': '13',
                },
            ],
            "events": [
                {
                    'id': 100,
                    'place': 'london',
                    'time': '18:00:00',
                    'date': '2024-03-14',
                    'note': 'dress code'
                },
                {
                    'id': 101,
                    'place': 'sydney',
                    'time': '7:00:00',
                    'date': '2024-03-14',
                    'note': 'swimming'
                },
                {
                    'id': 102,
                    'place': 'new york',
                    'time': '19:00:00',
                    'date': '2024-03-13',
                    'note': 'delivery'
                },
                {
                    'id': 103,
                    'place': 'tbd',
                    'time': '22:00:00',
                    'date': '2024-03-16',
                    'note': 'dance'
                },

            ]

        }
    }


import os
import json

def _read_data() -> dict:
    file_json = {'data': []}

    if not 'data' in os.listdir():
        os.mkdir('data')
        return file_json

    with open(os.path.join('data', 'data.json'), 'r') as f:
        #file_content = f.read()
        file_json = json.load(f)

    return file_json


def _write_data():
    pass


