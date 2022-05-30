##############################################
# CSC 246 - Fall 2019
##############################################
# CSC 246 - Fall 2019
# Missouri Western State University
# Homework #4 - Logic Programming
# Starter Template
# Student(s):

from kanren import *

cc1, cc2, ev1, ev2, pc1, pc2 = var(), var(), var(), var(), var(), var()
names = ['dr. crane', 'dr. grey', 'dr. demento', 'dr. farnsworth', 'dr. forrester']
curriculum_committee = (cc1, cc2)
evaluation_committee = (ev1, ev2)
promotion_committee = (pc1, pc2)
all_committee_members = (cc1, cc2, ev1, ev2, pc1, pc2)

allgoals = [
    membero('dr. grey', evaluation_committee),
    lany(
        lall(membero('dr. crane', evaluation_committee),
             membero('dr. crane', promotion_committee)),
        lall(membero('dr. crane', evaluation_committee),
             membero('dr. crane', curriculum_committee)),
        lall(membero('dr. crane', curriculum_committee),
             membero('dr. crane', promotion_committee))),
    lany(membero('dr. demento', curriculum_committee),
         membero('dr. demento', evaluation_committee)),
    membero('dr. farnsworth', all_committee_members),
    membero('dr. forrester', all_committee_members)
]

# TODO: nothing to change here, but consider setting the number of solutions to find to 1
# if you want your program to run quickly for testing! A setting of 0 will determine if you're
# 100% correct or not, but it may take a long time (or literally forever if you're wrong).
print("**********************************")
results = run(0, (curriculum_committee,
                  evaluation_committee,
                  promotion_committee) , (lall,) + tuple(allgoals))


results = frozenset(map(lambda t: (frozenset(t[0]), frozenset(t[1]), frozenset(t[2])), results))
for result in results:
    print(result)
print("number of results: " + str(len(results)))
