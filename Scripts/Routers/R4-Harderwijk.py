from netmiko import ConnectHandler
import getpass

# Define 'passwd' to prompt the user for a password
passwd = getpass.getpass('Please enter password: ')

# Create a dictionary with device information needed for SSH connection
Harderwijk = {
    "device_type": "cisco_ios",
    "host": "10.201.20.64",
    "username": "admin",
    "password": passwd,
    "secret": passwd
}

# Setup the connection to the device
connection = ConnectHandler(**Harderwijk)

# Define command needed for hostname configuration
hostname_config = [
    'hostname R4-Harderwijk'
]

# Define command needed for domain name configuration
domain_name_config = [
    'ip domain name ijsselstreek-university.nl'
]

# Define commands needed for NTP configuration
ntp_config = [
    'ntp server 10.10.0.14',
    'clock timezone CET 1'
]

# Define command needed for DNS configuration
dns_config = [
    'ip name-server 10.10.0.14'
]

# Define commands needed for VLAN configuration
vlan_config = [
    'vlan 10', 'name ISP-1',
    'vlan 11', 'name ISP-2',
    'vlan 20', 'name Systeembeheer',
    'vlan 30', 'name Directie',
    'vlan 40', 'name Docenten',
    'vlan 50', 'name Staff',
    'vlan 60', 'name Gasten',
    'vlan 70', 'name Studenten'
]

# Define commands needed for loopback address
loopback_config = [
    'interface loopback1', 'ip address 10.201.20.64 255.255.255.255'
]

# Define commands needed for SVI ipv4 configuration
svi_ipv4_config = [
    'interface Vlan10', 'ip address 10.1.3.1 255.255.255.252',
    'interface Vlan11', 'ip address 10.1.4.1 255.255.255.252',
    'interface Vlan20', 'ip address 10.201.20.1 255.255.255.192',
    'interface Vlan30', 'ip address 10.201.30.1 255.255.255.192',
    'interface Vlan40', 'ip address 10.201.40.1 255.255.255.0',
    'interface Vlan50', 'ip address 10.201.50.1 255.255.255.0',
    'interface Vlan60', 'ip address 10.201.60.1 255.255.252.0',
    'interface Vlan70', 'ip address 10.201.64.1 255.255.240.0'
]

# Define commands needed for L3 interface ipv4 configuration
l3_interface_ipv4_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.0.5.1 255.255.255.252',
    'interface GigabitEthernet0/0/1', 'ip address 10.0.5.5 255.255.255.252'
]

# Define commands needed for L3 interface ipv6 configuration
l3_interface_ipv6_config = [
    'interface GigabitEthernet0/0/0', 'ipv6 address 200:200:20:2::/64 eui-64',
    'interface GigabitEthernet0/0/1', 'ipv6 address 200:200:20:1::/64 eui-64',
    'ipv6 unicast-routing'
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet0/1/0', 'switchport mode trunk', 'switchport trunk allowed vlan none', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet0/1/1', 'switchport mode trunk', 'switchport trunk allowed vlan none', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet0/1/2', 'switchport mode access', 'switchport access vlan 10',
    'interface GigabitEthernet0/1/3', 'switchport mode access', 'switchport access vlan 11'
]

# Define commands needed for Port Security configuration
port_security_config = [
    'interface GigabitEthernet0/1/2', 'switchport port-security', 'switchport port-security maximum 1', 'switchport port-security violation shutdown', 'switchport port-security mac-address sticky',
    'interface GigabitEthernet0/1/3', 'switchport port-security', 'switchport port-security maximum 1', 'switchport port-security violation shutdown', 'switchport port-security mac-address sticky'
]

