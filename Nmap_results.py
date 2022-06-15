import nmap,datetime

xxx = input("Enter an IP adress you want to scan: ")
print(f"The IP adress is: {xxx}")
print("Please Wait ...")
x = datetime.datetime.now()

nmScan = nmap.PortScanner()
nmScan.scan(xxx)

file=open("open_ports.txt", 'a')
file.write('--------------------------------------------\n')
file.write('The scanned IP adress: '+str(xxx) +'\n'+'Scan date: '+ str(x)+'\n')
for host in nmScan.all_hosts():
    for proto in nmScan[host].all_protocols():
        lport = nmScan[host][proto].keys()
        
        #lport.sort()
        for port in lport:
            file.write('Open Port: '+str(port)+'/'+proto.upper()+' - Service: '+nmScan[host][proto][port]['name']+'\n')
file.write('--------------------------------------------\n')
file.write('Done \n')
file.close()
print('Done! Please check your open ports file.')
