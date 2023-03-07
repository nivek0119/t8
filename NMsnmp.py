from easysnmp import *
from pysnmp.hlapi import *
from pysnmp import *
import json
from pydantic.utils import deep_update #pip install pydantic
import time
import matplotlib.pyplot as plt
import numpy as np

def Obj_4_d_createDictionaryAndSaveinFile():
    
    di={}
    ipaddress=["40.0.0.1","30.0.0.1","30.0.0.2","30.0.0.3","198.51.100.4"]
    # ipaddress=["40.0.0.1"]

 #######################################################################################
 #IP-MIB::ipAdEntIfIndex.40.0.0.1 = INTEGER: 2
 #getting ip, subnet mask and its interface number from interger
    for ip in ipaddress:

        session = Session(hostname=ip, community='public', version=2)
        system_items = session.walk('1.3.6.1.2.1.4.20.1.2')

        for item in system_items:
        #     print('{oid_index}= {value}'.format(
        #     oid_index=item.oid_index,
        #     value=item.value
        # ))
            # print(item)
            oid="1.3.6.1.2.1.4.20.1.3."+item.oid_index
            k=session.get(oid)
            subnetval=k.value

            interfacename=""
            if item.value=="1":
                interfacename="FastEthernet0/0"
            elif item.value=="2":
                interfacename="FastEthernet1/0"
            elif item.value=="3":
                interfacename="FastEthernet1/1"
            elif item.value=="4":
                interfacename="FastEthernet2/0"
            elif item.value=="5":
                interfacename="FastEthernet2/1"
            elif item.value=="6":
                interfacename="GigabitEthernet3/0"
            elif item.value=="7":
                interfacename="Null"
                
            routername=""
            if ip=="40.0.0.1":
                routername="R1"
            elif ip=="30.0.0.1":
                routername="R5"
            elif ip=="30.0.0.2":
                routername="R2"
            elif ip=="30.0.0.3":
                routername="R3"
            elif ip=="198.51.100.4":
                routername="R4"

            v4val=str(item.oid_index)+"/"+subnetval

            update={
                routername:{
                    "addresses":{
                            interfacename:{
                                    "v4":v4val
                            }
                    }
                }
            }
            # update={}
            di = deep_update(di, update)


    # print(di)
    # print(json.dumps(di,sort_keys=True, indent=4))
 #######################################################################################
 

  #getting interfaceStatus 
    for ip in ipaddress:
        session = Session(hostname=ip, community='public', version=2)
        system_items2 = session.walk('1.3.6.1.2.1.2.2.1.8')
        # system_items2= system_items2[:-1]
        # print(system_items2)
        for item in system_items2:
            # print(item.value)

            interfacename=""
            if item.oid_index=="1":
                interfacename="FastEthernet0/0"
            elif item.oid_index=="2":
                interfacename="FastEthernet1/0"
            elif item.oid_index=="3":
                interfacename="FastEthernet1/1"
            elif item.oid_index=="4":
                interfacename="FastEthernet2/0"
            elif item.oid_index=="5":
                interfacename="FastEthernet2/1"
            elif item.oid_index=="6":
                interfacename="GigabitEthernet3/0"
            elif item.oid_index=="7":
                interfacename=""

            routername=""
            if ip=="40.0.0.1":
                routername="R1"
            elif ip=="30.0.0.1":
                routername="R5"
            elif ip=="30.0.0.2":
                routername="R2"
            elif ip=="30.0.0.3":
                routername="R3"
            elif ip=="198.51.100.4":
                routername="R4"

            
            if item.value=="2":
                interfaceStatus="down"
            else:
                interfaceStatus="Up"

            if interfacename=="":
                ""
            else:

                update={
                    routername:{
                        "Status":{
                                interfacename:interfaceStatus
                        }
                    }
                }
                
                di = deep_update(di, update)
     #######################################################################################
    # # print(di)

    #################################################################################################
    #IP-MIB::ipAddressIfIndex.ipv6."00:dd:00:00:00:00:00:00:00:00:00:00:00:00:00:01" = INTEGER: 2
    #getting ipv6 ip and its interface name from integer
    for ip in ipaddress:
    
        session = Session(hostname=ip, community='public', version=2)
        # di={}
        system_items = session.walk('.1.3.6.1.2.1.4.34.1.3.2')
        parts=[]
        for item in system_items:

            k=item.oid_index
            parts = k.split(".")
            parts=parts[2:]
            # print(parts)
            for i in range(len(parts)):
                inhex=hex(int(parts[i]))[2:]
                parts[i]=inhex
            parts=":".join(parts)
            # print(parts)


            interfacename=""
            if item.value=="1":
                interfacename="FastEthernet0/0"
            elif item.value=="2":
                interfacename="FastEthernet1/0"
            elif item.value=="3":
                interfacename="FastEthernet1/1"
            elif item.value=="4":
                interfacename="FastEthernet2/0"
            elif item.value=="5":
                interfacename="FastEthernet2/1"
            elif item.value=="6":
                interfacename="GigabitEthernet3/0"
            elif item.value=="7":
                interfacename="Null"
                    
            routername=""
            if ip=="40.0.0.1":
                routername="R1"
            elif ip=="30.0.0.1":
                routername="R5"
            elif ip=="30.0.0.2":
                routername="R2"
            elif ip=="30.0.0.3":
                routername="R3"
            elif ip=="198.51.100.4":
                routername="R4"


            update={
                    routername:{
                        "addresses":{
                                interfacename:{
                                        "v6":parts
                                }
                        }
                    }
                }
            di = deep_update(di, update)
        # print(di)

    print(json.dumps(di,sort_keys=True, indent=4))
    text_file = open("Output.txt", "w")

    text_file.write(str(di))

    text_file.close()




        
    
