#!/usr/bin/env python
from . import helpers # imports helpers.py from this directory
import time

should_loop = True # Variable to check if its running

def start_loop():
    """Start the script after some checks"""
    if helpers.do_this():
        loop_and_print()

def set_should_loop(bool):
    """Change the should_loop bool"""
    global should_loop
    should_loop = bool

def loop_and_print():
    """Loops while should_loop is True"""
    global should_loop
    while should_loop:
        print("Hello..")
        time.sleep(1)
