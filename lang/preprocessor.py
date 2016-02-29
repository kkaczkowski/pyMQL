# -*- coding: utf-8 -*-

import os, codecs
import config.config as config

def start(fsource, fout):
    print('Preprocessor load <%s>' %fsource)
    with codecs.open(fsource, 'r', encoding='utf8') as source:
        for line in source:
            if not line.strip().startswith('#') and 'import "' in line:
                fsubsource = line.replace('import "', '').replace('"', '').strip()
                start(fsubsource, fout)
            else:
                fout.write(line)
    
    
def prepare_runtime(pyout):
    runtime = ['functions', 'outcsv', 'dbconnection', 'dataset']
    with open(pyout, 'w') as pythoncode:
        pythoncode.write('%s\n' %config.config['python'])
        
        for libname in runtime:
            libfile = os.path.join('lang', 'runtime', '%s.py' %libname)
            with open(libfile, 'r') as runtimefile:
                body = runtimefile.read()
                pythoncode.write('# *******  %s  *******\n' %libfile)
                pythoncode.write(body)
                pythoncode.write('\n')
        pythoncode.write('# *******   T R A N S L A T E   M Q L   *******\n\n')
