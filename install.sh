#!/bin/bash

FOLDER_NAME="venv"

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "This script must be sourced. Use: . ${0}" >&2
  exit 1
fi

python3 -m venv $FOLDER_NAME
source $FOLDER_NAME/bin/activate

python3 -m pip install -r requirement.txt
