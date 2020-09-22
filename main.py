import sys

import airfoil

if len(sys.argv) < 2:
    print("Usage:")
    print("    $ python %s <airfoil_data_directory>" %
          sys.argv[0])
    sys.exit(0)

input_dir = sys.argv[1]

try:
    a = airfoil.Airfoil(input_dir)
except RuntimeError as e:
    print("ERROR: %s" % e)
    sys.exit(2)

print(a)
    
