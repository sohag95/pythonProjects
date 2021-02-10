print("**********NEWTON RAPHSON METHOD**********")
print("Equation : x^3-4x-9")
print("Derivative Equation: 3x^2-4")
print("Formula x1=x0-(fx/fx_der)")
print("*****************************************")
print("")
#initial value of x.....
#thevalue of x will be in between a and b.where f(a)<0 & f(b)>0
x=2.5
iteration=0
#setting the result till 4th decimal point
result=0.0000

done=False
while(not done):
    print(f"ITERATION = {iteration+1}\nValue of x{iteration}={x}")

    # CHANGE MAIN EQUATION HERE....****
    fx=x*x*x-4*x-9
    # CHANGE DERIVATIVE EQUATION HERE....****
    fx_der = 3 * x * x -4
    # ****************************
    x=x-(fx/fx_der)
    x=round(x,6)
    print(f"Value of x{iteration+1}={round(x, 6)}")
    print("")
    iteration += 1
    val_x=round(x,4)
    if result==val_x:
        done=True
    result=val_x

print(f"*****--ANSWER--*****\nRoot is:{round(x,6)}\nTotal Iteration "
      f":{iteration}\n********************")
