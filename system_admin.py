import os,sys

# how to tell if the current os is windows?
if os.name in ('nt', 'dos'):
    error = "ERROR: Windows is not supported"
    print(error, file=sys.stderr)


#
