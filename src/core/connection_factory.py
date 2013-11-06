from pymongo import MongoClient


def create():
    client = MongoClient('localhost', 27017)
    return client.forum
