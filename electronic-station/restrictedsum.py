#Recursion implementation for summing values inside a list/array
def checkio(data):
    return add(data,len(data)-1)
    
def add (data,n):
    if n == 0:
        return data[n]
    else:
         return data[n] + add(data,n-1)
