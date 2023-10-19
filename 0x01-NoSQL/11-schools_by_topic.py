#!/usr/bin/env python3
"""search schools by topics"""


def schools_by_topic(mongo_collection, topic):
    """Search schools that match a topic"""
    return mongo_collection.find({"topics": topic})
