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



curtis = set_fname(anon_employee(), "curtis")
steve = set_fname(anon_employee(), "steve")
dick = set_fname(anon_employee(), "dick")
ellen = set_fname(anon_employee(), "ellen")
harriet = set_fname(anon_employee(), "harriet")
amelia = set_fname(anon_employee(), "amelia")

employees = (curtis,dick,steve,ellen,harriet,amelia)

wallseats= (curtis, employee, employee)

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
