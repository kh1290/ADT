from perfTabs import PerformanceTableau
from sortingDigraphs import QuantilesSortingDigraph

t = PerformanceTableau('perfTab_9')
qs = QuantilesSortingDigraph(t,limitingQuantiles=13,LowerClosed=False)

input('qs')
print(qs)

input('qs.showSorting')
qs.showSorting()

input('qs.showQuantileOrdering')
qs.showQuantileOrdering(strategy='average')
