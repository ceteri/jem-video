from thinkbayes import Pmf

pmf = Pmf()
pmf.Set("H1", 1 / 2.0)
pmf.Set("H2", 1 / 2.0)

pmf.Mult("H1", 30 / 40.0)
pmf.Mult("H2", 20 / 40.0)

pmf.Normalize()

for bowl in ["H1", "H2"]:
    print bowl, pmf.Prob(bowl)
