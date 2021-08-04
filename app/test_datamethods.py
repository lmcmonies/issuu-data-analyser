#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import unittest

import datamethods as methods
import test_data as data
import fileIO


# test_datamethods.py Provides Unit Tests For Each Of The Methods In datamethods.py
class TestDataMethods(unittest.TestCase):

    # Task 2a

    # Tests generateCountriesList method
    def test_generateCountriesList(self):
        documentId, countriesList = data.generateCountriesListData()
        result = methods.generateCountriesList(documentId, fileIO.loadFile('sample.json'))
        self.assertTrue(result == countriesList)

    # Tests generateCountriesDict method.
    def test_generateCountriesDict(self):
        countriesDict, countriesList, calculatedCountriesDict, bogusCountriesDict = data.generateCountriesDictData()
        result = methods.generateCountriesDict(countriesDict, countriesList)
        self.assertTrue(result == calculatedCountriesDict)
        self.assertTrue(result != bogusCountriesDict)

    # Tests filterCountriesDict method.
    def test_filterCountriesDict(self):
        countriesDict, filteredCountriesDict = data.filterCountriesDictData()
        result = methods.filterCountriesDict(countriesDict)
        self.assertTrue(result == filteredCountriesDict)

    # Task 2b

    # Tests generateContinentsDict method.
    def test_generateContinentsDict(self):
        filteredCountriesDict, countriesInContinentsDict, continentsDict, generatedContinentsDict = \
            data.generateContinentsDictData()
        result = methods.generateContinentsDict(filteredCountriesDict, countriesInContinentsDict, continentsDict)
        self.assertTrue(result == generatedContinentsDict)

    # Tests filterContinentsDict method.
    def test_filterContinentsDict(self):
        continentsDict, filteredContinentsDict = data.filterContinentsDictData()
        result = methods.filterContinentsDict(continentsDict)
        self.assertTrue(result == filteredContinentsDict)

    # Task 3a

    # Tests generateBrowserListAndDictV1 method.
    def test_generateBrowserListAndDictV1(self):
        browserListDictTuple = data.generateBrowserListAndDictV1Data()
        result = methods.generateBrowserListAndDictV1(fileIO.loadFile('sample.json'))
        self.assertTrue(result == browserListDictTuple)

    # Task 3b

    # Tests generateBrowserListAndDictV2 method.
    def test_generateBrowserListAndDictV2(self):
        browserListDictTuple = data.generateBrowserListAndDictV2Data()
        result = methods.generateBrowserListAndDictV2(fileIO.loadFile('sample.json'))
        self.assertTrue(result == browserListDictTuple)

    # Tests calculateBrowserDict method.
    def test_calculateBrowserDict(self):
        browserDict, bList, calculatedBrowserDict = data.calculateBrowserDictData()
        result = methods.calculateBrowserDict(browserDict, bList)
        self.assertTrue(result == calculatedBrowserDict)

    # Task 4

    # Tests generateVisitorsDict method.
    def test_generateVisitorsDict(self):
        visitorsDict = data.generateVisitorsDictData()
        result = methods.generateVisitorsDict(fileIO.loadFile('sample.json'))
        self.assertTrue(result == visitorsDict)

    # Tests calcReadTime method.
    def test_calcReadTime(self):
        readTimeDict, calculatedReadTimeDict = data.calcReadTimeData()
        result = methods.calcReadTime(fileIO.loadFile('sample.json'), readTimeDict)
        self.assertTrue(result == calculatedReadTimeDict)

    # Tests determineTop10Readers method.
    def test_determineTop10Readers(self):
        readTimeDict, top10Readers = data.determineTop10ReadersData()
        result = methods.determineTop10Readers(readTimeDict)
        self.assertTrue(result == top10Readers)

    # Task 5

    # Tests generateReadersList method.
    def test_generateReadersList(self):
        documentId, visitorId, json, readersList = data.generateReadersListData()
        result = methods.generateReadersList(documentId, visitorId, json)
        self.assertTrue(result == readersList)

    # Tests constructDocDict method.
    def test_constructDocDict(self):
        documentId, readersList, json, docsReadDict = data.constructDocDictData()
        result = methods.constructDocDict(json, readersList, documentId)
        self.assertTrue(result == docsReadDict)

    # Tests calcAlsoLikes method.
    def test_calcAlsoLikes(self):
        docsReadDict, alsoLikesList = data.calcAlsoLikesData()
        result = methods.calcAlsoLikes(docsReadDict)
        self.assertTrue(result == alsoLikesList)

    # Tests count method.
    def test_count(self):
        documentId, docsReadDict, num = data.countData()
        result = methods.count(documentId, docsReadDict)
        self.assertTrue(result == num)

    # Tests determineTop10AlsoLikeDocs method.
    def test_determineTop10AlsoLikesDocs(self):
        alsoLikesList, top10AlsoLikes = data.determineTop10AlsoLikesDocsData()
        result = methods.determineTop10AlsoLikeDocs(alsoLikesList)
        self.assertTrue(result == top10AlsoLikes)

    # Helper Methods

    # Tests resetDictionaryValues method.
    def test_resetDictionaryValues(self):
        continentsDict, continentsDictReset = data.resetDictionaryValuesData()
        result = methods.resetDictionaryValues(continentsDict)
        self.assertTrue(result == continentsDictReset)


