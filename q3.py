from perfTabs import *
from outrankingDigraphs import *
from perfTabs import PartialPerformanceTableau


t = PerformanceTableau('perfTab_9')

######  Costs
c = PartialPerformanceTableau(t,criteriaSubset=t.objectives['C']['criteria'])
c.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='best')

#####  Benefits
b = PartialPerformanceTableau(t,criteriaSubset=t.objectives['B']['criteria'])
b.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='best')

######  Global
t.showHTMLPerformanceHeatmap(colorLevels=5,rankingRule='best')
