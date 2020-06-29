from perfTabs import *
from outrankingDigraphs import *

t = PerformanceTableau('perfTab_9')

g = BipolarOutrankingDigraph(t,Normalized=True)
g.recodeValuation(-56,+56)
g.showHTMLRelationTable(ndigits=0)

g.computeChordlessCircuits()
g.showChordlessCircuits()
