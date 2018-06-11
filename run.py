import json


def print_json():
    issue = {
        'type': 'issue',
        'check_name': 'Unused Variable',
        'categories': ['Style'],
        'description': 'Unused local variable foo',
        'remediation_points': 50000,
        'location': {
            'path': 'db_dir/project_db.py',
            'positions': {
                'begin': {
                    'line': 13,
                    'column': 1
                },
                'end': {
                    'line': 14,
                    'column': 5
                }
            }
        },
        'content': {
            'body': 'This is a markdown snippet'
        }
    }

    print(json.dumps(issue) + '\0')


if __name__ == '__main__':
    # read json data from file
    # json_data = open("/scripts/results.json").read()

    # load to dict
    # data = json.loads(sys.argv[1])
    # testing

    print_json()
