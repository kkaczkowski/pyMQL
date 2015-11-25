import csv

class OutCSV:
    
    def __init__(self, fname):
        csvfile = open(fname, 'w')
        self.csvfile = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
    def save(self, collection):
        if isinstance(collection[0], list) or isinstance(collection[0], tuple):
            self.csvfile.writerows(collection)
        else:
            self.csvfile.writerow(collection)
