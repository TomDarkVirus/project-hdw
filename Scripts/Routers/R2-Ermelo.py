from netmiko import ConnectHandler
import getpass

# Define variables to prompt the user for a login credentials
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
enable = getpass.getpass('Please enter the EXEC password: ')

# Create a dictionary with device information needed for SSH connection
Ermelo = {
    "device_type": "cisco_ios",
    "host": "10.102.20.64",
    "username": username,
    "password": password,
    "secret": enable
}

# Setup the connection to the device
connection = ConnectHandler(**Ermelo)
connection.enable()

# Define command needed for hostname configuration
hostname_config = [
    'hostname R2-Ermelo'
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
    'vlan 8', 'name Ermelo-Putten',
    'vlan 20', 'name Systeembeheer',
    'vlan 30', 'name Directie',
    'vlan 40', 'name Docenten',
    'vlan 50', 'name Staff',
    'vlan 60', 'name Gasten',
    'vlan 70', 'name Studenten'
]

# Define commands needed for loopback address
loopback_config = [
    'interface loopback1', 'ip address 10.102.20.64 255.255.255.255'
]

# Define commands needed for SVI ipv4 configuration
svi_ipv4_config = [
    'interface Vlan8', 'ip address 10.0.3.1 255.255.255.252',
    'interface Vlan20', 'ip address 10.102.20.1 255.255.255.192',
    'interface Vlan30', 'ip address 10.102.30.1 255.255.255.192',
    'interface Vlan40', 'ip address 10.102.40.1 255.255.255.0',
    'interface Vlan50', 'ip address 10.102.50.1 255.255.255.0',
    'interface Vlan60', 'ip address 10.102.60.1 255.255.252.0',
    'interface Vlan70', 'ip address 10.102.64.1 255.255.240.0'
]

# Define commands needed for SVI ipv6 configutation
svi_ipv6_config = [
    'interface Vlan8', 'ipv6 address 200:150:20:1::/64 eui-64'
]

# Define commands needed for L3 interface ipv4 configuration
l3_interface_ipv4_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.0.6.9 255.255.255.252',
    'interface GigabitEthernet0/0/1', 'ip address 10.0.6.5 255.255.255.252'
]

# Define commands needed for L3 interface ipv6 configuration
l3_interface_ipv6_config = [
    'interface GigabitEthernet0/0/0', 'ipv6 address 200:100:20:2::/64 eui-64',
    'interface GigabitEthernet0/0/1', 'ipv6 address 200:100:20:1::/64 eui-64',
    'ipv6 unicast-routing'
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet0/1/0', 'switchport mode access', 'switchport access vlan 8'
]

# Define commands needed for Port Security configuration
port_security_config = [
    'interface GigabitEthernet0/1/0', 'switchport port-security', 'switchport port-security maximum 1', 'switchport port-security violation shutdown', 'switchport port-security mac-address sticky',
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 2.2.2.2',
    'network 10.0.3.0 0.0.0.3 area 0',
    'network 10.0.6.4 0.0.0.3 area 0',
    'network 10.0.6.8 0.0.0.3 area 0',
    'network 10.102.20.64 0.0.0.0 area 0',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 100',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 100'
]

# Define commands needed for OSPFv3 configuration
ospfv3_config = [
    'router ospfv3 1',
    'router-id 2.2.2.2',
    'interface GigabitEthernet0/0/0', 'ospfv3 1 area 0 ipv6', 'ospfv3 1 ipv6 priority 100',
    'interface GigabitEthernet0/0/1', 'ospfv3 1 area 0 ipv6', 'ospfv3 1 ipv6 priority 100',
    'interface Vlan8', 'ospfv3 1 area 0 ipv6', 'ospfv3 1 ipv6 priority 100'
]

# Define commands needed for static routing configuration
static_route_config = [
    'ip route 0.0.0.0 0.0.0.0 10.0.6.6',
    'ip route 10.0.6.0 255.255.255.252 10.0.6.10',
    'ip route 10.10.0.0 255.255.0.0 10.0.3.2',
    'ip route 10.12.1.0 255.255.255.252 10.0.6.6',
    'ip route 10.12.2.0 255.255.255.252 10.0.6.6',
    'ip route 10.69.42.0 255.255.255.252 10.0.3.2',
    'ip route 172.16.0.0 255.255.0.0 10.0.6.6',
    'ip route 192.168.13.0 255.255.255.0 10.0.6.6',
    'ip route 192.168.100.0 255.255.255.0 10.0.6.6'
]

# Define commmands needed for Radius configuration
radius_config = [
    'aaa new-model',
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

result = connection.send_config_set(ospf_config)
print(result)

result = connection.send_config_set(ospfv3_config)
print(result)

result = connection.send_config_set(static_route_config)
print(result)

result = connection.send_config_set(radius_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()