# Define commands needed for DHCP with ipv4 configuration
dhcp_ipv4_config = [
    'ip dhcp excluded-address 10.201.20.1 10.201.20.10', 'ip dhcp pool Vlan20', 'network 10.201.20.0 255.255.255.192', 'default-router 10.201.20.1', 'lease 0 8',
    'ip dhcp excluded-address 10.201.30.1 10.201.30.5', 'ip dhcp pool Vlan30', 'network 10.201.30.0 255.255.255.192', 'default-router 10.201.30.1', 'lease 0 8',
    'ip dhcp excluded-address 10.201.40.1 10.201.40.5', 'ip dhcp pool Vlan40', 'network 10.201.40.0 255.255.255.0', 'default-router 10.201.40.1', 'lease 0 8',
    'ip dhcp excluded-address 10.201.50.1 10.201.50.5', 'ip dhcp pool Vlan50', 'network 10.201.50.0 255.255.255.0', 'default-router 10.201.50.1', 'lease 0 8',
    'ip dhcp excluded-address 10.201.60.1 10.201.60.5', 'ip dhcp pool Vlan60', 'network 10.201.60.0 255.255.252.0', 'default-router 10.201.60.1', 'lease 0 8',
    'ip dhcp excluded-address 10.201.64.1 10.201.64.5', 'ip dhcp pool Vlan70', 'network 10.201.64.0 255.255.240.0', 'default-router 10.201.64.1', 'lease 0 8',
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 4.4.4.4',
    'network 10.0.5.0 0.0.0.3 area 0',
    'network 10.0.5.4 0.0.0.3 area 0',
    'network 10.1.0.0 0.0.7.255 area 0',
    'network 10.201.0.0 0.0.255.255 area 4',
    'network 10.202.0.0 0.0.255.255 area 5',
    'network 10.203.0.0 0.0.255.255 area 6',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 200',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 200'
]

# Define commands needed for OSPFv3 configuration
ospfv3_config = [
    'router ospfv3 1',
    'router-id 4.4.4.4',
    'interface GigabitEthernet0/0/0', 'ospfv3 1 area 0 ipv6', 'ospfv3 priority 200',
    'interface GigabitEthernet0/0/1', 'ospfv3 1 area 0 ipv6', 'ospfv3 priority 200'
]

# Define commands needed for static routing configuration
static_route_config = [
    'ip route 0.0.0.0 0.0.0.0 10.1.3.2',
    'ip route 10.12.1.0 255.255.255.252 10.0.5.2',
    'ip route 10.12.2.0 255.255.255.252 10.0.5.2',
    'ip route 10.69.42.0 255.255.255.252 10.1.3.2',
    'ip route 172.16.0.0 255.255.0.0 10.0.5.2',
    'ip route 192.168.13.0 255.255.255.0 10.0.5.2'

]

# Define commands needed for MSTP configuration
mstp_config = [
    'spanning-tree mode mst',
    'spanning-tree mst configuration',
    'revision 1',
    'name Harderwijk',
    'instance 1 vlan 20,30,40,50,60,70',
    'spanning-tree mst 1 priority 0'
]

# Define commmands needed for Radius configuration
radius_config = [
    'aaa group server radius azure',
    'server name azure',
    'radius server azure',
    'address ipv4 10.10.0.14',
    'key Wachtwoord123',
    'exit',
    'aaa authentication login default group azure local'
]

# Defina commands needed to execute commands with printing funtion as visual check
result = connection.send_config_set(hostname_config)
print(result)

result = connection.send_config_set(domain_name_config)
print(result)

result = connection.send_config_set(ntp_config)
print(result)

result = connection.send_config_set(dns_config)
print(result)

result = connection.send_config_set(vlan_config)
print(result)

result = connection.send_config_set(loopback_config)
print(result)

result = connection.send_config_set(svi_ipv4_config)
print(result)

result = connection.send_config_set(l3_interface_ipv4_config)
print(result)

result = connection.send_config_set(l3_interface_ipv6_config)
print(result)

result = connection.send_config_set(l2_interface_config)
print(result)

result = connection.send_config_set(port_security_config)
print(result)

result = connection.send_config_set(dhcp_ipv4_config)
print(result)

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(ospfv3_config)
print(result)

result = connection.send_config_set(static_route_config)
print(result)

result = connection.send_config_set(mstp_config)
print(result)

result = connection.send_config_set(radius_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()