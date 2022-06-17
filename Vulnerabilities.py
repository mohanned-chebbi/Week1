import requests, zipfile,json
from io import BytesIO
print('Downloading started')

#Defining the zip file URL
url = 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip'

#filename = url.split('/')[-1]

req = requests.get(url)
print('Downloading Completed')

zipfile= zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall()

myjsonfile=open('nvdcve-1.1-modified.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

list=obj['CVE_Items']

cve=[]
for i in range(len(list)):
    cve.append(list[i].get("cve"))

data=[]
for i in range(len(cve)):
    data.append(cve[i].get("CVE_data_meta"))

cid=[]
for i in range(len(data)):
    cid.append(data[i].get("ID"))


desc=[]
for i in range(len(cve)):
    desc.append(cve[i].get("description"))

desdata=[]
for i in range(len(desc)):
    desdata.append(desc[i].get("description_data"))

for i in range(len(list)):
    print(cid[i] +':'+ desdata[i][0]['value'])
