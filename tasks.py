#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import fileIO
import datamethods as methods
import countries as country
#import charts
import gui


# Task 2a: Views By Country
def task2a(fle, documentId):
    # Generate List of Countries
    countriesList = methods.generateCountriesList(documentId, fileIO.loadFile(fle))

    # Generate Countries Dictionary
    methods.generateCountriesDict(country.countriesDict, countriesList)

    # Filter Countries With Views Into New Dictionary
    filteredCountriesDict = methods.filterCountriesDict(country.countriesDict)

    # Reset Countries Dictionary Values
    methods.resetDictionaryValues(country.countriesDict)

    # Display Views By Country In Console
    methods.consoleDisplay(filteredCountriesDict, 'Views By Country...', 'Country:', 'Total Views:')

    # Display Bar Chart: Views By Country
    charts.barChart(filteredCountriesDict, 'Countries', 'Views', 'Views by Country')


# Task 2b: Views by Continent
def task2b(fle, documentId):
    # Generate List of Countries
    countriesList = methods.generateCountriesList(documentId, fileIO.loadFile(fle))

    # Generate Countries Dictionary
    methods.generateCountriesDict(country.countriesDict, countriesList)

    # Filter Countries With Views Into New Dictionary
    filteredCountriesDict = methods.filterCountriesDict(country.countriesDict)

    # Generate Dictionary Containing Views By Continent
    continentsViewsDict = methods.generateContinentsDict(filteredCountriesDict, country.countriesInContinentsDict,
                                                         country.continentsDict)
    # Filter Continents Dict
    filteredContinentsDict = methods.filterContinentsDict(continentsViewsDict)

    # Reset Countries Dictionary Values
    methods.resetDictionaryValues(country.countriesDict)

    # Reset Continents Dictionary Values
    methods.resetDictionaryValues(country.continentsDict)

    # Display Views By Continent In Console
    methods.consoleDisplay(filteredContinentsDict, 'Views By Continent...', 'Continent:', 'Total Views:')

    # Display Bar Chart: Views by Continents
    charts.barChart(filteredContinentsDict, 'Continents', 'Views', 'Views by Continent')


# Task3a: Views By Browser Full String
def task3a(fle):
    print("Generating Views By Browser...")
    # Generate A List And Dict For Browser
    browserList, browserDict = methods.generateBrowserListAndDictV1(fileIO.loadFile(fle))

    # generateView by Browser
    calculatedBrowserDict = methods.calculateBrowserDict(browserDict, browserList)

    # Display Views By Browser In Console
    methods.consoleDisplay(calculatedBrowserDict, 'Views By Browser...', 'Browser Type:', 'Total Views:')
    
    # Display Results In Bar Chart.
    charts.barChart(calculatedBrowserDict, 'Browsers', 'Views', 'Views by Browser')

    return calculatedBrowserDict


# Task3b: Views By Browser Refined
def task3b(fle):
    print("Generating Views By Browser")
    # Generate A List And Dict For Browser
    browserList, browserDict = methods.generateBrowserListAndDictV2(fileIO.loadFile(fle))

    # Calculate Views By Browser
    calculatedBrowserDict = methods.calculateBrowserDict(browserDict, browserList)

    # Display Views By Browser In Console
    methods.consoleDisplay(calculatedBrowserDict, 'Views By Browser...', 'Browser Type:', 'Total Views:')

    # Display Views By Browser In Bar Chart
    charts.barChart(calculatedBrowserDict, 'Browsers', 'Views', 'Views by Browser')

    return calculatedBrowserDict


# Task 4: Top 10 Readers By Read Time
def task4(fle):
    print('Generating Top 10 Readers...')

    # Create a dictionary containing all visitors
    visitorsDict = methods.generateVisitorsDict(fileIO.loadFile(fle))

    # Calculate read time for each object
    visitorsReadTimeDict = methods.calcReadTime(fileIO.loadFile(fle), visitorsDict)

    # Determine Top 10 users
    sortedTop10Readers = methods.determineTop10Readers(visitorsReadTimeDict)

    # Display Top 10 Readers
    methods.consoleDisplay(sortedTop10Readers, 'Top 10 Readers', 'Visitor Id:', 'Total Read Time In Milliseconds:')

    return sortedTop10Readers


# Task 5: Top 10 Also Likes
def task5d(documentId, visitorId, fle):
    print("Generating Top 10 Also Likes Documents...")
    # Generate Readers List.
    readersList = methods.generateReadersList(documentId, visitorId, fileIO.loadFileFiltered(fle))

    # Constructs Dictionary of Sets. Key: visitor_uuid, Value: set{subject_doc_id}.
    docsReadDict = methods.constructDocDict(fileIO.loadFileFiltered(fle), readersList, documentId)

    # Constructs Also Likes List
    alsoLikes = methods.calcAlsoLikes(docsReadDict)

    # Also Likes Passed In To Sorting Method. Sorted Into Top 10, Descending Order.
    top10AlsoLikes = methods.determineTop10AlsoLikeDocs(alsoLikes)

    # Displays Top 10 Also Likes Documents In Console.
    methods.consoleDisplay(top10AlsoLikes, '***Top 10 Also Likes Documents***', 'Document Id: ', 'Total Reads: ')

    return top10AlsoLikes, docsReadDict


# Generates A Graphviz Diagram For Also Likes.
def task6(documentId, visitorId, fle):
    top10AlsoLikes, docsReadDict = task5d(documentId, visitorId, fle)
    charts.graphDiagram(docsReadDict, documentId, visitorId)


# Task 7: Launches The GUI
def task7():
    # Launches The GUI
    gui.launchGUI()

