import json
import os
import sys


def print_json(data):
    with os.fdopen(sys.stdout.fileno(), 'wb') as fp:
        for result in data["results"]:
            # Write to stdout buffer
            fp.write(json.dumps(result, ensure_ascii=False).encode())
            # write null byte after result
            fp.write(b'\00')
            # flush to stdout
            fp.flush()


if __name__ == '__main__':
    # read json data from file
    json_data = open("/scripts/results.json").read()

    # load to dict
    data = json.loads(json_data)

    print_json(data)
