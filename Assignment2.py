from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, GLPK

# Define decision variables
tA = LpVariable("Describe product", 0, None)
tB = LpVariable("Develop marketing strategy", 0, None)
tC = LpVariable("Design brochure", 0, None)
tD1 = LpVariable("Requirements analysis", 0, None)
tD2 = LpVariable("Software design", 0, None)
tD3 = LpVariable("System design", 0, None)
tD4 = LpVariable("Coding", 0, None)
tD5 = LpVariable("Write documentation", 0, None)
tD6 = LpVariable("Unit testing", 0, None)
tD7 = LpVariable("System testing", 0, None)
tD8 = LpVariable("Package deliverables", 0, None)
tE = LpVariable("Survey potential market", 0, None)
tF = LpVariable("Develop pricing plan", 0, None)
tG = LpVariable("Develop implementation plan", 0, None)
tH = LpVariable("Write client proposal", 0, None)
z = LpVariable("Z", 0, None)

##########################################################
# Worst Case
# Define the problem
prob_worst = LpProblem("Assignment2_worstCase", LpMinimize)

# Define constraints
prob_worst += -tA + tC >= 3
prob_worst += -tA + tD1 >= 3
prob_worst += -tA + tG >= 3
prob_worst += -tB + tE >= 15
prob_worst += -tC + tE >= 4
prob_worst += -tD1 + tD2 >= 7
prob_worst += -tD1 + tD3 >= 7
prob_worst += -tD2 + tD4 >= 20
prob_worst += -tD3 + tD4 >= 15
prob_worst += -tD4 + tD5 >= 25
prob_worst += -tD4 + tD6 >= 25
prob_worst += -tD5 + tD8 >= 6
prob_worst += -tD6 + tD7 >= 12
prob_worst += -tD7 + tD8 >= 15
prob_worst += -tD8 + tF >= 4
prob_worst += -tD8 + tG >= 4
prob_worst += -tE + tF >= 7
prob_worst += -tF + tH >= 6
prob_worst += -tG + tH >= 5
prob_worst += -tH + z >= 3

# Define objective function
prob_worst += z

# Solve the problem
prob_worst.writeLP("output/prob_worst.lp")
prob_worst.solve()
print ("Status:", LpStatus[prob_worst.status])

for v in prob_worst.variables():
    print(v.name, "=", v.varValue)

print ("Objective Worst Case", value(prob_worst.objective))
print ("")

##########################################################
# Expected Case
# Define the problem for expected hours
prob_exp = LpProblem("Assignment2_expected", LpMinimize)

# Define constraints
prob_exp += -tA + tC >= 2
prob_exp += -tA + tD1 >= 2
prob_exp += -tA + tG >= 2
prob_exp += -tB + tE >= 10
prob_exp += -tC + tE >= 3
prob_exp += -tD1 + tD2 >= 5
prob_exp += -tD1 + tD3 >= 5
prob_exp += -tD2 + tD4 >= 14
prob_exp += -tD3 + tD4 >= 10
prob_exp += -tD4 + tD5 >= 18
prob_exp += -tD4 + tD6 >= 18
prob_exp += -tD5 + tD8 >= 4
prob_exp += -tD6 + tD7 >= 10
prob_exp += -tD7 + tD8 >= 12
prob_exp += -tD8 + tF >= 3
prob_exp += -tD8 + tG >= 3
prob_exp += -tE + tF >= 6
prob_exp += -tF + tH >= 4
prob_exp += -tG + tH >= 4
prob_exp += -tH + z >= 2

# Define objective function
prob_exp += z

# Solve the problem
prob_exp.writeLP("output/prob_exp.lp")
prob_exp.solve()
print ("Status:", LpStatus[prob_exp.status])

for v in prob_exp.variables():
    print(v.name, "=", v.varValue)

print ("Objective Expected", value(prob_exp.objective))
print ("")

##########################################################
# Best Case
# Define the problem for best case hours
prob_best = LpProblem("Assignment2_bestCase", LpMinimize)

# Define constraints
prob_best += -tA + tC >= 1
prob_best += -tA + tD1 >= 1
prob_best += -tA + tG >= 1
prob_best += -tB + tE >= 5
prob_best += -tC + tE >= 2
prob_best += -tD1 + tD2 >= 3
prob_best += -tD1 + tD3 >= 3
prob_best += -tD2 + tD4 >= 10
prob_best += -tD3 + tD4 >= 5
prob_best += -tD4 + tD5 >= 15
prob_best += -tD4 + tD6 >= 15
prob_best += -tD5 + tD8 >= 3
prob_best += -tD6 + tD7 >= 8
prob_best += -tD7 + tD8 >= 10
prob_best += -tD8 + tF >= 2
prob_best += -tD8 + tG >= 2
prob_best += -tE + tF >= 5
prob_best += -tF + tH >= 2
prob_best += -tG + tH >= 3
prob_best += -tH + z >= 1

# Define objective function
prob_best += z

# Solve the problem
prob_best.writeLP("output/prob_best.lp")
prob_best.solve()
print ("Status:", LpStatus[prob_best.status])

for v in prob_best.variables():
    print(v.name, "=", v.varValue)

print ("Objective Best Case", value(prob_best.objective))
print ("")

# Sensitivity Report
import subprocess
sen_worst = "glpsol --lp ./output/prob_worst.lp --ranges ./output/prob_worst.sen"
sen_exp = "glpsol --lp ./output/prob_exp.lp --ranges ./output/prob_exp.sen"
sen_best = "glpsol --lp ./output/prob_best.lp --ranges ./output/prob_best.sen"
subprocess.run(sen_worst, shell=True, check=True)
subprocess.run(sen_exp, shell=True, check=True)
subprocess.run(sen_best, shell=True, check=True)

##########################################################
# Best Case with Additional Contractor
prob_best_add = LpProblem("Assignment2_bestCase_Additional", LpMinimize)

# Define constraints
prob_best_add += -tA + tC >= 1
prob_best_add += -tA + tD1 >= 1
prob_best_add += -tA + tG >= 1
prob_best_add += -tB + tE >= 5
prob_best_add += -tC + tE >= 2
prob_best_add += -tD1 + tD2 >= 3
prob_best_add += -tD1 + tD3 >= 3
prob_best_add += -tD2 + tD4 >= 10
prob_best_add += -tD3 + tD4 >= 5
prob_best_add += -tD4 + tD5 >= 15
# Additional Contractor Reduce 5 hours of work
prob_best_add += -tD4 + tD6 >= 10
prob_best_add += -tD5 + tD8 >= 3
prob_best_add += -tD6 + tD7 >= 8
prob_best_add += -tD7 + tD8 >= 10
prob_best_add += -tD8 + tF >= 2
prob_best_add += -tD8 + tG >= 2
prob_best_add += -tE + tF >= 5
prob_best_add += -tF + tH >= 2
prob_best_add += -tG + tH >= 3
prob_best_add += -tH + z >= 1

# Define objective function
prob_best_add += z

# define objective function
prob_best_add += z
# solve the problem
prob_best_add.writeLP("output/prob_best_add.lp")
prob_best_add.solve()
print ("Status:", LpStatus[prob_best_add.status])

for v in prob_best_add.variables():
  print(v.name, "=", v.varValue)
print ("Objective Additional Contractor", value(prob_best_add.objective))
print ("")