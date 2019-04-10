#!/usr/bin/python3
import sys

def main(inp, out):
    f = open(inp, "r")
    txt = f.read()
    f.close()
    l = txt.split("\n")
    d = dict()
    for line in l:
        line = line.strip()
        words = line.split("/")
        for word in words:
            for palabra in words:
                if palabra != word:
                    if word in d.keys():
                        if palabra not in d[word]:
                            d[word].append(palabra)
                    else:
                        d[word] = [palabra]
    g = open(out, "w")
    for key in d.keys():
        g.write(key + ',')
        g.write(",".join(d[key]))
        g.write("\n")
print("hello world\n")         
main(sys.argv[1], sys.argv[2])
