import json
def file_open():
    dic = {}
    f = open("1.log").readlines()
    print(f)
    for i in range(len(f)):
        f[i] = f[i].strip().split('|')
        #print(f[i])
        for j in range(len(f[i])):
            some = f[i][j].split('--->')
            #dic[some[0]] = some[1]
            
            #print("some------", dic)

file_open()
