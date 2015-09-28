stringi=[i for i in "abcdefghijklmnopqrstuvwxyz".lower()]
inp= raw_input()

for i in range(len(inp)):
    if(stringi):
        if(inp[i].lower() in stringi):
            stringi.remove(inp[i].lower())
if(stringi):
    print "pangram"
else: print "not pangram"
