#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020

# countries.py Provides Dictionaries For Countries And Continents.
continentsDict = \
    {
        'AF': 0,
        'AN': 0,
        'AS': 0,
        'EU': 0,
        'NA': 0,
        'OC': 0,
        'SA': 0,
    }

countriesDict = \
    {
        'MX': 0, 'VE': 0, 'AR': 0, 'DZ': 0, 'AO': 0, 'BJ': 0, 'BW': 0, 'BF': 0, 'BI': 0, 'CM': 0, 'CV': 0, 'CF': 0,
        'TD': 0, 'KM': 0, 'DJ': 0, 'EG': 0, 'GQ': 0, 'ER': 0, 'ET': 0, 'GA': 0, 'GM': 0, 'GH': 0, 'GN': 0, 'GW': 0,
        'CI': 0, 'KE': 0, 'LS': 0, 'LR': 0, 'LY': 0, 'MG': 0, 'MW': 0, 'ML': 0, 'MR': 0, 'MU': 0, 'YT': 0, 'MA': 0,
        'MZ': 0, 'NA': 0, 'NE': 0, 'NG': 0, 'CG': 0, 'CD': 0, 'RE': 0, 'RW': 0, 'SH': 0, 'ST': 0, 'SN': 0, 'SC': 0,
        'SL': 0, 'SO': 0, 'ZA': 0, 'SS': 0, 'SD': 0, 'SZ': 0, 'TZ': 0, 'TG': 0, 'TN': 0, 'UG': 0, 'EH': 0, 'ZM': 0,
        'ZW': 0, 'AQ': 0, 'BV': 0, 'TF': 0, 'HM': 0, 'GS': 0, 'AF': 0, 'AM': 0, 'AZ': 0, 'BH': 0, 'BD': 0, 'BT': 0,
        'IO': 0, 'BN': 0, 'KH': 0, 'CX': 0, 'CC': 0, 'GE': 0, 'HK': 0, 'IN': 0, 'ID': 0, 'IR': 0, 'IQ': 0, 'IL': 0,
        'JP': 0, 'JO': 0, 'KZ': 0, 'KW': 0, 'KG': 0, 'LA': 0, 'LB': 0, 'MO': 0, 'MY': 0, 'MV': 0, 'MN': 0, 'MM': 0,
        'NP': 0, 'KP': 0, 'OM': 0, 'PK': 0, 'PS': 0, 'CN': 0, 'PH': 0, 'QA': 0, 'SA': 0, 'SG': 0, 'KR': 0, 'LK': 0,
        'SY': 0, 'TW': 0, 'TJ': 0, 'TH': 0, 'TR': 0, 'TM': 0, 'AE': 0, 'UZ': 0, 'VN': 0, 'YE': 0, 'AX': 0, 'AL': 0,
        'AD': 0, 'AT': 0, 'BY': 0, 'BE': 0, 'BA': 0, 'BG': 0, 'HR': 0, 'CY': 0, 'CZ': 0, 'DK': 0, 'EE': 0, 'FO': 0,
        'FI': 0, 'FR': 0, 'DE': 0, 'GI': 0, 'GR': 0, 'GG': 0, 'IS': 0, 'IE': 0, 'IM': 0, 'IT': 0, 'JE': 0, 'XK': 0,
        'LV': 0, 'LI': 0, 'LT': 0, 'LU': 0, 'MK': 0, 'MT': 0, 'MD': 0, 'MC': 0, 'ME': 0, 'NL': 0, 'NO': 0, 'PL': 0,
        'PT': 0, 'HU': 0, 'RO': 0, 'RU': 0, 'SM': 0, 'RS': 0, 'SK': 0, 'SI': 0, 'ES': 0, 'SJ': 0, 'SE': 0, 'CH': 0,
        'UA': 0, 'GB': 0, 'VA': 0, 'AI': 0, 'AG': 0, 'AW': 0, 'BS': 0, 'BB': 0, 'BZ': 0, 'BM': 0, 'BQ': 0, 'VG': 0,
        'CA': 0, 'KY': 0, 'CR': 0, 'CU': 0, 'CW': 0, 'DM': 0, 'SV': 0, 'GL': 0, 'GD': 0, 'GP': 0, 'GT': 0, 'HT': 0,
        'HN': 0, 'JM': 0, 'MQ': 0, 'MS': 0, 'NI': 0, 'PA': 0, 'PR': 0, 'BL': 0, 'KN': 0, 'LC': 0, 'MF': 0, 'PM': 0,
        'VC': 0, 'SX': 0, 'DO': 0, 'TT': 0, 'TC': 0, 'VI': 0, 'US': 0, 'AS': 0, 'AU': 0, 'CK': 0, 'TL': 0, 'FJ': 0,
        'PF': 0, 'GU': 0, 'KI': 0, 'MH': 0, 'FM': 0, 'NR': 0, 'NC': 0, 'NZ': 0, 'NU': 0, 'NF': 0, 'MP': 0, 'PW': 0,
        'PG': 0, 'PN': 0, 'WS': 0, 'SB': 0, 'TK': 0, 'TO': 0, 'TV': 0, 'UM': 0, 'VU': 0, 'WF': 0, 'BO': 0, 'BR': 0,
        'CL': 0, 'CO': 0, 'EC': 0, 'FK': 0, 'GF': 0, 'GY': 0, 'PY': 0, 'PE': 0, 'SR': 0, 'UY': 0,
    }

countriesInContinentsDict = \
    {
        'AF': ['DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA',
               'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'YT', 'MA', 'MZ',
               'NA', 'NE', 'NG', 'CG', 'CD', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ',
               'TZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW'],
        'AN': ['AQ', 'BV', 'TF', 'HM', 'GS'],
        'AS': ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'IO', 'BN', 'KH', 'CX', 'CC', 'GE', 'HK', 'IN', 'ID', 'IR', 'IQ',
               'IL', 'JP', 'JO', 'KZ', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'KP', 'OM', 'PK',
               'PS', 'CN', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TR', 'TM', 'AE', 'UZ', 'VN',
               'YE'],
        'EU': ['AX', 'AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE',
               'GI', 'GR', 'GG', 'IS', 'IE', 'IM', 'IT', 'JE', 'XK', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC',
               'ME', 'NL', 'NO', 'PL', 'PT', 'HU', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SJ', 'SE', 'CH', 'UA',
               'GB', 'VA'],
        'NA': ['AI', 'AG', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BQ', 'VG', 'CA', 'KY', 'CR', 'CU', 'CW', 'DM', 'SV', 'GL',
               'GD', 'GP', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MX', 'MS', 'NI', 'PA', 'PR', 'BL', 'KN', 'LC', 'MF', 'PM',
               'VC', 'SX', 'DO', 'TT', 'TC', 'VI', 'US'],
        'OC': ['AS', 'AU', 'CK', 'TL', 'FJ', 'PF', 'GU', 'KI', 'MH', 'FM', 'NR', 'NC', 'NZ', 'NU', 'NF', 'MP', 'PW',
               'PG', 'PN', 'WS', 'SB', 'TK', 'TO', 'TV', 'UM', 'VU', 'WF'],
        'SA': ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE']
    }



