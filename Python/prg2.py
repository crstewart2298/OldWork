def allsubsets(set):
	""" This module is a generator of subsets from a given set. These subsets are returned as frozensets"""
	x = len(set)
	for i in range(1 << x):#loops throught all combination lengths
		yield frozenset([set[j] for j in range(x) if (i & (1 << j))])
		#adds values to set until set reaches desired length
print("Test set 1: [1,2,3]")
print(list(allsubsets([1,2,3])))
print("Test set 2: [a,b,c]")
print(list(allsubsets(['a','b','c'])))
