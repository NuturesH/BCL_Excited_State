#First write a model order
#Second according filename to write order
class B_H:
    def __init__(self, INF, OUTF):
        self.INF = INF 
        self.OUTF = OUTF
    def opt_h(self):
        import os
        INF = self.INF
        OUTF = self.OUTF
        fp = open(OUTF, 'w')
        for name in open(INF):
            name = name.strip().split('.pdb')[0]
            print name
            rst_order = "sander -O -i min.in -o {0}.out -p {0}.promtop -c {0}.inpcrd -r {0}.rst ".format(name)
            pdb_order = "ambpdb -p {0}.promtop <{0}.rst> {0}_OPT.pdb".format(name)
            print >> fp, rst_order
            print >> fp, pdb_order
        fp.close()
