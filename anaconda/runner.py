#!/usr/bin/env python

""" This is an example for what a project looks like
with multiple modules and threads while trying to use best practices.
"""
# Imports
import time
import threading 

# local 
from anaconda.hello import hello
from anaconda.world import world

# Storage
hello_running = False
world_running = False

def toggle_hello():
    """Run / stop hello, could ask for some parameters before running the function and pass that to the 
    hello.start_loop with threading.Thread(target=hello.start_loop, args=(paramet,))"""
    global hello_running
    hello_running ^= True # Toggle global parameter so this acts like a switch

    if hello_running: 
        hello.set_should_loop(True) 
        # Should start multithreading here so this runner thread is not blocked.  
        # threading = more lightweight than multiprocessing
        # coroutines are even better but didn't look into that yet
        hello_thread = threading.Thread(target=hello.start_loop)
        hello_thread.start()
    else:
        hello.set_should_loop(False)   

def toggle_world():
    """Run / stop hello, could ask for some parameters before running the function and pass that to the 
    hello.start_loop with threading.Thread(target=hello.start_loop, args=(paramet,))"""
    global world_running
    world_running ^= True # Toggle global parameter so this acts like a switch

    if world_running: 
        world.set_should_loop(True) 
        # Should start multithreading here so this runner thread is not blocked.  
        # threading = more lightweight than multiprocessing
        # coroutines are even better but i dont know about them (just yet)
        world_thread = threading.Thread(target=world.start_loop)
        world_thread.start()
        return
    else:
        world.set_should_loop(False)   
        return

def start():
    """Start our script/program"""

    # needed variables
    global hello_running
    global world_running

    # Print our menu
    # Keeps looping so the menu will always be there after a choice is done.
    while(True):
        # Option 1
        if hello_running:
            print('[1] | Stop hello')
        else:
            print('[1] | Run hello')
        # Option 2
        if world_running:
            print('[2] | Stop world')
        else:
            print('[2] | Run world')
        # Exit
        print('[3] | Exit program')

        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        
        #Check what choice was entered and act accordingly
        if option == 1:
           toggle_hello()
        elif option == 2:
            toggle_world()
        elif option == 3:
            print('Quiting program..')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')

if __name__ == '__main__':
    start()