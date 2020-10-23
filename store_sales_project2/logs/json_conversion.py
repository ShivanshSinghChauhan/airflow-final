import json
from itertools import product, chain
import os, sys
arr = os.listdir()


import os
import re
# {"workflowName":"","workflowStartTimestamp":"","wfTaskName":"","workflowTaskCompletionStatus":"","workflowTaskCounts":""}     

def  add_completion(filename , dic):
    # Filename: It is actually a path to the location of the file
    # dic: Dictionary containg the actaul data
    f = open(filename)
    count_complete = 0
    count_fail = 0
    for lines in f:
        match_com = re.search(r'AIRFLOW_CTX_EXECUTION_DATE',lines)
        match_fai = re.search(r'FAILED',lines)
        if (match_com):
            count_complete = 1
            break
        if match_fai:
            count_fail = 1
            break
    if count_complete == 1:
        dic["workflowTaskCompletionStatus"] = "Completed"
    if count_fail == 1:
        dic["workflowTaskCompletionStatus"] = "Failed"
    return dic
        

         
def add_path(lst , path):
    if(os.path.isdir(path)):
        files = os.listdir(path)
        for flowname in files:
            new_path = path + "/" + flowname
            if(os.path.isdir(new_path)):
                new_files = os.listdir(new_path)
                for task_name in new_files:
                    newest_path = new_path + "/" + task_name
                    if(os.path.isdir(newest_path)):
                        newest_files = os.listdir(newest_path)
                        for timestamp in newest_files:
                            final_loc = newest_path + "/" + timestamp
                            # At the final step of the location
                            if(os.path.isdir(final_loc)): #To check if there is any files inside the directory
                                final_file =  os.listdir(final_loc) # List  of all log file
                                dic = {"workflowName":flowname,"workflowStartTimestamp":flowname+timestamp,"wfTaskName":task_name,"workflowTaskCompletionStatus":"","workflowTaskCounts":len(new_files)-1}
                                # Iterating  through all log files
                                for each_log in  final_file:
                                    # To check if it's only a log file or not
                                    if(".log" in each_log):
                                        # Generating the path of thelog file
                                        final_path = os.path.join(final_loc, each_log)
                                        dic = add_completion(final_path , dic)
                                        print(dic)
                                        lst.append(dic)
                                


def main():
    directory = r'/Users/apple/Desktop/airflow/store_sales_project2/logs/'
    all_files=[]
    add_path(all_files , directory)
main()


