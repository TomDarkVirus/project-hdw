from netmiko import ConnectHandler
import getpass

# Define 'passwd' to prompt the user for a password
passwd = getpass.getpass('Please enter password: ')

# Create a dictionary with device information needed for SSH connection
Nunspeet = {
    "device_type": "cisco_ios",
    "host": "10.202.20.1",
    "username": "admin",
    "password": passwd,
    "secret": passwd
}

# Setup the connection to the device
connection = ConnectHandler(**Nunspeet)

# Define command needed for hostname configuration
hostname_config = [
    'hostname R5-Nunspeet'
]

# Defina command needed for domain name configuration
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
    'vlan 20', 'name Systeembeheer',
    'vlan 30', 'name Directie',
    'vlan 40', 'name Docenten',
    'vlan 50', 'name Staff',
    'vlan 60', 'name Gasten',
    'vlan 70', 'name Studenten'
]

# Define commands needed for SVI ipv4 configuration
svi_ipv4_config = [
    'interface Vlan20', 'ip address 10.202.20.1 255.255.255.192',
    'interface Vlan30', 'ip address 10.202.30.1 255.255.255.192',
    'interface Vlan40', 'ip address 10.202.40.1 255.255.255.0',
    'interface Vlan50', 'ip address 10.202.50.1 255.255.255.0',
    'interface Vlan60', 'ip address 10.202.60.1 255.255.252.0',
    'interface Vlan70', 'ip address 10.202.64.1 255.255.240.0'
]

# Define commands needed for L3 interface ipv4 configuration
l3_interface_ipv4_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.0.5.9 255.255.255.252',
    'interface GigabitEthernet0/0/1', 'ip address 10.0.5.6 255.255.255.252'
]

# Define commands needed for L3 interface ipv6 configuration
l3_interface_ipv6_config = [
    'interface GigabitEthernet0/0/0', 'ipv6 address 200:200:20:3::/64 eui-64',
    'interface GigabitEthernet0/0/1', 'ipv6 address 200:200:20:1::/64 eui-64',
    'ipv6 unicast-routing'
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 5.5.5.5',
    'network 10.0.5.4 0.0.0.3 area 0',
    'network 10.0.5.8 0.0.0.3 area 0',
    'network 10.1.0.0 0.0.7.255 area 0',
    'network 10.201.0.0 0.0.255.255 area 4',
    'network 10.202.0.0 0.0.255.255 area 5',
    'network 10.203.0.0 0.0.255.255 area 6',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 100',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 100'
]

# Define commands needed for OSPFv3 configuration
ospfv3_config = [
    'router ospfv3 1',
    'router-id 5.5.5.5',
    'interface GigabitEthernet0/0/0', 'ospfv3 1 area 0 ipv6', 'ospfv3 priority 100',
    'interface GigabitEthernet0/0/1', 'ospfv3 1 area 0 ipv6', 'ospfv3 priority 100'
]

# Define commands needed for static routing configuration
static_route_config = [
    'ip route 0.0.0.0 0.0.0.0 10.0.5.5'
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

result = connection.send_config_set(svi_ipv4_config)
print(result)

result = connection.send_config_set(l3_interface_ipv4_config)
print(result)

result = connection.send_config_set(l3_interface_ipv6_config)
print(result)

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(ospfv3_config)
print(result)

result = connection.send_config_set(static_route_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()