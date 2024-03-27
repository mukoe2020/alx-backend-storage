#!/usr/bin/env python3
"""
Module that uses pymongo to list documents
in a collection
"""


def list_all(mongo_collection):
    """
    a Python function that lists all documents in a collection
    """
    docs = mongo_collection.find()
    return docs
