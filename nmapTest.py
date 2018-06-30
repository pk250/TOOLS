# coding:utf8
#!/usr/bin/python
from nmap import nmap
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f","--file",action="store",dest="FileName",default="ms17-010",help="Out Put File Name")
parser.add_option("-l","--hosts",action="store",dest="hosts",default="10.1.1.1/24",help="target hosts")
(options,args) = parser.parse_args()
nm = nmap.PortScanner()
print('creating file....')
print(str(options.FileName))
fw=open(str(options.FileName)+".txt",'a+')
print('scanning.........')
print(str(options.hosts))
data = nm.scan(hosts=str(options.hosts),ports='445',arguments='--script=smb-vuln-ms17-010')
print('save out stream')
data1 = json.dumps(data)
data2 = json.loads(data1)
hosts = nm.all_hosts()

for index in range(len(hosts)):
    a = data2.get('scan').get(hosts[index]).get('hostscript')
    if a != None:
        print(a)
        print >> fw, hosts[index]
    else:
        print('not vuln')

