import sys

# argument exception.
if 3 > len(sys.argv):
    print(f"not enough argument : {len(sys.argv)}")
    sys.exit()

# file exception.
file = [s for s in sys.argv[1:] if '.txt' in s]
print(file[0])
if not file or 1 < len(file):
    print(f"input filename exactly include name. now.. {sys.argv}")
    sys.exit()

# op exception.
op = [s for s in sys.argv if '-' in s]

if 2 <= len(op):
    print(f"only one '-' option. now.. {op}")
    sys.exit()

if not op:
    print(f"can't process '-' option;; now.. {sys.argv}")
    sys.exit()

if 1 != len(op) or op[0] not in ['-w', '-a', '-r']:
    print(f"wrong in option argument. (e ex) '-w', '-r', '-a') now.. : {op}")
    sys.exit()

# change compare char.
op = op[0][1]

# str exception.
# ...

str = sys.argv[-1]

with open(f"{file[0]}", op) as f:
    if 'w' == op or 'a' == op:
        print('this write : ', str)
        f.write(str + ' ')

    if 'r' == op:
        print(f.read())
