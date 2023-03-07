from NMtcpdump import *
from NMdhcpserver import *
from NMsnmp import *
from NMgithub import *

print("Initializing Git")
gitInit()
print("Successfully Initialized Git")
print("")
print("Adding All files in repo")
gitAddAll()
print("")
print("Comminting All changes locally in repo")
gitCommit()
gitRemoteAddOrigin()
print("")
print("Sending all commit changes to remote repo")
gitpushOriginMaster()





pkts_list= rdpcap(r'/home/kevin/Netman/Lab_5_Midterm/lab5.pcap')
R2ipv6IP=pkts_list[6]['IPv6'].src
R3ipv6IP=pkts_list[16]['IPv6'].src

R2_F_0_0_mac=""
R3_F_0_0_mac=""

getmac = getMacFromIPv6Address(R2ipv6IP)
ipv6IP=getmac[0]
R2_F_0_0_mac=getmac[1]

print("For Router: R2-F0/0")
# 0063.6973.636f.2d63.6130.322e.3331.6231.2e30.3030.302d.4661.302f.30
print ("IPv6 Address:", ipv6IP)
print ("MAC:", R2_F_0_0_mac)

print("")

getmac = getMacFromIPv6Address(R3ipv6IP)
ipv6IP=getmac[0]
R2_F_0_0_mac=getmac[1]

print("For Router: R3-F0/0")
# 0063.6973.636f.2d63.6130.332e.3331.6330.2e30.3030.302d.4661.302f.30
print ("IPv6 Address:", ipv6IP)
print ("MAC:", R2_F_0_0_mac)

R2 = {
    'device_type': 'cisco_ios',
    'host':   'AAAA::C802:31FF:FEB1:0',
    'username': 'kevin',
    'password': 'kevin',
    'secret':'kevin'
}

ipv6OfR5=getIPv6AddressOfR5usingCDPinR2(R2)

R5 = {
    'device_type': 'cisco_ios',
    'host':   ipv6OfR5,
    'username': 'kevin',
    'password': 'kevin',
    'secret':'kevin'
}
print("")
print("Sending DHCP commands for R5-",ipv6OfR5)
sshAndExecuteCommands(R5)
print("")
print("")
getIPv4Bindings(R5)

print("Creating Dictionary")
Obj_4_d_createDictionaryAndSaveinFile()
print("Created Dictionary and Saved in Output.txt File")

print("")

print("getting CPU Utilization - Wait for 2 minutes")
getCpuUtilization()
print("Succesful Check Generated Image Output.jpg")

print("")


# gitStatus()
print("")
print("Showing Differences")
gitDiff()

# time.sleep(10)
print("")
print("Adding All files in repo")
gitAddAll()
print("")
print("Comminting All changes locally in repo")
print("")
gitCommit()
print("")
print("Sending all commit changes to remote repo")
print("")
gitpushOriginMaster()