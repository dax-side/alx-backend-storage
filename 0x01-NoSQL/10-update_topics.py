#!/usr/bin/env python3
""" update document"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Updates dcuments in a colleciton"""
    qry = {"name": name}
    newvars = {"$set": {"topics": topics}}
    mongo_collection.update_many(qry, newvars)
