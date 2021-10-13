# MY ANACONDA DON'T
Python example making use of best practice file structure and multithreading.  

***made for python3+ en Kipsiam***

---
## File structure
---
```
project/
|
|-- anaconda/
|   |-- runner.py (Main entrypoint)
|   |-- __main__.py 
|   |-- hello/
|   |   |-- hello.py (hello module)
|   |   |-- helpers.py (helper functions for hello module)
|   |
|   |-- world/
|       |-- world.py
|       |-- helpers.py
|
|-- data/  (Data folder could contain input/output files like logs while testing the application)
|   |-- input.txt 
|
|-- docs/  (Bigger/more complicated apps should have documentation for each module)
|   |- hello.md 
|   |- world.md
|
|-- readme.md (You are reading this one)
|-- LICENSE (Yes you should have a LICENSE)
|-- requirements.txt (Pip requirements to install)
|-- Makefile (A makefile could be used to automate tests and setup)
|-- .gitignore (files being ignored by git)
```
---
## Running
---
* Open the root as workspace folder and run `python3 -m anaconda` or `py -m anaconda` (depends on your path).
* Setup and run with `make setup` to install dependencies and `make run` to run the script
* Can't run this with the debug button i think. Learn some commands like `ctrl + ~`
---
## More
---
### Notes
* Makefile uses Make. You can install that with `choco install make` while having [Chocolatery](https://chocolatey.org/install) installed.  Or skip it all together..
* Opened up threads cant be closed with ctrl+c. If it chrases use your task manager. Should use a global variable for stopping it (like we are doing in this example) or change to classes with a [function that raises an exeption](https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/)
* the `__main__.py` in anaconda/ is there so we can run the module with `python3 -m anaconda`
* This project doesnt use any pip dependencies, but its there as an example
* It might be better to thread a whole Class instead of a method (function)

### Resources
* [More about multithreading](https://nitratine.net/blog/post/python-threading-basics/)
* [python3 import system](https://docs.python.org/3/reference/import.html#)
* [Best python guide ever](https://letmegooglethat.com/?q=How+to+do+X+in+python)

### Credits
BahbV <bob@bahbv.net>
