import requests
import pprint
import boto3
import json

import csv

'''
def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = {}
        for i in item.keys():
            leaves.update(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = {}
        for i in item:
            leaves.update(get_leaves(i, key))
        return leaves
    else:
        return {key : item}


with open('saleforce.json') as f_input:
    json_data = json.load(f_input)''

# First parse all entries to get the complete fieldname list
fieldnames = set()

for entry in json_data:
    fieldnames.update(get_leaves(entry).keys())

with open('output.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=sorted(fieldnames))
    csv_output.writeheader()
    csv_output.writerows(get_leaves(entry) for entry in json_data)'''

def t1():
    r = requests.get('http://ec2-52-52-87-0.us-west-1.compute.amazonaws.com:9095/shared-data/transformation-info?sharedDataRequestID=DHCS-FAS-002')
    path_val = r.json()['trasformFilePath']
    data_val = r.json()['data']
    t2(path_val)
    t3(data_val)

def t2(path_val):
    split_path = path_val.split("/")
    bucket = split_path[0]
    path = '/'.join(split_path[1:])
    s3 = boto3.client('s3', aws_access_key_id="AKIAWKFCJ64V2NBMV245", aws_secret_access_key="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", region_name='us-west-1')
    s3.download_file(str(bucket), str(path) + '/mapping.adm', 'mapping.adm')
    #print("path --->", str(path))
    #print("bucket --->", str(bucket))

    #usr = user input

def t3(data_val):
    url = "http://ec2-52-52-87-0.us-west-1.compute.amazonaws.com:9090/upload"

    #payload = {'json ': '"[{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]},{\\"DateOfBirth\\":\\"1/6/2004\\",\\"personName\\":[{\\"FirstName\\":\\"Debbie\\",\\"LastName\\":\\"Diebold\\"}],\\"SexatBirthCode\\":\\"M\\",\\"address\\":[{\\"structuredAddress\\":null,\\"FullAddress\\":\\"1750 FILBERT AVE 13 CHICO California CA 95926\\"}]}]"',
    #'sharedDataRequestId': 'DHCS-FAS-002'}

    payload = {'json ': data_val,
    'sharedDataRequestId': 'DHCS-FAS-002'}

    #print(payload)

    files = [
      ('file ', open('./mapping.adm','rb'))
    ]
    headers= {}

    response = requests.request("POST", url, headers=headers, data = payload, files = files)

t1()

    #print(response.text.encode('utf8'))
'''
def t4():
    url = "http://ec2-52-52-87-0.us-west-1.compute.amazonaws.com:9095/shared-data/salesforce/upload"

    payload = {}
    files = [
      ('file', open('/Users/apple/Desktop/airflow/store_sales_project2/dags/output.csv','rb'))
    ]
    headers= {}

    response = requests.request("POST", url, headers=headers, data = payload, files = files)

    print(response.text)

    #print(response.text)




#s3 = boto3.client('s3')    

API_ENDPOINT = "http://ec2-52-52-87-0.us-west-1.compute.amazonaws.com:9090/upload"

file = "/Users/apple/Desktop/airflow/store_sales_project2/dags/mapping.adm"

headers={'Content-type':'application/json', 'Accept':'application/json'}

y = "[{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]},{\"DateOfBirth\":\"1/6/2004\",\"personName\":[{\"FirstName\":\"Debbie\",\"LastName\":\"Diebold\"}],\"SexatBirthCode\":\"M\",\"address\":[{\"structuredAddress\":null,\"FullAddress\":\"1750 FILBERT AVE 13 CHICO California CA 95926\"}]}]"

data = json.loads(y)
 
sharedDataRequestId = "DHCS-FAS-002" 

parameter = {'file': "file", 'data': "data", 'sharedDataRequestId': "sharedDataRequestId" }

r = requests.post(url = API_ENDPOINT, json = parameter, headers = headers) 

pastebin_url = r.text 
print(pastebin_url)


'''

'''
import airflow.hooks.S3_hook

def upload_file_to_S3_with_hook():
    hook = airflow.hooks.S3_hook.S3Hook('my_S3_conn')
    hook.get_key('integration/SharedDataRequest/DHCS-FAS-002/atlasmap-mapping.adm' , 'xaqua-udp')'''