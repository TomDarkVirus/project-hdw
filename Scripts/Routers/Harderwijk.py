from netmiko import ConnectHandler
import getpass

# Define 'passwd' to prompt the user for a password
passwd = getpass.getpass('Please enter password: ')

# Define device information needed for SSH connection
Harderwijk = {
    "device_type": "cisco_ios",
    "host": "10.200.20.1",
    "username": "Harderwijk",
    "password": passwd,
    "secret": passwd
}

# Setup the connection to the device
connection = ConnectHandler(**Harderwijk)

# Define command needed for hostname configuration
hostname_config = [
    'hostname RT4-Harderwijk'
]

# Define command needed for domain name configuration
domain_name_config = [
    'ip domain name IJsselstreek.edu'
]

# Define commands needed for NTP configuration
ntp_config = [
    'ntp server 10.10.0.14'
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

# Define commands needed for VLAN interface configuration
vlan_interface_config = [
    'interface Vlan10', 'ip address 10.1.3.1 255.255.255.252',
    'interface Vlan11', 'ip address 10.1.4.1 255.255.255.252'
]

# Define commands needed for L3 interface configuration
l3_interface_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.168.0.130 255.255.255.240',
    'interface GigabitEthernet0/0/1', 'ip address 10.168.0.34 255.255.255.240'
]

# Define commands needed for SVI configutation
svi_config = [
    'interface GigabitEthernet0/0/0.20', 'encapsulation dot1Q 20', 'ip address 10.200.20.1 255.255.255.192',
    'interface GigabitEthernet0/0/0.30', 'encapsulation dot1Q 30', 'ip address 10.200.30.1 255.255.255.192',
    'interface GigabitEthernet0/0/0.40', 'encapsulation dot1Q 40', 'ip address 10.200.40.1 255.255.255.0',
    'interface GigabitEthernet0/0/0.50', 'encapsulation dot1Q 50', 'ip address 10.200.50.1 255.255.255,0',
    'interface GigabitEthernet0/0/0.60', 'encapsulation dot1Q 60', 'ip address 10.200.60.1 255.255.252.0',
    'interface GigabitEthernet0/0/0.70', 'encapsulation dot1Q 70', 'ip address 10.200.64.1 255.255.240.0'
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet0/1/0', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet0/1/1', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
    'interface GigabitEthernet0/1/2', 'switchport mode access', 'switchport access vlan 10',
    'interface GigabitEthernet0/1/3', 'switchport mode access', 'switchport access vlan 11'
]

# Define commands needed for DHCP configuration
dhcp_config = [
    'ip dhcp excluded-address 10.200.20.1 10.200.20.10', 'ip dhcp pool Vlan20', 'network 10.200.20.0 255.255.255.192', 'default-router 10.200.20.1', 'lease 0 8',
    'ip dhcp excluded-address 10.200.30.1 10.200.30.5', 'ip dhcp pool Vlan30', 'network 10.200.30.0 255.255.255.192', 'default-router 10.200.30.1', 'lease 0 8',
    'ip dhcp excluded-address 10.200.40.1 10.200.40.5', 'ip dhcp pool Vlan40', 'network 10.200.40.0 255.255.255.0', 'default-router 10.200.40.1', 'lease 0 8',
    'ip dhcp excluded-address 10.200.50.1 10.200.50.5', 'ip dhcp pool Vlan50', 'network 10.200.50.0 255.255.255.0', 'default-router 10.200.50.1', 'lease 0 8',
    'ip dhcp excluded-address 10.200.60.1 10.200.60.5', 'ip dhcp pool Vlan60', 'network 10.200.60.0 255.255.252.0', 'default-router 10.200.60.1', 'lease 0 8',
    'ip dhcp excluded-address 10.200.64.1 10.200.64.5', 'ip dhcp pool Vlan70', 'network 10.200.64.0 255.255.240.0', 'default-router 10.200.64.1', 'lease 0 8'
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 1.1.1.1',
    'network 10.168.0.32 0.0.0.15 area 0',
    'network 10.168.0.128 0.0.0.15 area 0',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 200',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 200'
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

result = connection.send_config_set(vlan_interface_config)
print(result)

result = connection.send_config_set(l3_interface_config)
print(result)

result = connection.send_config_set(svi_config)
print(result)

result = connection.send_config_set(l2_interface_config)
print(result)

result = connection.send_config_set(dhcp_config)
print(result)

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(mstp_config)
print(result)

result = connection.send_config_set(acl_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()