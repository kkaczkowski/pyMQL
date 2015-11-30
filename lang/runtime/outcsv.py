# -*- coding: utf-8 -*-

import csv, codecs

class OutCSV:
    
    def __init__(self, fname):
        csvfile = codecs.open(fname, 'w', encoding='utf8') 
        self.csvfile = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        
    def save(self, collection):
        if isinstance(collection[0], list) or isinstance(collection[0], tuple):
            self.csvfile.writerows(collection)
        else:
            self.csvfile.writerow(collection)
