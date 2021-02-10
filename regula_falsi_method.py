
print("**********REGULA FALSI METHOD**********")
print("Equation=x^3-x-1")
print("*****************************************")
print("")

#'a' is the value in whice f(x)<0 so,a=x
a=1
#'b' is the value in whice f(x)>0 so,b=x
b=1.5
#setting the result till 4th decimal point
result=0.0000
iteration=0
done=False
while(not done):
    iteration += 1
    print(f"ITERATION = {iteration}\nValue of a={a}\nValue of b={b}")
    # CHANGE EQUATION HERE....****
    fa=a*a*a-a-1
    fb=b*b*b-b-1
    # ****************************
    x=round((a*fb-b*fa)/(fb-fa),6)

    #CHANGE EQUATION HERE....****
    fx=round(x*x*x-x-1,6)
    #****************************
    print(f"Value of x{iteration}={x}\nf(x{iteration})={fx}")
    if fx<0:
        a=round(x,6)
        print(f"f(x{iteration})<0, so now value of 'a'={a}")
    else:
        b=round(x,6)
        print(f"f(x{iteration})>0, so now value of 'b'={b}")
    print("")
    val_x=round(x,4)
    if result==val_x:
        done=True
    result=val_x

print(f"*****--ANSWER--*****\nRoot is:{round(x,6)}\nTotal Iteration "
      f":{iteration}\n********************")



