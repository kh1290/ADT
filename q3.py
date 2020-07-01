from perfTabs import *
from outrankingDigraphs import *
from perfTabs import PartialPerformanceTableau


t = PerformanceTableau('perfTab_9')

#####  Costs
input('Costs')
c = PartialPerformanceTableau(t,criteriaSubset=t.objectives['C']['criteria'])
c.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='RankedPairs',Correlations=True,Transposed=True)

#####  Benefits
input('Benefits')
b = PartialPerformanceTableau(t,criteriaSubset=t.objectives['B']['criteria'])
b.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='RankedPairs',Correlations=True,Transposed=True)

#####  Global
input('Global')
t.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='RankedPairs',Correlations=True,Transposed=True)
