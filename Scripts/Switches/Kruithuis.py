from netmiko import ConnectHandler
import getpass

# Define 'passwd' to prompt the user for a password
passwd = getpass.getpass('Please enter password: ')

# Create a dictionary with device information needed for SSH connection
Westeinde = {
    "device_type": "cisco_s300",
    "host": "10.201.20.4",
    "username": "admin",
    "password": passwd
}

# Setup the SSH connection to the device
connection = ConnectHandler(**Westeinde)

# Define command needed for hostname configuration
hostname_config = [
    'hostname SW6-Kruithuis'
]

# Defina command needed for domain name configuration
domain_name_config = [
    'ip domain name ijsselstreek-university.nl'
]

# Define commands needed for SNTP configuration
sntp_config = [
    'sntp server 10.10.0.14',
    'clock timezone CET 1'
]

# Define command needed for DNS configuration
dns_config = [
    'ip name-server 10.10.0.14'
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
    'interface Vlan20', 'ip address 10.201.20.4 255.255.255.192',
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet 1', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet 2', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet 3', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70'
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

# Disconnect the SSH connection with the device
connection.disconnect()