#!/usr/bin/env python3
"""
Contains a function that returns a list of documents
based on a certain criteria
"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school
    having a specific topic
    """
    same_topic = mongo_collection.find({"topic": topic})
    return same_topic
