#!/usr/bin/env bash
#
# Purpose of this script is to make deployments one-click from Pycharm IDE
#

# Move one folder above and initiate python environment
source ../VENV/bin/activate
fab deploy:host=elspeth@journal.abraham-v.com
