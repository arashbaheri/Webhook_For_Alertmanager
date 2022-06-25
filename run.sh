#!/bin/bash
# Released under GPLv3+ Licence
# Arash Baheri<arashbaheri@icloud.com>, 2022

export SHELL=/bin/bash
cd "$( dirname "${BASH_SOURCE[0]}" )"
source .venv/bin/activate
python3 WebHook.py
