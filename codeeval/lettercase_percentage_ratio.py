import sys

with open(sys.argv[1], "r") as f:
    for line in f:
        upper, line = 0.0, line.rstrip()
        for c in line:
            if c.isupper():
                upper += 1
        print "lowercase: %2.2f uppercase: %2.2f" % \
              (((len(line) - upper) / len(line))*100, (upper / len(line)) * 100)
