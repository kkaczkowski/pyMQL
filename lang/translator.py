import argparse

class MQLToPython(argparse.Action):
    
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(MQLToPython, self).__init__(option_strings, dest, **kwargs)
        
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)
