#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# Imports
import countries as country


# test_data.py Provides Data For Testing Purposes For The Methods In test_datamethods.py.

def generateCountriesListData():
    documentId = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
    countriesList = ['MX', 'MX']
    return documentId, countriesList


def generateCountriesDictData():
    countriesDict = {'MX': 0, 'VE': 0, 'AR': 0}
    countriesList = ['MX', 'MX']
    calculatedCountriesDict = {'MX': 2, 'VE': 0, 'AR': 0}
    bogusCountriesDict = {'VE': 0, 'AR': 0}
    return countriesDict, countriesList, calculatedCountriesDict, bogusCountriesDict


def filterCountriesDictData():
    countriesDict = {'MX': 2, 'VE': 0, 'AR': 0}
    filteredCountriesDict = {'MX': 2}
    return countriesDict, filteredCountriesDict


def generateContinentsDictData():
    filteredCountriesDict = {'MX': 2}
    countriesInContinentsDict = country.countriesInContinentsDict
    continentsDict = country.continentsDict
    generatedContinentsDict = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 2, 'OC': 0, 'SA': 0}
    return filteredCountriesDict, countriesInContinentsDict, continentsDict, generatedContinentsDict


def filterContinentsDictData():
    continentsDict = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 2, 'OC': 0, 'SA': 6}
    filteredContinentsDict = {'NA': 2, 'SA': 6}
    return continentsDict, filteredContinentsDict


