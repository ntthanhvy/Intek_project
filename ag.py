import sys
if len(sys.argv) == 3:
    s = sys.argv[1].lower()
    file = open(sys.argv[2], "r")
    x = 1
    for line in file:
        a = line.lower()
        if s in a:
            k = 0
            a = a.split(s)
            print('\033[1;33m' + str(x) + '\033[0m' + ":", end="")
            for i in range(len(a) - 1):
                print(line[k: k + len(a[i])], end="")
                k += len(a[i])
                print('\33[30;43m' + line[k:k + len(s)] + '\33[0m', end="")
                k += len(s)
            print(line[k: k + len(a[len(a) - 1])], end="")
        x += 1

else:
    s = sys.argv[2]
    file = open(sys.argv[3], "r")
    x = 1
    for line in file:
        if s in line:
            k = 0
            a = line.split(s)
            print('\033[1;33m' + str(x) + '\033[0m' + ":", end="")
            for i in range(len(a) - 1):
                print(line[k: k + len(a[i])], end="")
                k += len(a[i])
                print('\33[30;43m' + line[k:k + len(s)] + '\33[0m', end="")
                k += len(s)
            print(line[k: k + len(a[len(a) - 1])], end="")
        x += 1
