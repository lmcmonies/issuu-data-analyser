#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import itertools as it
from tkinter import filedialog


# datamethods.py Provides All Methods For The Logic Of The Document Tracker Application.

# Task 2a

# Generates A List Of All Countries In Documents Based On Document Id.
def generateCountriesList(documentId, document):
    countriesList = []
    for doc in document:
        try:
            if doc['subject_doc_id'] == documentId:
                countriesList.append(doc['visitor_country'])
        except KeyError:
            pass
    return countriesList


# Documents by Country
def generateCountriesDict(countriesDict, countriesList):
    for country in countriesDict:
        for val in countriesList:
            if country == val:
                countriesDict[country] = countriesDict[country] + 1
    return countriesDict


# Filter Countries Dict
def filterCountriesDict(countriesDict):
    filteredCountriesDict = {}
    for country, val in countriesDict.items():
        if val > 0:
            filteredCountriesDict[country] = val
    return filteredCountriesDict


# Task 2b

# Group Countries by Continents
def generateContinentsDict(filteredCountriesDict, countriesInContinentsDict, continentsDict):
    for key, val in filteredCountriesDict.items():
        for continent in countriesInContinentsDict:
            for country in countriesInContinentsDict[continent]:
                if country == key:
                    continentsDict[continent] += val
    return continentsDict


# Filter Continents Dict
def filterContinentsDict(continentsDict):
    filteredContinentsDict = {}
    for key, val in continentsDict.items():
        if val > 0:
            filteredContinentsDict[key] = val
    return filteredContinentsDict


# Task 3a

# Filter JSON Objects by Browser. Used In Task 3a.
def generateBrowserListAndDictV1(document):
    browserList = []
    browserDict = {}
    for doc in document:
        try:
            string = doc["visitor_useragent"]
            browserList.append(string)
            if string not in browserDict:
                if doc["visitor_device"] == "browser":
                    browserDict[string] = 0
        except KeyError:
            pass
    return browserList, browserDict


# Task 3b

# # Filter JSON Objects by Browser Splitting String On First / .Used in Task 3b.
def generateBrowserListAndDictV2(document):
    browserList = []
    browserDict = {}
    for doc in document:
        try:
            string = doc["visitor_useragent"]
            substring = string.split('/')[0]
            stripped = substring.strip('"')
            browserList.append(stripped)
            if stripped not in browserDict:
                if doc["visitor_device"] == "browser":
                    browserDict[stripped] = 0
        except KeyError:
            pass
    return browserList, browserDict


# Calculate Totals For Each Browser.
def calculateBrowserDict(browserDict, browserList):
    for browser in browserList:
        for k, v in browserDict.items():
            if browser == k:
                browserDict[k] += 1
    return browserDict


# Task 4

# Generate Visitors Dict. Groups Each JSON Object By Visitor Id.
def generateVisitorsDict(document):
    visitorsDict = {}
    # Input: document, lambda: Group on visitor_uuid.
    # Reference: [6]
    for key, group in it.groupby(document, key=lambda x: x['visitor_uuid']):
        for obj in group:
            visitorsDict[obj['visitor_uuid']] = 0
    return visitorsDict


# Calculates Read Time Of Each Visitor
def calcReadTime(document, visitorsDict):
    for doc in document:
        try:
            pageReadTime = doc['event_readtime']
            visitorsDict[doc['visitor_uuid']] += pageReadTime
        except KeyError:
            pass
    return visitorsDict


# Sorts The VisitorsReadTimeDict Into A Top 10, Largest ReadTime Value First.
def determineTop10Readers(visitorsReadTimeDict):
    # Reference: [18]
    # Sorted: Adapted From [18].
    # Input: visitorsReadTimeDict, Lambda: Sort On visitor_uuid, Reverse: Descending, 10: 10 Values In Total
    top10 = sorted(visitorsReadTimeDict.items(), key=lambda x: x[1], reverse=True)[:10]
    return top10


# Tasks 5/6

# Task 5a.
# Generates A List Of Visitors That Have Read The Input Document.
# Filters Out Visitor If Visitor Id Specified.
def generateReadersList(documentId, visitorId, document):
    readersList = []  # Holds Readers Values (visitor_uuid)
    for doc in document:  # Iterates Through Each Document In File
        try:
            if doc['visitor_uuid'] not in readersList:  # Ensures No Duplicate Readers
                if doc['visitor_uuid'] != visitorId:  # Filters Out Docs Read By Visitor Id
                    if documentId == doc['subject_doc_id']:  # Ensures Document Id Matches Document Id In File Document
                        if doc['event_type'] == 'read':  # Ensures Document Has Been Read
                            readersList.append(doc['visitor_uuid'])  # Adds Reader To Readers List.
        except KeyError:
            pass
    print("\n***Readers List***")  # Prints Readers List To Console
    for doc in readersList:
        print(doc)
    return readersList  # Returns Readers List For Further Processing


