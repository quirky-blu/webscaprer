import requests as r
from_sem,to_sem=1,2
year=23
branch={'C':'CS','I':'IT','T':'ETC','E':'Ei','M':'MECH','V':'CIVIL'}
sec={0:'a',1:'b'}
for br in branch.keys():
    if br in ['C','I','T']:
        sec={0:'a',1:'b'}
    else:
        sec={0:'a'}
    for section in sec.keys():
        semno=1
        while semno in range(from_sem,to_sem+1):
            l=[]
            for i in range(1,81):
                s=str(r.get('http://results.ietdavv.edu.in/DisplayStudentResult?rollno='+str(year)+br+str(semno)+str(section)+str(i).zfill(2)+'&typeOfStudent=Regular').content)
                if s.count('ROLL_NO NOT FOUND')==1:
                #    print('no roll no')
                    continue
                # y=s.find('Student Name')
                # z=y+33
                # while s[z].isalpha() or s[z]==' ':
                #     z+=1
                # print(s[y+33:z])
                x=s.find("SGPA")
                z=x+40
                try:
                    while s[z]!='<' :
                        z+=1
                    # print(s[x+40:z])
                    l.append(float(s[x+40:z]))
                except:
                    print('sgpa not found for roll no'+str(year)+br+str(semno)+str(section)+str(i).zfill(2))
            print(branch[br]+' sec '+ sec[section] + ' sem '+ str(semno) +' avg : ', + sum(l)/len(l))
            semno+=1



