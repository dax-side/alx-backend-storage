#!/usr/bin/env python3
""" Pymongo collection object"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document into a collection"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
