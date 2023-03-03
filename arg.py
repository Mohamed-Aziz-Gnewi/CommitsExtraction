import sys

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', type(sys.argv[i]))