def generateBrowserListAndDictV1Data():
    browserListDictTuple = (['Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 '
                             '(KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;'
                             'FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]',
                             'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 '
                             'Safari/537.36',
                             'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 '
                             '(KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;'
                             'FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]'
                                , 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'],
                            {'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 '
                             '(KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;'
                             'FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]': 0,
                             'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 '
                             'Safari/537.36'
                             : 0, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'
                             : 0
                             })
    return browserListDictTuple


def generateBrowserListAndDictV2Data():
    browserListDictTuple = (['Mozilla', 'Mozilla', 'Mozilla', 'Mozilla'], {'Mozilla': 0})
    return browserListDictTuple


def calculateBrowserDictData():
    browserDict = {'Mozilla': 0, 'Opera': 0, 'Dalvik': 0}
    bList = ['Mozilla', 'Opera', 'Mozilla', 'Dalvik']
    calculatedBrowserDict = {'Mozilla': 2, 'Opera': 1, 'Dalvik': 1}
    return browserDict, bList, calculatedBrowserDict


def generateVisitorsDictData():
    visitorsDict = {'745409913574d4c6': 0, '9a83c97f415601a6': 0, '64bf70296da2f9fd': 0}
    return visitorsDict


def calcReadTimeData():
    readTimeDict = {'745409913574d4c6': 0, '9a83c97f415601a6': 0, '64bf70296da2f9fd': 0}
    calculatedReadTimeDict = {'745409913574d4c6': 0, '9a83c97f415601a6': 0, '64bf70296da2f9fd': 797}
    return readTimeDict, calculatedReadTimeDict


def determineTop10ReadersData():
    readTimeDict = {'745409913574d4c6': 4567, '9a83c97f415601a6': 9284, '64bf70296da2f9fd': 836252,
                    '64bf70236da2f9fd': 73920, '745403213574d4c6': 928374, '9a83c45f415601a6': 93846,
                    '61bf70236da2f9fd': 0, '8b73c97f415601a6': 0, '745403216774d4c6': 0, '9a90c45f415601a6': 392727,
                    '745409953574d4c6': 0, '9a45c45f415601a6': 48272, '8b73c97f475681a6': 84837,
                    '61bf72236da2f9fd': 344565, '64bf70496da2f9fd': 493837, '745403303574d4c6': 309029,
                    '745409912374d4c6': 3454565, '745409913509d4c6': 34343, '745409913575f4c6': 234243
                    }
    top10Readers = [('745409912374d4c6', 3454565), ('745403213574d4c6', 928374),
                    ('64bf70296da2f9fd', 836252), ('64bf70496da2f9fd', 493837),
                    ('9a90c45f415601a6', 392727), ('61bf72236da2f9fd', 344565),
                    ('745403303574d4c6', 309029), ('745409913575f4c6', 234243),
                    ('9a83c45f415601a6', 93846), ('8b73c97f475681a6', 84837)]
    return readTimeDict, top10Readers


def generateReadersListData():
    documentId = '100806162735-00000000115598650cb8b514246272b5'
    visitorId = '00000000deadbeef'
    data = [{'visitor_uuid': '4108dc09bfe11aoc', 'subject_doc_id':
        '101122221951-00000000a695c340822e61891c8f14cf',
             'event_type': 'read'}, {'visitor_uuid': '4108dc09bfe11aoc', 'subject_doc_id':
        '100806162735-00000000115598650cb8b514246272b5',
                                     'event_type': 'read'}, {'visitor_uuid': '00000000deadbeef', 'subject_doc_id':
        '101122221951-00000000a695c340822e61891c8f14cf', 'event_type': 'read'},
            {'visitor_uuid': '00000000deadbeef', 'subject_doc_id':
                '100806162735-00000000115598650cb8b514246272b5', 'event_type': 'read'}]
    readersList = ['4108dc09bfe11aoc']
    return documentId, visitorId, data, readersList


def constructDocDictData():
    documentId = '100806162735-00000000115598650cb8b514246272b5'
    readersList = ['4108dc09bfe11aoc']
    data = [{'visitor_uuid': '4108dc09bfe11aoc', 'subject_doc_id':
        '101122221951-00000000a695c340822e61891c8f14cf',
             'event_type': 'read'}, {'visitor_uuid': '4108dc09bfe11aoc', 'subject_doc_id':
        '100806162735-00000000115598650cb8b514246272b5',
                                     'event_type': 'read'}, {'visitor_uuid': '00000000deadbeef', 'subject_doc_id':
        '101122221951-00000000a695c340822e61891c8f14cf', 'event_type': 'read'},
            {'visitor_uuid': '00000000deadbeef', 'subject_doc_id':
                '100806162735-00000000115598650cb8b514246272b5', 'event_type': 'read'}]
    docsReadDict = {'4108dc09bfe11aoc': {'101122221951-00000000a695c340822e61891c8f14cf'}}
    return documentId, readersList, data, docsReadDict


def calcAlsoLikesData():
    docsReadDict = {'4108dc09bfe11aoc': {'101122221951-00000000a695c340822e61891c8f14cf'}}
    alsoLikesList = [(1, '101122221951-00000000a695c340822e61891c8f14cf')]
    return docsReadDict, alsoLikesList


def countData():
    documentId = '101122221951-00000000a695c340822e61891c8f14cf'
    docsReadDict = {'4108dc09bfe11aoc': {'101122221951-00000000a695c340822e61891c8f14cf'}}
    num = 1
    return documentId, docsReadDict, num


def determineTop10AlsoLikesDocsData():
    alsoLikesList = [(1, '101122221951-00000000a695c340822e61891c8f14cf'),
                     (2, '102322221951-00000000a395c340822e61891d2f14cf'),
                     (8, '102329621954-00000000a795c340922f61891d2f14cf'),
                     (1, '101122221959-00000000a695c340822e61891c8f14jh'),
                     (6, '102322221953-00000000a395c340822e61891d2f14er'),
                     (3, '102329621957-00000000a795c340922f61891d2f14dk'),
                     (2, '101122221951-00000200a695c340822e61891c8f14cf'),
                     (12, '102322221951-00007000a395c340822e61891d2f14cf'),
                     (5, '102329621954-00000900a795c340922f61891d2f14cf'),
                     (4, '101122221959-00000400a695c340822e61891c8f14jh'),
                     (18, '102322221953-00000600a395c340822e61891d2f14er'),
                     (9, '102329621957-00040000a795c340922f61891d2f14dk')
                     ]
    top10AlsoLikes = [(18, '102322221953-00000600a395c340822e61891d2f14er'),
                      (12, '102322221951-00007000a395c340822e61891d2f14cf'),
                      (9, '102329621957-00040000a795c340922f61891d2f14dk'),
                      (8, '102329621954-00000000a795c340922f61891d2f14cf'),
                      (6, '102322221953-00000000a395c340822e61891d2f14er'),
                      (5, '102329621954-00000900a795c340922f61891d2f14cf'),
                      (4, '101122221959-00000400a695c340822e61891c8f14jh'),
                      (3, '102329621957-00000000a795c340922f61891d2f14dk'),
                      (2, '102322221951-00000000a395c340822e61891d2f14cf'),
                      (2, '101122221951-00000200a695c340822e61891c8f14cf'),
                      ]
    return alsoLikesList, top10AlsoLikes


def resetDictionaryValuesData():
    continentsDict = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 2, 'OC': 0, 'SA': 6}
    continentsDictReset = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 0, 'OC': 0, 'SA': 0}
    return continentsDict, continentsDictReset


def displayToolData():
    label = 'Continents'
    fName = '/lm384/sample_100k_lines.json'
    dataStruct = {'AF': 0, 'AN': 0, 'AS': 0, 'EU': 0, 'NA': 2, 'OC': 0, 'SA': 6}
    string = 'Continents\nsample_100k_lines.json \n\nAF\nAN\nAS\nEU\nNA\nOC\nSA'

    return label, fName, dataStruct, string

