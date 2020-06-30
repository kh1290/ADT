from perfTabs import PerformanceTableau
from sortingDigraphs import QuantilesSortingDigraph

t = PerformanceTableau('perfTab_9')
qs = QuantilesSortingDigraph(t,limitingQuantiles=13,LowerClosed=False)
print(qs)
qs.showSorting()
