#!/bin/bash

cd /usr/share/pyaccounts/PyAccounts
source ../bin/activate
../bin/python3.10 PyAccounts.py "$@" 2>/tmp/`date +'%d-%m-%Y_%H:%M:%S'`-PyAccounts.log
