#!/usr/bin/env python3
"""
This script contains a function that updates a document
in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a school
    document based on the name:
    """
    return mongo_collection.update_many(
            {"name": name}, {'$set': {"topics": topics}}
            )
