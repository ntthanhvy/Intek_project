import sys
import os


length = len(sys.argv)


def replace_all(line, d):
    for k, v in d:
        line = line.replace(k, v)
    return line


def change_word_case(pattern, line):
    w = line.slipt(pattern)
    d = {}
    for k in range(len(w) - 1):
        i = line.index(pattern, len(w[k]))
        word = '\33[30;43' + linne[i: len(pattern) + i] + '\33[0m'
        d.update({line[i: len(pattern) + i]: word})
    r = replace_all(line, d)
    return r


def main():
    if '--hidden' in sys.argv:
        for r, ds, fs in os.walk('.'):
            for f in fs:
                path = os.path.join(r, f)
                if 'ag.py' not in path:
                    print('\33[1;32m' + path + '\33[0m')
                    w = sys.argv[-1].lower()
                    file = open(path, 'r')
                    x = 1
                    for line in file:
                        a = line.lower()
                        if w in a:
                            a = a.split(w)
                            print(a)
                            print('\33[1;33m' + str(x) + '\33[0m' + ":", end ="")
                            for i in range(len(a) - 1):
                                j = line.lower().index(w, len(a[i]))
                                print(line[0: len(a[i]) - 1], end="")
                                print('\33[33;43' + line[j: j + len(w)] + '\33[0m', end="")
                            print(line[-1 - len(a) - 1: -1], end="")
                        x += 1




main()
