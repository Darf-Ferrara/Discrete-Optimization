#############################################################################
# JuMP
# An algebraic modelling langauge for Julia
# See http://github.com/JuliaOpt/JuMP.jl
#############################################################################
# knapsack.jl
#
# Solves a simple knapsack problem:
# max sum(p_j x_j)
# st sum(w_j x_j) <= C
# x binary
#############################################################################
using JuMP
# Maximization problem

InputData = readdlm("tmp.data")
numBins = Int(InputData[1,1])
m = Model()
@defVar(m, x[1:numBins], Bin)
profit = InputData[2:end,1]
weight = InputData[2:end,2]
capacity = InputData[1,2]

# Objective: maximize profit
@setObjective(m, Max, dot(profit, x))

# Constraint: can carry all
@addConstraint(m, dot(weight, x) <= capacity)

# Solve problem using MIP solver
status = solve(m)
IsSolved = status == :Optimal ? 1 : 0
BinUsed = int([getValue(x[i]) for i in 1:numBins])

println( string(int(getObjectiveValue(m))) * " " * string(IsSolved) * "\n" * replace(string(BinUsed)[2:(end-1)],","," "))
#println("Solution is:")
#println(string(int(x)))
#for i = 1:Int(InputData[1,1])
#	#print("x[$i] = ", getValue(x[i]))	
#	println(", w[$i] = ", weight[i])
#end
