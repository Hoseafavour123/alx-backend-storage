#!/usr/bin/env python3
""""Insert document in collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert new school and return id"""
    school = {}
    for k, v in kwargs.items():
        school[k] = v
    result = mongo_collection.insert(school)
    return result._id
