#!/usr/bin/env python3
"""
Script that contains a function for inserting a
new document within a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in a collection
    based on kwargs
    """
    new_col = mongo_collection.insert_one(kwargs)
    return new_col.inserted_id
