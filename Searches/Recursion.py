def factorial(n): # For Tracing / Trace Table
    answer = 1
    for x in range(1, n+1):
        answer = answer * x
        return answer
    #-----------------

print(factorial(3))

#-------------------------------
# Same program but done RECURSIVELY. Recurision Concept

def recursiveFact(n):
    if n ==0:
        return 1
    else:
        return n* recursiveFact(n-1)
    #----------------

print(recursiveFact(3))