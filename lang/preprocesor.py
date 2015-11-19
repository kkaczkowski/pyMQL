
def start(fsource, fout):
    with open(fsource, 'r') as source:
        for line in source:
            if 'import "' in line:
                fsubsource = line.replace('import "', '').replace('"', '').strip()
                start(fsubsource, fout)
            else:
                fout.write(line)
    
    
