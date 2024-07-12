import numpy as np


O=5
yet4 = np.array([[]], dtype=int)
tt = np.array([[]], dtype=int)
def huy(k,v,i,j):
    global tt
   # tt = np.array([[]])
    if k>3:
        k = k-1
        t = np.append(v,i)
        for x in range(j,3):
            if k==3:
                tt = np.append(tt,t)
                gg = np.array([[x]], int)
                tt = np.append(tt,gg)
            uu = np.array([[x]])
            huy(k,t,uu,x)
    
huy(O,yet4,np.array([[]], dtype=int),0)


kim = np.array([0,1,2], dtype=int)


listh = np.array([4,5,7], dtype=int)

def xx(b):
    if b==2:
        return tt
    else:
       return kim
    
l =xx(1)
#cc=4
listm = np.array([[]], int)
listmm = np.array([[]], int)
listy = np.array([], int)

def gyu(cc):
    global listm
    global listy
    for u in range(1,cc):
        if u ==1:
            listm=np.append(listm, [[listh[0]]])
            listm=np.append([listm], [[listh[1]]], axis=0)
            listm=np.append(listm, [[listh[2]]], axis=0)
        else:
            listy = xx(cc)
            for r in range(0,int(listy.shape[0]/cc)):
                for l in range(0,cc):
                    listm = np.append(listm, listh[listy[r*cc+l]])
        print(listm)


#only works if listh has at least 2 numbers
listf=np.array([[]])
for t in range(0,listh.shape[0]):
    if t==0:
        listf=np.append(listf, listh[t])
        listf=[listf]
    else:
        
        listf=np.append(listf, [[listh[t]]], axis=0)
    print(listf)
print(listf)


for v in range(listf.shape[0]-2,-1,-1):

    ii = listf[v,0]+listf[v+1,0]
    listf=np.delete(listf,(v+1), axis=0)
    listf=np.delete(listf,(v), axis=0)
    listf=np.append(listf, [[ii]], axis=0)
print(listf)


'''
def jui(cc):
    
    global listmm
    listmm= np.array([[]], int)
    global listy
    listy = np.array([], int)
    
    listy = xx(cc) 


    listbb = np.array([[]])
    for r in range(0,int(listy.shape[0]/cc)):
        for l in range(0,cc):
            if l==cc-1 and r!=0:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
                print('ii')
                print(listbb)
                listbb = np.append(listbb, [listmm], axis=0)
                listmm = np.array([[]])
            elif r==0 and l==cc-1:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
                print('kk')
                listbb = np.append(listbb, [listmm])
                listmm = np.array([[]])
                listbb=[listbb]
            else:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
    print(listbb)
jui(2)
'''
#same thing but multiplying all numbers in rows
'''
def jui2(cc):
    
    global listmm
    listmm= np.array([[]], int)
    global listy
    listy = np.array([], int)
    
    listy = xx(cc) 

    listo = np.array([[]])
    listbb = np.array([[]])
    for r in range(0,int(listy.shape[0]/cc)):
        for l in range(0,cc):
            if l==cc-1 and r!=0:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
                print('ii')
                
                for t in range(0,listmm.shape[0]):
                    if t==0:
                        listo=np.append(listo, listmm[t])
                        listo=[listo]
                    else:
                        print('oop')
                        print(listo)
                        print(listmm[t])
                        listo=np.append(listo, [[listmm[t]]], axis=0)
                    
                for v in range(listo.shape[0]-2,-1,-1):

                    ii = listo[v,0]+listo[v+1,0]
                    listo=np.delete(listo,(v+1), axis=0)
                    listo=np.delete(listo,(v), axis=0)
                    listo=np.append(listo, [[ii]], axis=0)
                print(listo)
                                    

                print(listbb)
                listbb = np.append(listbb, [listmm], axis=0)
                listmm = np.array([[]])
            elif r==0 and l==cc-1:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
                print('kk')
                listbb = np.append(listbb, [listmm])
                listmm = np.array([[]])
                listbb=[listbb]
            else:
                listmm = np.append(listmm, listh[listy[r*cc+l]])
    print(listbb)
jui2(2)
'''



'''
#print(listy)
listbb = np.array([[9,9]])
for r in range(0,int(listy.shape[0]/cc)):
    for l in range(0,cc):
        if l==cc-1:
            listmm = np.append(listmm, listh[listy[r*cc+l]])

            listbb = np.append(listbb, [listmm], axis=0)
            listmm = np.array([[]])
        elif r==0 and l==0:
            print('oo')
            listmm = np.append(listmm, listh[listy[r*cc+l]])
        else:
            listmm = np.append(listmm, listh[listy[r*cc+l]])
print(listbb)
'''
'''
listbb=np.array([])
listbb = np.append(listbb, [8])
listbb = np.append(listbb, [8])
listbb= [listbb]
listbb = np.append(listbb, [[8,9]], axis=0)
print(listbb)
'''

'''

for r in range(0,int(listy.shape[0]/cc)):
    for l in range(0,cc):
        listm = np.append(listm, listh[listy[r*cc+l]])

print(listm)
print(listy.shape[0]/cc)
print(listy)
'''
