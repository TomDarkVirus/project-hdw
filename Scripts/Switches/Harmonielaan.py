from netmiko import ConnectHandler

# Define device information needed for SSH connection
Harmonielaan = {
    "device_type": "cisco_s300",
    "host": "10.200.20.5",
    "username": "Harmonielaan",
    "password": "Wachtwoord12!"
}

# Setup the SSH connection to the device
connection = ConnectHandler(**Harmonielaan)

# Define command needed for hostname configuration
hostname_config = [
    'hostname SW5-Harmonielaan'
]

# Defina command needed for domain name configuration
domain_name_config = [
    'ip domain name IJsselstreek.edu'
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

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet 1', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet 2', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet 3', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70'
]

# Define commands needed for MSTP configuration
mstp_config = [
    'spanning-tree mode mst',
    'spanning-tree mst configuration',
    'revision 1',
    'name Harderwijk',
    'instance 1 vlan 20,30,40,50,60,70,80',
    'spanning-tree mst 1 priority 8192'
]

# Defina commands needed to execute commands with printing funtion as visual check
result = connection.send_config_set(hostname_config)
print(result)

result = connection.send_config_set(domain_name_config)
print(result)

result = connection.send_config_set(vlan_config)
print(result)

result = connection.send_config_set(l2_interface_config)
print(result)

result = connection.send_config_set(mstp_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()