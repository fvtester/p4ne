import ipaddress
import glob
import ipaddress
import re

def IPclassify(sent):
    if sent.find("ip address")>=0 and re.match('^([1-9]{1,3}\.?){1,4}', sent.replace("ip address","").strip()):
        #print(sent.replace("ip address","").strip().split(' ')[0])
        return {'ip':ipaddress.IPv4Address(sent.replace("ip address","").strip().split(' ')[0])}
    if sent.find("interface")>=0 and re.match('^([A-z].)', sent.replace("interface","").strip()):
        #print(sent.replace("interface","").strip())
        sent_list = sent.split(' ')
        # print(sent_list)
        for ind, j in enumerate(sent_list):
            # print(j)
            if j == "interface":
                return {'int': sent_list[ind + 1].strip()}
    if sent.find(" host ")>=0:
        sent_list=sent.split(' ')
        #print(sent_list)
        for ind, j in enumerate(sent_list):
            #print(j)
            if j == 'host':
                #print('host')
                return {'host': sent_list[ind+1].strip()}#.replace("host","")}#.strip().split(' ')[0]}
    else: return {}

files=glob.glob('config_files\*.txt')
ip_adresses=[]
interfaces=[]
hosts=[]
for file in files:
    with open(file) as f:
        for i in f:
            if IPclassify(i).keys():
                #print(IPclassify(i).keys())
                if 'ip' in IPclassify(i).keys():
                    ip_adresses.append(IPclassify(i)['ip'])
                if 'int' in IPclassify(i).keys():
                    interfaces.append(IPclassify(i)['int'])
                if 'host' in IPclassify(i).keys():
                    #print(1)
                    hosts.append(IPclassify(i)['host'])
            #if IPclassify(i):
                #ip_adresses.append(i.replace("ip address","").strip())
print('ip_adresses: ',list(set(ip_adresses)))
print(len(list(set(ip_adresses))))
print('interfaces: ', list(set(interfaces)))
print(len(list(set(interfaces))))
print('hosts: ', list(set(hosts)))
print(len(list(set(hosts))))
