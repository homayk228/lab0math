from statistics import mean
massive=[138.8,136.5,134.1,140.4,139,137.8,135.8,138.4,138.2,138.1,137.9,136.2,137.9,137.9,135.4,141.4,136.7,136.7,136.8,140,140.5,138.3,163.3,140.1,141.1,138.5,139.8,142.2,138.8,139,135,140.6,141.2,140.8,139.1,137.5,142.6,139.9,140,138.8,141.9,139.8,139.1,142,135.1,139.9,137.2,138.7,136.6,150.6]
list_avg = mean(massive)
massiveform1=[]
massiveform2=[]
massiveform3=[]
i=0
while i < len(massive):
    eq1=list_avg-massive[i]
    massiveform3.append(eq1**2)
    if eq1 < 0:
        eq1=(-1)*eq1
    massiveform1.append(eq1)
    i+=1
i=0
while i < len(massiveform1):
    eq2=massiveform1[i]**2
    massiveform2.append(eq2)
    i+=1
i=0
eq3=0
while i < len(massiveform3):
    eq3+=massiveform3[i]
    i+=1
eq4=(eq3**0.5)/(len(massive)-1)



print("Среднее:")
print(list_avg)
print("Массив 1:")    
print(massiveform1)
print("Массив 2:")    
print(massiveform2)
print("О со шляпкой:")
print(eq4)
print(min(massive),max(massive))

nm=[]
t=0
while t < 7:
    nm.append(0)
    t+=1
print(nm)




i=0
i2=0
while i<len(massive):
    i2+=1
    if massive[i] < 138.2714:
        print("1: "+str(massive[i])+':'+str(i2))
        nm[0]=nm[0]+1
    elif massive[i] < 142.4428:
        print("2: "+str(massive[i])+':'+str(i2))
        nm[1]=nm[1]+1
    elif massive[i] < 146.6142:
        print("3: "+str(massive[i])+':'+str(i2))
        nm[2]=nm[2]+1
    elif massive[i] < 150.7856:
        print("4: "+str(massive[i])+':'+str(i2))
        nm[3]=nm[3]+1
    elif massive[i] < 154.957:
        print("5: "+str(massive[i])+':'+str(i2))
        nm[4]=nm[4]+1
    elif massive[i] < 159.1284:
        print("6: "+str(massive[i])+':'+str(i2))
        nm[5]=nm[5]+1
    else:
        print("7: "+str(massive[i])+':'+str(i2))
        nm[6]=nm[6]+1
    i+=1

print(nm)