'''
#print(arr)
#print()

def add_path(lst , path):
    if(os.path.isdir(path)):
        files = os.listdir(path)
        for flowname in files:
            new_path = path + "/" + flowname
            if(os.path.isdir(new_path)):
                new_files = os.listdir(new_path)
                for task_name in new_files:
                    newest_path = new_path + "/" + task_name
                    if(os.path.isdir(newest_path)):
                        newest_files = os.listdir(newest_path)
                        for timestamp in newest_files:
                            final_loc = newest_path + "/" + timestamp
                            if(os.path.isdir(final_loc)):
                                final_file =  os.listdir(final_loc)
                                print(final_file)
                                #print(flowname,timestamp,task_name,len(new_files))
                                dic = {"workflowName":flowname,"workflowStartTimestamp":flowname+timestamp,"wfTaskName":task_name,"workflowTaskCompletionStatus":"","workflowTaskCounts":len(new_files)-1}
                                #print(dic)
                                #print()
                                lst.append(dic)
    
        

def main():
    directory = r'/Users/apple/Desktop/airflow/store_sales_project2/logs/'
    all_files=[]
    add_path(all_files , directory)
main()

      
def  recursive_fun(dic,path):
    files = os.listdir(path)
    for file in files:
        new_path = path + "/" + file
        if file  not in dic and os.path.isdir(new_path):
            dic[file]={}
            recursive_fun(dic[file],new_path)
        else:
            dic[file] = 0
            
def recursive_print(dic):
    for key,value in dic.items():
        print(key)
        if(value != 0):
            recursive_print(value)
    

def main():
    directory = r'/Users/apple/Desktop/airflow/store_sales_project2/logs/'
    name = os.path.basename(directory)
    all_files={name:{}}
    recursive_fun(all_files[name],directory)
    print("---->  ",all_files)
    recursive_print(all_files)
    
main()


import os
directory = r'/Users/apple/Desktop/airflow/store_sales_project2/logs/'
files_path1 = os.listdir(directory)
name = os.path.basename(directory)
all_files={name:{}}

for first in files_path1:
    path2 = directory+"/"+first
    if first not in all_files[name] and os.path.isdir(path2):
        all_files[name][first]={}
        files_path2 = os.listdir(path2)
        for second in files_path2:
            path3 = path2+"/"+second
            if second not in all_files[name][first] and os.path.isdir(path3):
                all_files[name][first][second] = {}
                files_path3 = os.listdir(path3)
                for third in files_path3:
                    path4 = path3+"/"+third
                    if third not in all_files[name][first][second] and os.path.isdir(path4):
                        all_files[name][first][second][third] = {}
                        files_path4 = os.listdir(path4)
                        for fourth in files_path4:
                            if fourth not in all_files[name][first][second][third]:
                                all_files[name][first][second][third][fourth] = 0
                    else:
                        all_files[name][first][second][third] = 0    
            else:
                all_files[name][first][second] = 0
    else:
        all_files[name][first] = 0
        
print(all_files)        

      
for k,v in all_files.items():
    #print("Parent Key:---" , k)
    if(v != 0):
        for key,value in v.items():
            #print("Parent Key1:---" , key)
            if (value != 0):
                for ke,val in value.items():
                    #print("Parent Key2:---" , ke)
                    if (val != 0):
                        for x,y in val.items():
                            #print("Parent Key3:---" , x)
                            if (y != 0):
                                for a,b in y.items():
                                    print("logs:---" , a)


 
path = "/Users/apple/Desktop/airflow/store_sales_project2/logs/"
print(os.scandir(path))


dirs = os.listdir( path )
subfolders = [ f.name for f in os.scandir(path) if f.is_dir() ]

#print(subfolders)

dict = {}

lis = []

for root, dirs, files in os.walk("/Users/apple/Desktop/airflow/store_sales_project2/logs"):
    #print("root------>",root)
    #print()
    
    
    
    if dirs != []:
        lis.append(dirs)
        #print("dirs------>",dirs)
        #print()
    #
    #print("files------>",files)
    #print()
    #print("------------------------------------------")
    #print()

#print(lis)
    

def directrys():
    path = "/Users/apple/Desktop/airflow/store_sales_project2/logs/"
    
    dirs = os.listdir( path )
    #print(dirs)
    
    
    subfolders = [ f.name for f in os.scandir(path) if f.is_dir() ]
    #print("DAGs --------->  ", subfolders)
    #print()
    
    DAG_task_list = []
    
    for i in range(len(subfolders)):
        path = "/Users/apple/Desktop/airflow/store_sales_project2/logs/" + str(subfolders[i])
        
        task = [ f.name for f in os.scandir(path) if f.is_dir() ]
        
        DAG_task_list.append(task)
        
    #print("tasks --------->  ",DAG_task_list)
    #print()
directrys()

    
    tast_sub_lisy = []

    
    for i in range(len(DAG_task_list)):
        for j in range(len(DAG_task_list[i])):
            path = path + "/" + DAG_task_list[i][j]
            print(path)
            
            #task_subfolder = [ f.name for f in os.scandir(path) if f.is_dir() ]
            
            #tast_sub_lisy.append(task_subfolder)
            
    #print(tast_sub_lisy)
            
            
    
    
   # print(subfolders)



workflow_id
workflow_str_time = 
no_of_workflow_tasks = 
current_task = 
current_tast_status = 


for file in dirs:    
    print(file)
   #pass
print()

directry = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]

for i in range(len(directry)):
    #print(directry[i])
    #print()
    pass

from glob import glob
glob("/Users/apple/Desktop/airflow/store_sales_project2/logs/*")





print("root prints out directories only from what you specified")
print("dirs prints out sub-directories from root")
print("files prints out all files from root and directories")
print("*" * 20)


for root, dirs, files in os.walk("/Users/apple/Desktop/airflow/store_sales_project2/logs"):
    print("root------>",root)
    print()
    print("dirs------>",dirs)
    print()
    print("files------>",files)
    print()
    print("------------------------------------------")
    print()
    
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
    


