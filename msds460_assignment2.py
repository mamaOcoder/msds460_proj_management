from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, GLPK

# Define decision variables
tA = LpVariable("tA", 0, None)
tB = LpVariable("tB", 0, None)
tC = LpVariable("tC", 0, None)
tD1 = LpVariable("tD1", 0, None)
tD2 = LpVariable("tD2", 0, None)
tD3 = LpVariable("tD3", 0, None)
tD4 = LpVariable("tD4", 0, None)
tD5 = LpVariable("tD5", 0, None)
tD6 = LpVariable("tD6", 0, None)
tD7 = LpVariable("tD7", 0, None)
tD8 = LpVariable("tD8", 0, None)
tE = LpVariable("tE", 0, None)
tF = LpVariable("tF", 0, None)
tG = LpVariable("tG", 0, None)
tH = LpVariable("tH", 0, None)
z = LpVariable("z", 0, None)

# Define the problem for worstcase hours
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
prob_worst.solve()
print ("Status:", LpStatus[prob_worst.status])

for v in prob_worst.variables():
    print(v.name, "=", v.varValue)

print ("Objective Worst Case", value(prob_worst.objective))
print ("")

##########################################################
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
prob_exp.solve()
print ("Status:", LpStatus[prob_exp.status])

for v in prob_exp.variables():
    print(v.name, "=", v.varValue)

print ("Objective Expected", value(prob_exp.objective))
print ("")

##########################################################
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
prob_best.solve()
print ("Status:", LpStatus[prob_best.status])

for v in prob_best.variables():
    print(v.name, "=", v.varValue)

print ("Objective Best Case", value(prob_best.objective))
print ("")

