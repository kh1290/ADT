from perfTabs import *
t = PerformanceTableau('perfTab_9')
print(t)
input('NetFlows ranking')
t.showHTMLPerformanceHeatmap(Correlations=True,ndigits=0,colorLevels=5,
                             rankingRule='NetFlows',StoreRanking=True)
input('Copeland ranking')
t.showHTMLPerformanceHeatmap(Correlations=True,ndigits=0,colorLevels=5,
                             rankingRule='Copeland',StoreRanking=True)
input('Kohler ranking')
t.showHTMLPerformanceHeatmap(Correlations=True,ndigits=0,colorLevels=5,
                             rankingRule='Kohler',StoreRanking=True)

input('Fusion of NetFlows and Kohler rankings')
from transitiveDigraphs import *
rf = RankingsFusion(t,[t.netFlowsRanking,t.kohlerRanking])
rf.exportGraphViz(fileName='netFlowsKohlerFusion')
