from perfTabs import *
from outrankingDigraphs import *
from perfTabs import PartialPerformanceTableau
from randomPerfTabs import RandomCBPerformanceTableau
from performanceQuantiles import PerformanceQuantiles
from sortingDigraphs import NormedQuantilesRatingDigraph

h = PerformanceTableau('historicalData_9')
t = PerformanceTableau('perfTab_9')

pq = PerformanceQuantiles(h, numberOfBins=13,LowerClosed=True)
pq.showLimitingQuantiles(ByObjectives=True)
pq.updateQuantiles(t,historySize=None)
pq.showHTMLLimitingQuantiles(Transposed=True)

nqr = NormedQuantilesRatingDigraph(pq,t,rankingRule='best')
#nqr.showHTMLPerformanceTableau(actionsSubset=nqr.newActions)
nqr.showHTMLRatingHeatmap(Correlations=True,colorLevels=5)
nqr.showHTMLPerformanceTableau(actionsSubset=nqr.profiles)
nqr.exportGraphViz()
