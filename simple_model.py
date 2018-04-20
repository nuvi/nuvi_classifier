#! /usr/bin/env python
from __future__ import division

import re
import os
import sys
import pickle

keywords = {
    "good": 110,
    "great": 160,
    "like": 208,
    "time": 52,
    # "would": 41,
    "should": 41,
    "would recommend": 10000,
    "really": 142,
    "come back": 323,
    # "get": 39,
    # "go": 35,
    "nice": 900,
    "best": 310,
    "well": 100,
    "always": 206,
    "love": 391,
    "little": 257,
    "staff": 784,
    "pretty": 799,
    "first": 2064,
    "never": 138,
    # "chicken": 1546,
    "friendly": 2784,
    "people": 62,
    "much": 298,
    "definitely": 2005,
    "restaurant": 1118,
    "recommend": 1699,
    "could": 71,
    "amazing": 2314,
    "better": 453,
    "experience": 1185,
    "order": 685,
    "come": 70,
    "around": 265,
    "right": 193,
    "delicious": 100000,
    "every": 172,
    "make": 45,
    "menu": 3113,
    "way": 84,
    "still": 126,
    "night": 209,
    "wait": 401,
    "minutes": 309,
    "ever": 281,
}

keyword_set = set(keywords.keys())

class Simple_Classifier:
    def __init__(self, min_number=2):
        self.min_number = min_number
        self.keywords = {
            "good": 110,
            "great": 160,
            "like": 208,
            "time": 52,
            # "would": 41,
            "should": 41,
            "would recommend": 10000,
            "really": 142,
            "come back": 323,
            # "get": 39,
            # "go": 35,
            "nice": 900,
            "best": 310,
            "well": 100,
            "always": 206,
            "love": 391,
            "little": 257,
            "staff": 784,
            "pretty": 799,
            "first": 2064,
            "never": 138,
            # "chicken": 1546,
            "friendly": 2784,
            "people": 62,
            "much": 298,
            "definitely": 2005,
            "restaurant": 1118,
            "recommend": 1699,
            "could": 71,
            "amazing": 2314,
            "better": 453,
            "experience": 1185,
            "order": 685,
            "come": 70,
            "around": 265,
            "right": 193,
            "delicious": 100000,
            "every": 172,
            "make": 45,
            "menu": 3113,
            "way": 84,
            "still": 126,
            "night": 209,
            "wait": 401,
            "minutes": 309,
            "ever": 281,
        }
        self.keyword_set = set(self.keywords.keys())

    def evaluate(self, X, Y):
        correct = 0
        for x, y in zip(X, Y):
            if self.predict(x) == y:
                correct += 1
        return (correct * 1.0) / len(X)

    def predict_all(self, X):
        return map(self.predict, X)

    def predict(self, x):
        tweet_set = set(x.split())
        shared_words = self.keyword_set & tweet_set
        return len(shared_words) >= self.min_number


# # simply enough words are feedback
# def number_of_keywords_classifier(tweet_text, min_number=2):
#     tweet_word_set = set(tweet_text.split())
#     shared_words = keyword_set & tweet_word_set

#     return len(shared_words) >= min_number


# # a certain percent of all words are feedback
# def percentage_keywords_classifier(tweet_text, min_percent=.05):
#     tweet_word_set = set(tweet_text.split())
#     shared_words = keyword_set & tweet_word_set

#     return len(shared_words) / len(tweet_word_set) >= min_percent


# classifier = number_of_keywords_classifier

# files = ["./feedback_files/%s" % x for x in os.listdir(
#     "./feedback_files") if os.path.splitext(x)[1] in [".txt", ]]


# files += ["./non_feedback_files/%s" % x for x in os.listdir(
#     "./non_feedback_files") if os.path.splitext(x)[1] in [".txt", ]]


# for fpath in files:
#     feedback = []
#     non_feedback = []
#     try:
#         for line in open(fpath, "r"):
#             if classifier(line):
#                 feedback.append(line)
#             else:
#                 non_feedback.append(line)
#         print fpath
#         print len(feedback), "/", len(non_feedback) + len(feedback)
#         percent_correct = len(feedback) / (len(non_feedback) + len(feedback))
#         print 1 - percent_correct if "non_" in fpath else percent_correct
#         print ""

#     except KeyboardInterrupt:
#         continue

# # files.reverse()
# # print files

# # print_and_write_keywords()


classifier = Simple_Classifier()

pickle.dump(classifier, open('simple_model.p', 'wb'))