from randomPerfTabs import RandomCBPerformanceTableau
from outrankingDigraphs import *
from linearOrders import *


def Copeland(t, g):
    cop = CopelandRanking(g)
    cop.showRanking()
    corr = g.computeOrdinalCorrelation(cop)
    g.showCorrelation(corr)
    t.showHTMLPerformanceHeatmap(pageTitle='Copeland Ranking',actionsList=cop.copelandRanking,colorLevels=5,Correlations=True)
    t.showRankingConsensusQuality(cop.copelandRanking)

def NetFlows(t, g):
    nf = NetFlowsRanking(g)
    nf.showRanking()
    corr = g.computeOrdinalCorrelation(nf)
    g.showCorrelation(corr)
    t.showHTMLPerformanceHeatmap(pageTitle='NetFlows Ranking',colorLevels=5,Correlations=True)
    t.showRankingConsensusQuality(nf.netFlowsRanking)

def Kohler(t, g):
    ko = KohlerRanking(g)
    ko.showRanking()
    corr = g.computeOrdinalCorrelation(ko)
    g.showCorrelation(corr)
    t.showHTMLPerformanceHeatmap(pageTitle='Kohler Ranking',actionsList=ko.kohlerRanking,colorLevels=5,Correlations=True)
    t.showRankingConsensusQuality(ko.kohlerRanking)

def ArrowNRaynaud(t, g):
    ar = KohlerRanking((-g))
    ar.showRanking()
    corr = g.computeRankingCorrelation(ar.kohlerOrder)
    g.showCorrelation(corr)
    t.showHTMLPerformanceHeatmap(pageTitle='Arrow&Raynaud Ranking',actionsList=ar.kohlerOrder,colorLevels=5,Correlations=True)
    t.showRankingConsensusQuality(ar.kohlerOrder)

def RankedPairs(t, g):
    rp = RankedPairsRanking(g)
    rp.showRanking()
    corr = g.computeOrdinalCorrelation(rp)
    g.showCorrelation(corr)
    t.showHTMLPerformanceHeatmap(pageTitle='RankedPairs Ranking',actionsList=rp.rankedPairsRanking,colorLevels=5,Correlations=True) 
    t.showRankingConsensusQuality(rp.rankedPairsRanking)


if __name__ == "__main__":
    
    t = PerformanceTableau('perfTab_9')
    g = BipolarOutrankingDigraph(t,Normalized=True)

    input('Copeland') 
    Copeland(t, g)

    input('NetFlows') 
    NetFlows(t, g)

    input('Kohler') 
    Kohler(t, g)

    input('ArrowNRaynaud') 
    ArrowNRaynaud(t, g)

    input('RankedPairs') 
    RankedPairs(t, g)
