from netmiko import ConnectHandler

# Define device information needed for SSH connection
Putten = {
    "device_type": "cisco_ios",
    "host": "10.200.20.3",
    "username": "Putten",
    "password": "Wachtwoord12!",
    "secret": "Wachtwoord12!"
}

# Setup the connection to the device
connection = ConnectHandler(**Putten)

# Define command needed for hostname configuration
hostname_config = [
    'hostname RT6-Putten'
]

# Defina command needed for domain name configuration
domain_name_config = [
    'ip domain name IJsselstreek.edu'
]

# Define commands needed for NTP configuration
ntp_config = [
    'ntp server 10.10.0.7'
    'clock timezone CET 1'
]

# Define command needed for DNS configuration
dns_config = [
    'ip name-server 10.10.0.7'
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

# Define commands needed for L3 interface configuration
l3_interface_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.168.0.131 255.255.255.240',
    'interface GigabitEthernet0/0/1', 'ip address 10.168.0.67 255.255.255.240'
]

# Define commands needed for SVI configutation
svi_config = [
    'interface GigabitEthernet0/0/0.20', 'encapsulation dot1Q 20', 'ip address 10.200.20.3 255.255.255.192',
    'interface GigabitEthernet0/0/0.30', 'encapsulation dot1Q 30', 'ip address 10.200.30.3 255.255.255.192',
    'interface GigabitEthernet0/0/0.40', 'encapsulation dot1Q 40', 'ip address 10.200.40.3 255.255.255.0',
    'interface GigabitEthernet0/0/0.50', 'encapsulation dot1Q 50', 'ip address 10.200.50.3 255.255.255,0',
    'interface GigabitEthernet0/0/0.60', 'encapsulation dot1Q 60', 'ip address 10.200.60.3 255.255.252.0',
    'interface GigabitEthernet0/0/0.70', 'encapsulation dot1Q 70', 'ip address 10.200.64.3 255.255.240.0'
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 2.2.2.2',
    'network 10.168.0.64 0.0.0.15 area 0',
    'network 10.168.0.128 0.0.0.15 area 0',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 100',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 100'
]

# Define commands needed for ACL configuration
acl_config = [
    'ip access-list extended 20',
    'remark allow SSH on VLAN20',
    'permit 10.200.20.0 0.0.0.63'
    'line vty 15'
    'access-class 20 in'
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

result = connection.send_config_set(l3_interface_config)
print(result)

result = connection.send_config_set(svi_config)
print(result)

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(acl_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()