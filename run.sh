#!/bin/bash

bandit -r -f json /code \
| sed '$ d' | sed 's/^  //g' \
| sed -r -n -e '/result/,${p}' \
| sed 's/^\"results\": //g' \
| sed 's/\"code\"/\"type\": \"issue\",\n    \"content\"/g' \
| sed 's/issue_text/description/g' \
| sed 's/],/]/g' | sed 's/\"filename\"/\"categories\": \[\"Security\"\],\n    \"filename\"/g' \
| sed 's/test_name/check_name/g' | sed 's/line_number/location/g' \
| sed 's/line_range/other_locations/g' | sed 's/issue_severity/severity/g' \
| sed '/^.*\(issue_confidence\|test_id\|check_name\).*$/d' \
| sed '$ d' | tr -d '\n' | sed 's/},/}\n/g' | sed 's/\[  {/{/g' \
| sed 's/^  //g' | sed 's/{ */{/g' | sed 's/, *\"/,\"/g' \
| sed 's/\[ */\[/g' | sed 's/ *\]/\]/g' | sed 's/\] *}/\]}/g'