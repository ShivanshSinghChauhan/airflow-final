import json

import os
arr = os.listdir()
#print(arr)

directry = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]
print(directry)

def file_open():
    dic = {}
    lis_val = []
    lis_key = []
    lis = []
    f = open("1.log").readlines()
    for i in range(0, 20): #len(f)
        f[i] = f[i].strip().split('|')

        if (("--------------------------------------------------------------------------------") not in f[i]):
            dic["time"] = f[i][0]
            dic["file"] = f[i][1]
            dic["level"] = f[i][2]
            dic["message"] = f[i][3]
            #print("dic=======>",dic)
            #print()
            
    

file_open()
        
'''
    
        if ("--------------------------------------------------------------------------------" not in f[i]):
            for j in range(len(f[i])):
                some = f[i][j].strip().split('--->')
                som = json.dumps(some)
                #dic[some[0]] = dic[some[1]]
                #dic[som[0]] = som[1]
    print(dict(som))
    print()
                #lis_key.append([some[0]])
                #lis_val.append([some[1]])
                
                #dic[some[0]] = lis.append([some[1]])
    #print("lis_val------>",lis_val)
    #print()
    #print("lis_key------>",lis_key)
    
    #print(dic[lis_key[0][0]])
    
    
    for i in range(len(lis_key)):
        
        if lis_key[i] in dic:
            dic[lis_key[i]] = lis.append(lis_val[i])
        else:
            dic[lis_key[i]]'''
    


