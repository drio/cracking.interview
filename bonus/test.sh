#!/bin/bash
# pip install sniffer
# sniffer -x--verbose -x--with-doctest
filewatcher *.py "clear;date;python test.py"
