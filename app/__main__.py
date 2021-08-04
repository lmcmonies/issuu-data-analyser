#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import sys
import tasks as task
import getopt
import datamethods as methods
import countries as dictionary
#import charts
import tkinter as tk
from tkinter import filedialog
import fileIO


# Menu Takes TaskId From Command Line Option -t. Executes Relevant Task.
def menu():
    if taskId == '2a':
        task.task2a(fileName, docId)
    elif taskId == '2b':
        task.task2b(fileName, docId)
    elif taskId == '3a':
        task.task3a(fileName)
    elif taskId == '3b':
        task.task3b(fileName)
    elif taskId == '4':
        task.task4(fileName)
    elif taskId == '5d':
        task.task5d(docId, visitorId, fileName)
    elif taskId == '6':
        task.task6(docId, visitorId, fileName)
    elif taskId == '7':
        task.task7()


# Entry Point Of The Application
if __name__ == '__main__':

    # Variables Hold Command Line Args
    visitorId = None
    docId = None
    taskId = None
    fileName = None

    argv = sys.argv[1:]
    # CLI Options Stored In List
    # Reference: [7]
    try:
        options, args = getopt.getopt(argv, "u:d:t:f:")
    except getopt.GetoptError as err:
        print(err)

    #  Iterate Through Options And Assigns To Relevant Variables.
    for option, arg in options:
        if option in ['-u']:
            visitorId = arg
        elif option in ['-d']:
            docId = arg
        elif option in ['-t']:
            taskId = arg
        elif option in ['-f']:
            fileName = arg

    menu()
