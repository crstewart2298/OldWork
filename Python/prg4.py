##############################################
# CSC 246 - Fall 2019
# Missouri Western State University
# Homework #4 - Logic Programming
# Starter Template 
# Student(s): 

from kanren import *

allgoals = []   # goals used to solve the logic puzzle


def anon_employee():
  return (var(), var(), var())

def set_fname(employee, name):
  return (name, employee[1], employee[2])

def set_lname(employee, name):
  return (employee[0], name, employee[2])

def set_job(employee, job):
  return (employee[0], employee[1], job)

pm1 = set_job(anon_employee(), "product manager")
pm2 = set_job(anon_employee(), "product manager")
pw1 = set_job(anon_employee(), "publications writer")
ae1 = set_job(anon_employee(), "applications engineer")
ae1 = set_lname(ae1, "fairview")
ma1 = set_job(anon_employee(), "marketing analyst")
ma1 = set_lname(ma1,"radcliffe")
mm1 = set_job(anon_employee(), "marketing manager")

pm = (pm1,pm2)
ae = (ae1)
ma = (ma1)
mm = (mm1)
pw = (pw1)

c1 = set_lname(anon_employee(),"chase")
r1 = set_lname(anon_employee(), "radcliffe")
f1 = set_lname(anon_employee(), "fairview")
m1 = set_lname(anon_employee(), "macklin")
w1 = set_lname(anon_employee(), "weathervane")
w1 = set_fname(w1, "ellen")
s1 = set_lname(anon_employee(), "singer")
s1 = set_fname(s1, "amelia")

chase = (c1)
radcliffe = (r1)
fairview = (f1)
macklin = (m1)
singer = (s1)
weathervane = (w1)

curtis = set_fname(anon_employee(), "curtis")

steve = set_fname(anon_employee(), "steve")
steve = set_job(steve,"publications writer")
allgoals.append(membero(steve, pw))

dick = set_fname(anon_employee(), "dick")

ellen = set_fname(anon_employee(), "ellen")
ellen = set_lname(ellen, "weathervane")

harriet = set_fname(anon_employee(), "harriet")

amelia = set_fname(anon_employee(), "amelia")
amelia = set_lname(amelia, "singer")

wallseats = (curtis,steve,ellen)	# employees with seats by the wall
windowseats = (amelia, harriet, dick)	# employees with seats by the window
employees = (curtis,dick,steve,ellen,harriet,amelia)	# all employees (same vars)


def has_wall_seat(employee):
  """produces a goal expecting the employee to have a wall seat"""
  return (membero, employee, wallseats)
def has_window_seat(employee):
  """produces a goal expecting the employee to have a window seat"""
  return (membero, employee, windowseats)
def is_employee(employee):
  """produces a goal asserting that 'employee' is one of the six employees in question"""
  return (membero, employee, employees)
def is_male(employee):
  """produces a goal asserting that the employee has one of the male first names"""
  return (lany, 
            is_employee(set_fname(employee, "steve")),
            is_employee(set_fname(employee, "curtis")),
            is_employee(set_fname(employee, "dick")))
def is_female(employee):
  """produces a goal asserting that the employee has one of the female first names"""
  return (lany, 
            is_employee(set_fname(employee, "ellen")),
            is_employee(set_fname(employee, "amelia")),
            is_employee(set_fname(employee, "harriet")))

allgoals.append(is_employee(steve))
allgoals.append(is_employee(dick))
allgoals.append(is_employee(curtis))
allgoals.append(is_employee(ellen))
allgoals.append(is_employee(amelia))
allgoals.append(is_employee(harriet))

allgoals.append(is_male(dick))
allgoals.append(is_male(steve))
allgoals.append(is_male(curtis))
allgoals.append(is_male(pm1))
allgoals.append(is_female(ellen))
allgoals.append(is_female(amelia))
allgoals.append(is_female(harriet))
allgoals.append(is_female(pm2))
"""***********************************************************************************"""

def is_steve_lname(employee):
  """produces a goal asserting that steve has one of his possible last names"""
  return (lall(
            is_employee(set_lname(employee, "macklin")),
            membero(steve, macklin)))
def is_curtis_lname(employee):
  """produces a goal asserting that curtis has one of his possible last names"""
  return (lall( 
            is_employee(set_lname(employee, "radcliffe")),
            membero(curtis, radcliffe)))
def is_dick_lname(employee):
  """produces a goal asserting that dick has one of his possible last names"""
  return (lany(lall( 
            is_employee(set_lname(employee, "radcliffe")),
            membero(dick, radcliffe)),lall(
            is_employee(set_lname(employee, "chase")),
            membero(dick, chase)), lall(
            is_employee(set_lname(employee, "fairview")),
            membero(dick, fairview))))
def is_harriet_lname(employee):
  """produces a goal asserting that harriet has one of her possible last names"""
  return (lany(lall(
            is_employee(set_lname(employee, "radcliffe")),
            membero(harriet, radcliffe)), lall(
            is_employee(set_lname(employee, "fairview")),membero(harriet, fairview))))

allgoals.append(is_steve_lname(steve))
allgoals.append(is_curtis_lname(curtis))
allgoals.append(is_dick_lname(dick))
allgoals.append(is_harriet_lname(harriet))

"""***********************************************************************************"""

def is_ellen_job(employee):
  """produces a goal asserting that ellen has one of her possible jobs"""
  return (lany(lall(
                is_employee(set_job(employee, "product manager")),
                membero(ellen, pm)),lall(
                is_employee(set_job(employee, "market analyst")),
                membero(ellen, ma)),lall(
                is_employee(set_job(employee, "applications engineer")),
                membero(ellen,ae))))
def is_harriet_job(employee):
  """produces a goal asserting that harriet has one of her possible jobs"""
  return (lany(lall(
                is_employee(set_job(employee, "market analyst")),
                membero(harriet, ma)),lall(
                is_employee(set_job(employee, "applications engineer")),
                membero(harriet,ae))))
def is_amelia_job(employee):
  """produces a goal asserting that amelia has one of her possible jobs"""
  return (lany(lall(
                is_employee(set_job(employee, "market manager")),
                membero(amelia, mm)),lall(
                is_employee(set_job(employee, "market analyst")),
                membero(amelia, ma))))
def is_dick_job(employee):
  """produces a goal asserting that dick has one of his possible jobs"""
  return (lany(lall(
                is_employee(set_job(employee, "product manager")),
                membero(dick, pm)),lall(
                is_employee(set_job(employee, "market analyst")),
                membero(dick, ma))))
def is_curtis_job(employee):
  """produces a goal asserting that curtis has one of his possible jobs"""
  return(lall(
    is_employee(set_job(employee, "market analyst")),
                membero(curtis, ma)))
          
allgoals.append(is_ellen_job(ellen))
allgoals.append(is_amelia_job(amelia))
allgoals.append(is_harriet_job(harriet))
allgoals.append(is_dick_job(dick))
allgoals.append(is_curtis_job(curtis))

# TODO: nothing to change here, but consider setting the number of solutions to find to 1 
# if you want your program to run quickly for testing! A setting of 0 will determine if you're 
# 100% correct or not, but it may take a long time (or literally forever if you're wrong). 
print("**********************************")
results = run(0, (wallseats, windowseats), (lall,) + tuple(allgoals))
results = set(map(lambda x: (frozenset(x[0]), frozenset(x[1])), results))  # eliminate duplicates
for (walls, windows) in results:
  print("wall seats: ")
  for employee in walls:
    print(employee)
  print("window seats: ")
  for employee in windows:
    print(employee)
  print("-----------")

print("number of results: " + str(len(results)))
