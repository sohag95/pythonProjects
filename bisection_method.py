print("**********BISECTION METHOD**********")
print("Equation=x^3-x-4")
print("************************************")
#'a' is the value in whice f(x)<0 so,a=x
a=1.7
#'b' is the value in whice f(x)>0 so,b=x
b=1.8
#setting the result till 4th decimal point
result=0.000
iteration=0
done=False
while(not done):
    iteration += 1
    print(f"ITERATION = {iteration}\nValue of a={a}\nValue of b={b}")
    m=round((a+b)/2,6)
    print(f"So, m={m}")
    # CHANGE EQUATION HERE....****
    fm =round( m * m * m - m -4,6)
    # ****************************

    print(f"Value of f({m})={fm}")
    if fm<0:
        a=m
        print(f"f(m)<0, so now value of 'a'={a}")
    else:
        b=m
        print(f"f(m)>0, so now value of 'b'={b}")
    print("")
    val_m=round(m,3)
    if result==val_m:
        done=True
    result=val_m

print(f"*****--ANSWER--*****\nRoot is:{round(m,6)}\nTotal Iteration "
      f":{iteration}\n********************")

