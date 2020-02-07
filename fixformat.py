import sys
import re

if (len(sys.argv) != 3):
    print "Usage: ./sqir2circ <input file>"
    exit(-1)

inf = open(sys.argv[1])
outf = open(sys.argv[2], "w")

assert (inf.readline() == "OPENQASM 2.0;\n"), "Invalid file format."
assert (inf.readline() == "include \"qelib1.inc\";\n"), "Invalid file format."

inf.readline() # newline
m = re.match(r"qreg q\[([0-9]+)\];\n", inf.readline())
assert(m), "Invalid file format."
nqbits = int(m.group(1))
inf.readline() # newline

outf.write("\tdef t,0,'T'\n")
outf.write("\tdef tdg,0,'T^\\dagger'\n")
outf.write("\tdef s,0,'S'\n")
outf.write("\tdef sdg,0,'S^\\dagger'\n\n")

for i in range(nqbits):
    outf.write("\tqubit q%d\n" % i)
outf.write("\n")

for line in inf.readlines():
    m = re.match(r"cx q\[([0-9]+)\], q\[([0-9]+)\];\n", line)
    if m:
        outf.write("\tcnot q%s,q%s\n" % (m.group(1), m.group(2)))
        continue
    m = re.match(r"([a-zA-Z]+) q\[([0-9]+)\];\n", line)
    assert(m), "Invalid operation format: %s" % line
    outf.write("\t%s q%s\n" % (m.group(1), m.group(2)))


