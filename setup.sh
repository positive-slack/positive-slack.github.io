#!/bin/bash

set -e

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
pelican-themes -i themes/attila
pelican-themes -i themes/blue-penguin-dark