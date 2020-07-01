from perfTabs import *
from outrankingDigraphs import *
from perfTabs import PartialPerformanceTableau
from randomPerfTabs import RandomCBPerformanceTableau
from performanceQuantiles import PerformanceQuantiles
from sortingDigraphs import NormedQuantilesRatingDigraph

h = PerformanceTableau('historicalData_9')
t = PerformanceTableau('perfTab_9')

pq = PerformanceQuantiles(h, numberOfBins=13,LowerClosed=True)
input('pq.showLimitingQuantiles')
pq.showLimitingQuantiles(ByObjectives=True)
pq.updateQuantiles(t,historySize=None)
input('pq.showHTMLLimitingQuantiles')
pq.showHTMLLimitingQuantiles(Transposed=True)

nqr = NormedQuantilesRatingDigraph(pq,t,rankingRule='best')
input('nqr.showHTMLRatingHeatmap')
nqr.showHTMLRatingHeatmap(Correlations=True,colorLevels=5)
input('nqr.showHTMLPerformanceTableau')
nqr.showHTMLPerformanceTableau(actionsSubset=nqr.profiles)
nqr.exportGraphViz(graphType='pdf')
