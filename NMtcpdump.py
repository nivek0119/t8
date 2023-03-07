from scapy.all import *

def getMacFromIPv6Address(ipv6):
    #remove / "subnet" if given
    subnetIndex = ipv6.find("/")
    if subnetIndex != -1:
        ipv6 = ipv6[:subnetIndex]

    ipv6Partitions = ipv6.split(":")
    macPartitions = []
    for ipv6Partition in ipv6Partitions[-4:]:
        while len(ipv6Partition) < 4:
            ipv6Partition = "0" + ipv6Partition
        macPartitions.append(ipv6Partition[:2])
        macPartitions.append(ipv6Partition[-2:])

    # modifying partitions to match MAC value
    macPartitions[0] = "%02x" % (int(macPartitions[0], 16) ^ 2)
    # print(macPartitions)
    del macPartitions[4]
    del macPartitions[3]
    mac= ":".join(macPartitions)
    

    return [ipv6,mac]
    # return


# getmac = getMacFromIPv6Address(ipv6IP)
# print(getmac)

# ipv6IP=getmac[0]
# mac=getmac[1]


# print ("IPv6 Address:", ipv6IP)
# print ("MAC:", mac)