from netmiko import ConnectHandler
import getpass

# Define variables to prompt the user for a login credentials
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')

# Create a dictionary with device information needed for SSH connection
Brinklaan = {
    "device_type": "cisco_s300",
    "host": "10.101.20.4",
    "username": username,
    "password": password
}

# Setup the SSH connection to the device
connection = ConnectHandler(**Brinklaan)

# Define command needed for hostname configuration
hostname_config = [
    'hostname SW3-Brinklaan'
]

# Defina command needed for domain name configuration
domain_name_config = [
    'ip domain name ijsselstreek-university.nl'
]

# Define commands needed for SNTP configuration
sntp_config = [
    'sntp server 10.10.0.14',
    'sntp server 192.168.13.99',
    'clock timezone CET 1'
]

# Define command needed for DNS configuration
dns_config = [
    'ip name-server 10.10.0.14 10.10.0.15 192.168.13.99 192.168.13.150'
]

# Define commands needed for VLAN configuration
vlan_config = [
    'vlan 20 name Systeembeheer',
    'vlan 30 name Directie',
    'vlan 40 name Docenten',
    'vlan 50 name Staff',
    'vlan 60 name Gasten',
    'vlan 70 name Studenten'
]

# Define commands needed for SVI ipv4 configuration
svi_ipv4_config = [
    'interface Vlan20', 'ip address 10.101.20.4 255.255.255.192',
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet 1', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet 2', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
]

# Define command needed for default gateway configuration
default_gateway_config = [
    'ip default-gateway 10.101.20.1'
]

# Define commands needed for MSTP configuration
mstp_config = [
    'spanning-tree mode mst',
    'spanning-tree mst configuration',
    'revision 1',
    'name Deventer',
    'instance 1 vlan 20,30,40,50,60,70',
    'spanning-tree mst 1 priority 8192'
]

# Defina commands needed to execute commands with printing funtion as visual check
result = connection.send_config_set(hostname_config)
print(result)

result = connection.send_config_set(domain_name_config)
print(result)

result = connection.send_config_set(sntp_config)
print(result)

result = connection.send_config_set(dns_config)
print(result)

result = connection.send_config_set(vlan_config)
print(result)

result = connection.send_config_set(svi_ipv4_config)
print(result)

result = connection.send_config_set(l2_interface_config)
print(result)

result = connection.send_config_set(default_gateway_config)
print(result)

result = connection.send_config_set(mstp_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()