filename = 'demo.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))

lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n'
          for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)
