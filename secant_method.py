print("**********SECANT METHOD**********")
print("Equation=x^3-4x-9")
print("************************************")

#'a' is the value in whice f(x)<0 so,a=x
a=2
#'b' is the value in whice f(x)>0 so,b=x
b=3
iteration=0
#setting the result till 4th decimal point
result=0.0000

done=False
while(not done):
    iteration += 1
    # CHANGE EQUATION HERE....****
    fa =round( a * a * a - 4 * a - 9,6)
    fb =round( b * b * b - 4 * b - 9,6)
    # ****************************
    print(f"ITERATION = {iteration}\nValue of x{iteration-1}={a}\nValue of x{iteration}={b}\n"
          f"Value of f(x{iteration-1})={fa}\nValue of f(x{iteration})={fb}")

    x=round((a*fb-b*fa)/(fb-fa),6)
    print(f"Value of x{iteration+1}={x}")
    print("")
    a=b
    b=round(x,4)

    val_x=round(x,4)
    if result==val_x:
        done=True
    result=val_x


print(f"*****--ANSWER--*****\nRoot is:{x}\nTotal Iteration "
      f":{iteration}\n********************")

