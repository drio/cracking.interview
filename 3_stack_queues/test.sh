#!/bin/bash
# pip install sniffer
# sniffer -x--verbose -x--with-doctest
filewatcher *.py "python test.py; echo "

