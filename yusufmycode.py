N=range(1000)
p=[]
x_0=0.4
lambda_1=0.9
for i in N:
    p.append(x_0)
    x_0=4*lambda_1*x_0*(1-x_0)
print p
    
  


    
  


