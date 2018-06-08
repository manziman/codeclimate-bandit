#!/bin/bash

bandit -r -f json /code | sed -r -n -e '/result/,${p}' \
| sed 's/\"code\"/\"type\": \"issue\",\n    \"content\"/g' \
| sed 's/issue_text/description/g' | sed 's/],/]/g' \
| sed 's/\"filename\"/\"categories\": \[\"Security\"\],\n    \"filename\"/g' \
| sed 's/test_name/check_name/g' | sed 's/line_number/location/g' \
| sed 's/line_range/other_locations/g' | sed 's/issue_severity/severity/g' \
| sed 's/^  \"results\": \[$/{\n  \"results\": \[/g' | sed '/^.*\(issue_confidence\|test_id\|check_name\).*$/d' \
| xargs -0 -I {} python3 /scripts/run.py {}