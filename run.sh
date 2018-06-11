#!/bin/bash

bandit -r -f json /code | xargs -0 -I {} python3 /scripts/run.py {}