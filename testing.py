with open('form.txt','r+',encoding='utf-8') as file1:
    metn = file1.read()
    metn2 = str(metn[178:-59])
    
print(metn2)
with open('textin2.txt','w',encoding='utf-8') as file2:
    file2.write(metn2)



