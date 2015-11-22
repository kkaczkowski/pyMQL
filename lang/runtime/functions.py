import random, os

genrandom = random.Random()
genrandom.seed(os.urandom(100))

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
    
    
def randomize(collection):
    if collection != None and len(collection) > 0:
        size = len(collection)
        num.randrange(0, size)
        return collection[num]
    return []


def Oracle(uri):
    pass


def PostgreSQL(uri):
    pass

