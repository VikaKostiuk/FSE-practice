

ime = "Kostiuk Victoria"   

import os
papka = os.path.dirname(os.path.abspath(__file__))
nf = input("Имя файла (Precip, Precip1 или Precip2): ")  
fayl = open(os.path.join(papka, nf + ".txt"), "r", encoding="utf-8")

pr = fayl.readline().strip() 
mest = fayl.readline().strip()       
my = fayl.readline().split(",")      
mes = my[0].strip()                 
god = int(my[1])                     

if mes == "April" or mes == "June" or mes == "September" or mes == "November":
    dn = 30                         
elif mes == "February":
    if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
        dn = 29
    else:
        dn = 28
else:
    dn = 31                          

osad = [None] * (dn + 1)             
                                     
osh = []                            
nom = 3                              

for st in fayl:                      
    nom = nom + 1                    
    dan = st.split()                 
    if len(dan) == 0:                
        continue                     
    den = int(dan[0])                
    kol = float(dan[1])             

    if den < 1 or den > dn:          
        osh.append(("Invalid", den, nom))
    elif osad[den] is not None:      
        osh.append(("Repeated", den, nom))   
    else:                            
        osad[den] = kol

fayl.close()                         

mn = None                           
mx = None                           
sm = 0.0                             

for den in range(1, dn + 1):         
    if osad[den] is not None:       
        if mn is None or osad[den] < mn:
            mn = osad[den]
        if mx is None or osad[den] > mx:
            mx = osad[den]
        sm = sm + osad[den]

ot = []                              
ot.append("Programmer: " + ime)
ot.append(pr)
ot.append("")
ot.append("Precipitation report for " + mest + " during " + mes + ", " + str(god))
ot.append("")
ot.append("Error".ljust(12) + "Day".rjust(5) + "Line".rjust(9))
for o in osh:                       
    ot.append(o[0].ljust(12) + str(o[1]).rjust(5) + str(o[2]).rjust(9))
ot.append("")
ot.append("Day Amount Graph")

for den in range(1, dn + 1):         
    if osad[den] is None:            
        sum_t = "NA".rjust(7)
        zv = ""
    else:
        sum_t = f"{osad[den]:.2f}".rjust(7)   
        ost = osad[den]              
        kz = 0                       
        while ost > 0.000001:       
            kz = kz + 1              
            ost = ost - 0.25        
        zv = " " + "*" * kz          
    ot.append(str(den).rjust(3) + sum_t + zv)

ot.append("")
ot.append("Minimum".rjust(10) + "Maximum".rjust(11) + "Average".rjust(11))
if mn is None:                       
    ot.append("NA".rjust(10) + "NA".rjust(11) + "NA".rjust(11))
else:
    sr = sm / dn                     
    ot.append(f"{mn:.2f}".rjust(10) + f"{mx:.2f}".rjust(11) + f"{sr:.2f}".rjust(11))

vyh = open(os.path.join(papka, nf.replace("Precip", "Report") + ".txt"), "w", encoding="utf-8")
for s in ot:                        
    vyh.write(s + "\n")              
vyh.close()                         

print("Отчёт записан в файл Report.txt")