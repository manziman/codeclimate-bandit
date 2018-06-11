import json
import sys


def print_json(result):
    """Format bandit to codeclimate issue and print

    Take a bandit issue and format to a codecliamte
    issue. Then print.
    
    Arguments:
        result {dict} -- a bandit result.
    """
    path = "/".join(result["filename"].split("/")[2:])

    issue = {
        "type": "issue",
        "check_name": result["test_name"],
        "categories": ["Style"],
        "description": result["issue_text"],
        "remediation_points": 50000,
        "location": {
            "path": path,
            "lines": {
                "begin": result["line_range"][0],
                "end": result["line_range"][-1]
            }
        },
        "content": {
            "body": result["code"]
        }
    }

    print(json.dumps(issue) + "\0")


if __name__ == "__main__":
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
    data = json.loads(sys.argv[1])

    for result in data["results"]:
        print_json(result)