# Task 5b
# Generates A Dictionary Where Values Are Sets Containing Documents Read By The Readers Defined In The
# readersList.
def constructDocDict(document, readersList, documentId):
    docsReadDict = {}  # Holds Document Id of Document Reader Has Read. Key: visitor_uuid, Value: subject_doc_id
    try:
        for doc in document:  # Iterate Through Each Document In File
            for reader in readersList:  # Iterate Through Each Reader In Readers List
                if doc["subject_doc_id"] != documentId:  # Filter Out Input Document
                    if doc["event_type"] == 'read':  # Check Document Has Been Read
                        if doc['visitor_uuid'] == reader:  # Check Doc Visitor Id Matches Visitor Id In List
                            # Current Reader Is Key, Current Document Id Added To Current Readers Set.
                            # Reference: [8]
                            docsReadDict.setdefault(reader, set()).add(doc["subject_doc_id"])
    except KeyError:
        pass
    print("\n***Docs Read By Readers***")
    for doc in docsReadDict.items():  # Print Dictionary In Console
        print(doc)
    return docsReadDict  # Return Constructed Document Read By Readers Dictionary For Further Processing.


# Count Method Used By calcAlsoLikes Method.
def count(docId, docsReadDict):
    num = 0
    for key, val in docsReadDict.items():  # Iterate Through docsReadDict
        if docId in docsReadDict[key]:  # If docId in Current Keys Set, proceed.
            num += 1  # Add 1 to Num
    return num  # Return Num For Further Processing


# Generates A List Of Tuples. Each Tuple Generated Contains: (Number Of Readers: 'document_uuid').
def calcAlsoLikes(docsReadDict):
    unionSet = set([])  # Holds A Union Of All Sets In docsReadDict.
    for key, val in docsReadDict.items():
        unionSet = unionSet | set(docsReadDict[key])  # Generates Union Set Based On Each Set Held In docsReadDict

    # List Comprehension. Creates List Of Tuples. A Comparison Is Done Between docId In unionSet And docsReadDict.
    # This Comparison Generates Number Of Readers In The Tuple.
    alsoLikesList = [(count(docId, docsReadDict), docId) for docId in unionSet]

    return alsoLikesList  # Return List Of Tuples For Further Processing.


# Sorts alsoLikes List In Descending Order.
def determineTop10AlsoLikeDocs(alsoLikes):
    # Reference: [18]
    # Sorted: Adapted From [18].
    # Input: alsoLikes, Lambda: Sort On Tuple Item 0, Reverse: Descending, 10: 10 Values In Total
    top10AlsoLikes = sorted(alsoLikes, key=lambda x: x[0], reverse=True)[:10]
    return top10AlsoLikes  # Return Sorted alsoLikes List For Display


# Helper Methods
# Resets Dictionary Values To 0
def resetDictionaryValues(dictionary):
    for key in dictionary:
        dictionary[key] = 0
    return dictionary


# Tool For Displaying Data In Gui Display Box.
# Reference: https://stackoverflow.com/questions/20768405/print-dictionary-in-python-ttk
# Reference: [10]
# Adapted from falsetru and [10]
def displayTool(label, fName, dataStruct):
    string = label + fName.rsplit('/', 1)[1]+ '\n' + '\n'.join('{}'.format(key) for key in dataStruct)
    return string


# Select File From The System
def selectFile():
    try:
        filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                              filetypes=(("json files", "*.json"), ("all files", "*.*")))
        return filename
    except FileNotFoundError as fe:
        print(fe)


# Console Display Method
def consoleDisplay(dataStruct, name, a, b):
    print("\n" + name)
    if type(dataStruct) is list:
        for i in dataStruct:
            # print(a + " " + str(i[0]) + "   ", b + " " + str(i[1]))
            print(i)

    elif type(dataStruct) is dict:
        for key, val in dataStruct.items():
            print(a + " " + key + "     " + b + " " + str(val))

# Naive Implementation Of Calculating Also Likes. Not Currently In Use.
# def calculateAlsoLikes(docsReadDict):
#     alsoLikesDict = {}
#     try:
#         for key, val in docsReadDict.items():
#             for i in val:
#                 if i not in alsoLikesDict:
#                     alsoLikesDict[i] = 0
#
#         for i in alsoLikesDict:
#             for key, val in docsReadDict.items():
#                 for j in val:
#                     if j == i:
#                         alsoLikesDict[j] += 1
#     except KeyError:
#         pass
#     print("\n***Also Likes Dictionary***")
#     for doc in alsoLikesDict.items():
#         print(doc)
#     return alsoLikesDict
