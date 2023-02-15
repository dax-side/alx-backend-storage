#!/usr/bin/env python3
""" pymongo list"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ return a list of documents from collection"""
    return list(mongo_collection.find({"topics": topic}))
