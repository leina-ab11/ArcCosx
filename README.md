# F1: arccos(x)

This is a calculator for calculating arccos(x) within the domain of [-1,1]. 

The calculator uses built from scratch nan checker, square root function using Newton's method and Maclaurin's method to calculate arccos(x).
The code imports Tkinter for gui purposes only.

To access the repository you can navigate to [arccos(x) GitHub repository](https://github.com/leina-ab11/ArcCosx)

## Files:

The breakdown of the files is as follows:
* gui.py: This is responsible for a gui for the user to enter values within [-1,1], it shows the results for the user and the errors accordingly.
* helper_math_functions.py: This is responsible for all of the helper functions that can help with separation of concerns. Since the solution relies heavily on mathematical equations, they were placed into this file. Nan checking, square root function, Maclaurin's method for finding arccos(x) are all contained within this file.
* main.py: This is the old textual interface from D1. It is left in the repository for reference. gui.py is an incremental enhancement of main.py.
* user_input.py: This is responsible for the user's input. It is in a separate file to ensure both textual and graphical interfaces work without triggering the other by accident. 

## Requirements:
**Python 3 or higher.**

## How to Run:

* To run the code based on D1 requirements you run:
```bash 
python main.py
```
* To run the code based on D2 requirements you run:
```bash
python gui.py
```