def getCpuUtilization():
    timez=0
    utilinationList=[]
    timeListInSeconds=[]
    while(1):
        if timez>=120:
            break
        else:
            session = Session(hostname="40.0.0.1", community='public', version=2)
            system_items=session.walk(".1.3.6.1.4.1.9.9.109.1.1.1.1.6")
            # print(timez)
            # print()
            utilinationList.append(system_items[0].value)
            timeListInSeconds.append(timez)
            timez=timez+5
            time.sleep(5)

   

    x = np.array(timeListInSeconds)  # X-axis points
    y = np.array(utilinationList) # Y-axis points
    
    plt.plot(x, y)  
    # plt.show()  
    plt.xlabel('Time in Seconds')
    plt.ylabel('CPU Utilization in Percentage')
    plt.title('CPU Utilization Line Graph')
    plt.savefig("output.jpg")



    ""

# fun2() .1.3.6.1.4.1.9.9.109.1.1.1.1.3

def fun2():
    

    # interface_name_walk = session.walk('1.3.6.1.2.1.2.2.1.2') #interface number
    # interface_name=[]
    # for item in interface_name_walk:
    #     interface_name.append(item.value)
    # print(interface_name)

    # ip_Address_walk = session.walk('1.3.6.1.2.1.4.20.1.1') #ip address
    # ip_Address=[]
    # for item in ip_Address_walk:
    #     ip_Address.append(item.value)
    # print(ip_Address)

    # ip_Address_subnet_walk = session.walk('.1.3.6.1.2.1.4.20.1.3') #ip address subnet
    # ip_Address_subnet=[]
    # for item in ip_Address_subnet_walk:
    #     ip_Address_subnet.append(item.value)
    # print(ip_Address_subnet)

    # interface_status_walk = session.walk('1.3.6.1.2.1.2.2.1.8')#interface status
    # interface_status=[]
    # for item in interface_status_walk:
    #     interface_status.append(item.value)
    # print(interface_status)

    
    # index = session.walk('1.3.6.1.2.1.4.20.1.2')#index
    # interface_status=[]
    # for item in interface_status_walk:
    #     index.append(item.value)
    # # print(index)

    # dict={}
    
    # loc = session.get('ifDescr.1')
    # print(loc.value)
    # #cpu1min - 1.3.6.1.4.1.9.2.1.57.0
    # #IP-MIB::ipv6InterfaceIdentifier.2 = STRING: c801:31ff:fea2:1c
    # #IP-MIB::ipAddressIfIndex.ipv6."cc:cc:00:00:00:00:00:00:00:00:00:00:00:00:00:01" = INTEGER: 2
    
    # # system_items = session.walk('IP-MIB::ipAddressIfIndex.ipv6')
    # # system_items = session.walk('.1.3.6.1.2.1.4.34.1.5.2')

    ipaddress=["40.0.0.1","30.0.0.1","30.0.0.2","30.0.0.3","198.51.100.4"]
    # ipaddress=["40.0.0.1"]

 #######################################################################################
    for ip in ipaddress:
    
        session = Session(hostname=ip, community='public', version=2)
        di={}
        system_items = session.walk('.1.3.6.1.2.1.4.34.1.3.2')
        parts=[]
        for item in system_items:

            k=item.oid_index
            parts = k.split(".")
            parts=parts[2:]
            # print(parts)
            for i in range(len(parts)):
                inhex=hex(int(parts[i]))[2:]
                parts[i]=inhex
            parts=":".join(parts)
            # print(parts)


            interfacename=""
            if item.value=="1":
                interfacename="FastEthernet0/0"
            elif item.value=="2":
                interfacename="FastEthernet1/0"
            elif item.value=="3":
                interfacename="FastEthernet1/1"
            elif item.value=="4":
                interfacename="FastEthernet2/0"
            elif item.value=="5":
                interfacename="FastEthernet2/1"
            elif item.value=="6":
                interfacename="GigabitEthernet3/0"
            elif item.value=="7":
                interfacename="Null"
                    
            routername=""
            if ip=="40.0.0.1":
                routername="R1"
            elif ip=="30.0.0.1":
                routername="R5"
            elif ip=="30.0.0.2":
                routername="R2"
            elif ip=="30.0.0.3":
                routername="R3"
            elif ip=="198.51.100.4":
                routername="R4"


            update={
                    routername:{
                        "addresses":{
                                interfacename:{
                                        "v6":parts
                                }
                        }
                    }
                }
            di = deep_update(di, update)
        print(di)