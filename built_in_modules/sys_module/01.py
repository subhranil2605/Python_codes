import sys


print(sys.version)


# stdin
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input: {line}')
print("Exit")


# stdout

