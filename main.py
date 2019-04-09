#!/usr/bin/python3
import sys
import random
def wlen(filename):
	f = open(filename, 'r')
	str = f.read()
	l = str.split('\n')
	list = [0] * 26
	for i in l:
		list[len(i)]  += 1
	list[0] = 0
	return list

def wordslength(num, filename):
	f = open(filename, 'r')
	str = f.read()
	l = str.split('\n')
	s = set()
	for i in l:
		if len(i) == num:
			s.add(i)
	return s

def findcontainers(word, s):
        ret = []
        ctr = 0
        for palabra in s:
            if word in palabra and palabra != word + "s" and palabra != word + "ing" and palabra != word and palabra != word + "ed" and palabra != word + "est" and palabra != word + "ish" and palabra != word + "er":
                ret.append(palabra)
        return ret


def main(word):
    f = open("dictall.txt", 'r')
    str = f.read()
    f.close()
    l = str.split('\n')
    s = set()
    for i in l:
        s.add(i)
    while word not in s:
        word=input("Please choose a different word:\n")    
    b = findcontainers(word, s)
    ret = b[random.randrange(len(b))]
    ctr = ret.find(word)
    stop = ctr + len(word)
    noun = input("Give a singular noun associated with " + word + ":\n")
    while len(noun)==0:
            noun = input("Please give a valid noun:\n")
    verb = input("Give an action associated with " + ret + " (present tense):\n")
    while len(verb)==0:
            noun = input("Please give a valid verb:\n")
    ret = ret[0:ctr] + ret[ctr:stop].upper() + ret[stop:]
    print("How does a " + noun +  " " + verb + "?")
    print(ret)
    ans = input("save?(y/n)\n")
    if ans == 'y':
        g = open("puns.txt", "a")
        g.write("How does a " + noun +  " " + verb + "?\n")
        g.write(ret + "\n\n")
main(sys.argv[1])
