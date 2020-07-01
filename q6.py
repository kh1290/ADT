from sparseOutrankingDigraphs import PreRankedOutrankingDigraph
from perfTabs import *
from outrankingDigraphs import *
from randomPerfTabs import RandomCBPerformanceTableau
from performanceQuantiles import PerformanceQuantiles
from sortingDigraphs import NormedQuantilesRatingDigraph

h = PerformanceTableau('historicalData_9')
t = PerformanceTableau('perfTab_9')
pq = PerformanceQuantiles(h, numberOfBins=13,LowerClosed=True)
pq.updateQuantiles(t,historySize=None)
nqr = NormedQuantilesRatingDigraph(pq,t,rankingRule='RankedPairs')

bg = PreRankedOutrankingDigraph(nqr,quantiles=3,LowerClosed=False)
bt = PreRankedOutrankingDigraph(t,quantiles=3)
best = PartialPerformanceTableau(t,bt.boostedRanking[:11])
best.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='RankedPairs',Correlations=True,Transposed=True)
