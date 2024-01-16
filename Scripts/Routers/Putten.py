from netmiko import ConnectHandler
import getpass

# Define 'passwd' to prompt the user for a password
passwd = getpass.getpass('Please enter password: ')

# Define device information needed for SSH connection
Putten = {
    "device_type": "cisco_ios",
    "host": "10.200.20.3",
    "username": "Putten",
    "password": passwd,
    "secret": passwd
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

# Define commands needed for L3 interface ipv4 configuration
l3_interface_ipv4_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.0.5.2 255.255.255.240',
    'interface GigabitEthernet0/0/1', 'ip address 10.0.5.10 255.255.255.240'
]

# Define commands needed for L3 interface ipv6 configuration
l3_interface_ipv6_config = [
    'interface GigabitEthernet0/0/0', 'ipv6 address 200:200:20:2::/64 eui-64', 'ipv6 enable',
    'interface GigabitEthernet0/0/1', 'ipv6 address 200:200:20:3::/64 eui-64', 'ipv6 enable',
    'ipv6 unicast-routing'
]

# Define commands needed for SVI ipv4 configutation
svi_ipv4_config = [
    'interface GigabitEthernet0/0/0.20', 'encapsulation dot1Q 20', 'ip address 10.200.20.3 255.255.255.192',
    'interface GigabitEthernet0/0/0.30', 'encapsulation dot1Q 30', 'ip address 10.200.30.3 255.255.255.192',
    'interface GigabitEthernet0/0/0.40', 'encapsulation dot1Q 40', 'ip address 10.200.40.3 255.255.255.0',
    'interface GigabitEthernet0/0/0.50', 'encapsulation dot1Q 50', 'ip address 10.200.50.3 255.255.255,0',
    'interface GigabitEthernet0/0/0.60', 'encapsulation dot1Q 60', 'ip address 10.200.60.3 255.255.252.0',
    'interface GigabitEthernet0/0/0.70', 'encapsulation dot1Q 70', 'ip address 10.200.64.3 255.255.240.0'
]

# Define commands needed for SVI ipv6 configutation
svi_ipv6_config = [

]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 2.2.2.2',
    'network 10.0.5.0 0.0.0.3 area 0',
    'network 10.0.5.8 0.0.0.3 area 0',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 0',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 0'
]

# Define commands needed for OSPFv3 configuration
ospfv3_config = [
    'ipv6 router ospf 1',
    'router-id 3.3.3.3',
    'interface GigabitEthernet0/0/0', 'ipv6 ospf 1 area 0', 'ipv6 ospfv3 priority 0',
    'interface GigabitEthernet0/0/1', 'ipv6 ospf 1 area 0', 'ipv6 ospfv3 priority 0'
]

# Define commands needed for ACL configuration
acl_config = [
    'ip access-list extended 20',
    'remark allow SSH on VLAN20',
    'permit 10.200.20.0 0.0.0.63',
    'line vty 15',
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

result = connection.send_config_set(l3_interface_ipv4_config)
print(result)

result = connection.send_config_set(svi_ipv4_config)
print(result)

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(ospfv3_config)
print(result)

result = connection.send_config_set(acl_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()