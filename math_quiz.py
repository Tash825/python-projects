import random
import time

operators = ["+","-","*"]
min_op = 1
max_op = 10
total_problems = 10

def problem():
    left =  random.randint(min_op, max_op)
    right =  random.randint(min_op, max_op)
    operator = random.choice(operators)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

correct =0
input("press enter to start")
print("--------------------")

start = time.time()
for i in range(total_problems):
    expr, answer = problem()
    guess = input("Problem ~" + str(i+1) + ": " + expr + " = ")
    if guess == str(answer):
        correct += 1

end = time.time()
total_time = round(end- start, 2)
print("--------------------")
print("Nice work!, you finished in" , total_time , " seconds and got " + str(correct) + " answers right and "+ str(10-correct) +" answers wrong")
