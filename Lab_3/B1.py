import os
papka = os.path.dirname(os.path.abspath(__file__))  
nf = input("Номер файла (1-5): ")                   
fayl = open(os.path.join(papka, nf + ".ChaseData.txt"), "r")
per = fayl.readline().split()       
nstr = int(per[0])                 
nstb = int(per[1])                 

mr = None   
ms = None   
kr = None    
ks = None    
dm = 0       
dk = 0       
pojm = False 
tab = []     

for st in fayl:                     
    dan = st.split()                
    if len(dan) == 0:               
        continue                   
    bukva = dan[0]                  

    if bukva == "P":
        if kr is None:              
            tk = "( ?, ?)"
        else:                       
            tk = "(" + str(kr).rjust(2) + "," + str(ks).rjust(2) + ")"

        if mr is None:              
            tm = "( ?, ?)"
        else:
            tm = "(" + str(mr).rjust(2) + "," + str(ms).rjust(2) + ")"

        if kr is None or mr is None:    
            rass = ""
        else:                          
            rass = str(abs(kr - mr) + abs(ks - ms))

        tab.append(tk + "      " + tm + "      " + rass.rjust(3))

    elif bukva == "M":
        a = int(dan[1])             
        b = int(dan[2])             

        if mr is None:              
            mr = a
            ms = b
        else:                       
            dm = dm + abs(a) + abs(b)           
            mr = (mr + a - 1) % nstr + 1        
            ms = (ms + b - 1) % nstb + 1

    
    elif bukva == "C":
        a = int(dan[1])
        b = int(dan[2])

        if kr is None:              
            kr = a
            ks = b
        else:                       
            dk = dk + abs(a) + abs(b)
            kr = (kr + a - 1) % nstr + 1
            ks = (ks + b - 1) % nstb + 1

    if kr is not None and mr is not None:      
        if kr == mr and ms == ks:               
            pojm = True
            break                              
fayl.close()                       

print("Cat and Mouse")
print()
print("  Cat          Mouse     Distance")
print("-" * 36)
for s in tab:                      
    print(s)
print("-" * 36)
print()
print()
print("Distance  Mouse    Cat")
print(str(dm).rjust(14) + str(dk).rjust(8))
print()

if pojm:                            
    print("Cat caught Mouse")
else:
    print("Mouse evaded Cat")
