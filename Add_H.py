#First read pdb file name
#Second build new tleap file
#Three mod file
class AH: 
    def __init__(self, INF, modf, shf):
        self.INF = INF 
        self.modf = modf
        self.shf = shf 
    def NPDB(self):
        INF = self.INF
        modf = self.modf
        shf = self.shf
        fd = open(shf, 'w')
        for name in open(INF):
            name = name.strip()
            print name
            OUTF = name.replace(".pdb", "_H.pdb")
            TOPF = name.replace("pdb", "promtop")
            CRDF = name.replace("pdb", "inpcrd")
            TF = name.replace(".pdb", ".tleap")
            order = "tleap -f %s" %(TF)
            print >> fd , order
            print TF
            fp = open(TF, 'w')
            for line in open(modf):
                line= line.strip()
                line = line.replace('INpdb', name)
                line = line.replace('OUTpdb', OUTF)
                line = line.replace("promtop", TOPF)
                line = line.replace("inpcrd", CRDF)
                print >> fp, line 
            fp.close()
        fd.close()
