from netmiko import ConnectHandler
import re
import time

def sshAndExecuteCommands(RouterSshDetails):
    try:
        connection = ConnectHandler(**RouterSshDetails)
        connection.enable()
        
        try:
            Commands=["ip dhcp excluded-address 30.0.0.2","ip dhcp excluded-address 30.0.0.3","ip dhcp pool R2","host 30.0.0.2 255.255.255.0","client-identifier 0063.6973.636f.2d63.6130.322e.3331.6231.2e30.3030.302d.4661.302f.30","exit","ip dhcp pool R3","host 30.0.0.3 255.255.255.0","client-identifier 0063.6973.636f.2d63.6130.332e.3331.6330.2e30.3030.302d.4661.302f.30","exit","ip dhcp pool v4","network 30.0.0.0 255.255.255.0"]
            # Commands=["interface loopback 5"]
            output=connection.send_config_set(Commands)
            time.sleep(60)
           
            if "%" in output:
                print("ERROR - Invalid Command")
                print(output)
                return
            
        except Exception as e:
            print("!!!")
            print("Exception occured - see below")
            print(e)
            print("!!!")
        print("Done for:" + RouterSshDetails["host"])
        connection.disconnect()
    except Exception as e:
        print("something went wrong in sshAndExecuteCommands Call for "+RouterSshDetails["host"])
        print(e)

def getIPv6AddressOfR5usingCDPinR2(RouterSshDetails):
    try:
        connection = ConnectHandler(**RouterSshDetails)
        connection.enable()
        
        # Commands=["do show run | inc pool","","","",""]
        Commands=["do show cdp entry R5.do.name"]
        output=connection.send_config_set(Commands)
        # print(output)
        if "%" in output:
            print("ERROR - Invalid Command")
            print(output)
            return
        
        # print("Done for:" + RouterSshDetails["host"])
        connection.disconnect()
        neighbor=re.search('IPv6 address: +(.*[0-9,A-Z]) +\(global unicast\)',output)
        ip=neighbor.group(1)
        # print(ip)
        return ip
    except Exception as e:
        print("something went wrong in getIPv6AddressOfR5usingCDPinR2 Call for "+RouterSshDetails["host"])
        print(e)
    
def getIPv4Bindings(RouterSshDetails):
    try:
        connection = ConnectHandler(**RouterSshDetails)
        connection.enable()
       
        output=connection.send_config_set("do show ip dhcp binding")
        print(output)
        # print(output)
        if "%" in output:
            print("ERROR - Invalid Command")
            print(output)
            return
        
        # return output
    except Exception as e:
        print("something went wrong in getIPv4Bindings Call for "+RouterSshDetails["host"])
        print(e)

    
    
