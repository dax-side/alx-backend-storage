#!/usr/bin/env python3
""" pymongo list"""
import pymongo


def list_all(mongo_collection):
    """
        finds all documents form pymongo collection
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
