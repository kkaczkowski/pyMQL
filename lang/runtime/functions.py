# -*- coding: utf-8 -*-

import random, os, logging
import pprint as nice

random.seed(os.urandom(100))
logging.basicConfig(handlers=[logging.FileHandler('mql.log'), 
                              logging.StreamHandler()], 
                              level=logging.DEBUG)

def count(collection):
    return len(collection)
    
    
def first(collection):
    if collection != None and len(collection) > 0:
        return collection[0]
    return []
    
    
def last(collection):
    if collection != None and len(collection) > 0:
        return collection[-1]
    return []


def choice(collection):
    return random.choice(collection) 

    
def sample(collection, count):
    size_collection = len(collection)
    if count > size_collection:
        logging.debug("function sample decrease limit from %s to %s" %(count, size_collection))
        count = size_collection
    return random.sample(collection, int(count))


def shuffle(collection):
    return random.shuffle(collection)

def pprint(collection):
    nice.pprint(collection)
