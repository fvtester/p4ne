import glob
#print(glob.glob('config_files\*.txt'))
files=glob.glob('config_files\*.txt')
ip_adresses=[]
for file in files:
    with open(file) as f:
        for i in f:
            if i.find("ip address")>=0 and len(i.replace("ip address","").strip()):
                ip_adresses.append(i.replace("ip address","").strip())
print(list(set(ip_adresses)))
print(len(list(set(ip_adresses))))
