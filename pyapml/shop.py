# Collection of functions for decision trees
# FIXME! Re-implement as class
# AUTHOR Sven Schrodt
# SINCE 2025-11-11
# 
# BibTeX citation
#
# @misc{clickstream_data_for_online_shopping_553,
#   title        = {{Clickstream Data for Online Shopping}},
#   year         = {2019},
#   howpublished = {UCI Machine Learning Repository},
#   note         = {{DOI}: https://doi.org/10.24432/C5QK7X}
# }

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

class Shop:

    ctry = None
    color = None
    photo_loc = None
    photo_type = None

    def __init__(self):
        self.init()

    def init(self):

        self.ctry = {
            "1": "Australia",
            "2": "Austria",
            "3": "Belgium",
            "4": "British Virgin Islands",
            "5": "Cayman Islands",
            "6": "Christmas Island",
            "7": "Croatia",
            "8": "Cyprus",
            "9": "Czech Republic",
            "10": "Denmark",
            "11": "Estonia",
            "12": "unidentified",
            "13": "Faroe Islands",
            "14": "Finland",
            "15": "France",
            "16": "Germany",
            "17": "Greece",
            "18": "Hungary",
            "19": "Iceland",
            "20": "India",
            "21": "Ireland",
            "22": "Italy",
            "23": "Latvia",
            "24": "Lithuania",
            "25": "Luxembourg",
            "26": "Mexico",
            "27": "Netherlands",
            "28": "Norway",
            "29": "Poland",
            "30": "Portugal",
            "31": "Romania",
            "32": "Russia",
            "33": "San Marino",
            "34": "Slovakia",
            "35": "Slovenia",
            "36": "Spain",
            "37": "Sweden",
            "38": "Switzerland",
            "39": "Ukraine",
            "40": "United Arab Emirates",
            "41": "United Kingdom",
            "42": "USA",
            "43": "biz (*.biz)",
            "44": "com (*.com)",
            "45": "int (*.int)",
            "46": "net (*.net)",
            "47": "org (*.org)"
        }

        self.color = {
            "1": "beige",
            "2": "black",
            "3": "blue",
            "4": "brown",
            "5": "burgundy",
            "6": "gray",
            "7": "green",
            "8": "navy blue",
            "9": "of many colors",
            "10": "olive",
            "11": "pink",
            "12": "red",
            "13": "violet",
            "14": "white"
        }

        self.photo_loc = {
            "1": "top left",
            "2": "top in the middle",
            "3": "top right",
            "4": "bottom left",
            "5": "bottom in the middle",
            "6": "bottom right"
        }

        self.photo_type = {
            "1": "en face",
            "2": "profile"
        }