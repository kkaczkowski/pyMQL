import os

def start(fsource, fout):
    with open(fsource, 'r') as source:
        for line in source:
            if 'import "' in line:
                fsubsource = line.replace('import "', '').replace('"', '').strip()
                start(fsubsource, fout)
            else:
                fout.write(line)
    
    
def prepare_runtime(pyout):
    runtime = ['functions', 'dataset']
    with open(pyout, 'w') as pythoncode:
        for libname in runtime:
            libfile = os.path.join('lang', 'runtime', '%s.py' %libname)
            with open(libfile, 'r') as runtimefile:
                body = runtimefile.read()
                pythoncode.write('# *******  %s  *******\n' %libfile)
                pythoncode.write(body)
                pythoncode.write('\n')
        pythoncode.write('# *******   T R A N S L A T E   M Q L   *******\n')