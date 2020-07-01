from perfTabs import *
from outrankingDigraphs import *

t = PerformanceTableau('perfTab_9')

g = BipolarOutrankingDigraph(t,Normalized=True)
g.recodeValuation(-56,+56)
input('g.showHTMLRelationTable')
g.showHTMLRelationTable(ndigits=0)

input('g.computeChordlessCircuits')
g.computeChordlessCircuits()

input('g.showChordlessCircuits')
g.showChordlessCircuits()
