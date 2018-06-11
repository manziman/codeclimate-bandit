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
    """Example bandit output:

        "results": [
            {
            "code": "4 def location_generated_num(host_network_num):\n5     ran_host_num = randint(1, 255)\n6     return \"\".join([str(host_network_num), str(ran_host_num)])\n",
            "filename": "./db_dir/custom_data.py",
            "issue_confidence": "HIGH",
            "issue_severity": "LOW",
            "issue_text": "Standard pseudo-random generators are not suitable for security/cryptographic purposes.",
            "line_number": 5,
            "line_range": [
                5
            ],
            "test_id": "B311",
            "test_name": "blacklist"
            },
            ...
    """


    # load to dict
    # data = json.loads(sys.argv[1])
    # testing

    print_json()
