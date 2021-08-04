#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import json


# file.py Module Provides File Loading Methods.

# Load File In. User Generator. Yield Sends One Line At A Time For Processing.
def loadFile(file):
    try:
        with open(file) as f:
            for doc in f:
                yield json.loads(doc)
    except KeyError:
        pass
    except FileNotFoundError as fe:
        print(fe)
    except Exception as e:
        print(e)


# Variation Of LoadFile Method. Ensures Documents Without subject_doc_id Are Not Yielded.
def loadFileFiltered(file):
    try:
        with open(file) as f:
            for doc in f:
                if 'subject_doc_id' in doc:
                    yield json.loads(doc)
    except KeyError:
        pass
    except FileNotFoundError as fe:
        print(fe)
    except Exception as e:
        print(e)
