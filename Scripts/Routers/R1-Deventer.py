from netmiko import ConnectHandler
import getpass

# Define variables to prompt the user for login credentials
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
enable = getpass.getpass('Please enter the EXEC password: ')

# Create a dictionary with device information needed for SSH connection
Deventer = {
    "device_type": "cisco_ios",
    "host": "10.101.20.64",
    "username": username,
    "password": password,
    "secret": enable
}

# Setup the connection to the device
connection = ConnectHandler(**Deventer)
connection.enable()

# Define command needed for hostname configuration
hostname_config = [
    'hostname R1-Deventer'
]

# Define command needed for domain name configuration
domain_name_config = [
    'ip domain name ijsselstreek-university.nl'
]

# Define commands needed for NTP configuration
ntp_config = [
    'ntp server 10.10.0.14',
    'ntp server 192.168.13.99',
    'clock timezone CET 1'
]

# Define commands needed for DNS configuration
dns_config = [
    'ip name-server 10.10.0.14',
    'ip name-server 10.10.0.15',
    'ip name-server 192.168.13.99',
    'ip name-server 192.168.13.150'
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
    'interface loopback1', 'ip address 10.101.20.64 255.255.255.255'
]

# Define commands needed for SVI ipv4 configuration
svi_ipv4_config = [
    'interface Vlan10', 'ip address 192.168.100.3 255.255.255.0',
    'interface Vlan11', 'ip address 192.168.200.2 255.255.255.0',
    'interface Vlan20', 'ip address 10.101.20.1 255.255.255.192', 'ip helper-address 192.168.13.41',
    'interface Vlan30', 'ip address 10.101.30.1 255.255.255.192', 'ip helper-address 192.168.13.41',
    'interface Vlan40', 'ip address 10.101.40.1 255.255.255.0', 'ip helper-address 192.168.13.41',
    'interface Vlan50', 'ip address 10.101.50.1 255.255.255.0', 'ip helper-address 192.168.13.41',
    'interface Vlan60', 'ip address 10.101.60.1 255.255.252.0', 'ip helper-address 192.168.13.41',
    'interface Vlan70', 'ip address 10.101.64.1 255.255.240.0', 'ip helper-address 192.168.13.41'
]

# Define commands needed for L3 interface ipv4 configuration
l3_interface_ipv4_config = [
    'interface GigabitEthernet0/0/0', 'ip address 10.0.6.6 255.255.255.252',
    'interface GigabitEthernet0/0/1', 'ip address 10.0.6.1 255.255.255.252'
]

# Define commands needed for L3 interface ipv6 configuration
l3_interface_ipv6_config = [
    'interface GigabitEthernet0/0/0', 'ipv6 address 200:100:20:1::/64 eui-64',
    'interface GigabitEthernet0/0/1', 'ipv6 address 200:100:20:3::/64 eui-64',
    'ipv6 unicast-routing'
]

# Define commands needed for L2 interface configuration
l2_interface_config = [
    'interface GigabitEthernet0/1/0', 'switchport mode trunk', 'switchport trunk allowed vlan add 20,30,40,50,60,70',
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
    'ip dhcp relay information option',
    'ip dhcp pool Vlan20', 'relay source 10.101.20.0 255.255.255.192', 'relay destination 192.168.13.41',
    'ip dhcp pool Vlan30', 'relay source 10.101.30.0 255.255.255.192', 'relay destination 192.168.13.41',
    'ip dhcp pool Vlan40', 'relay source 10.101.40.0 255.255.255.0', 'relay destination 192.168.13.41',
    'ip dhcp pool Vlan50', 'relay source 10.101.50.0 255.255.255.0', 'relay destination 192.168.13.41',
    'ip dhcp pool Vlan60', 'relay source 10.101.60.0 255.255.252.0', 'relay destination 192.168.13.41',
    'ip dhcp pool Vlan70', 'relay source 10.101.64.0 255.255.240.0', 'relay destination 192.168.13.41'
]

# Define commands needed for OSPF configuration
ospf_config = [
    'router ospf 1',
    'router-id 1.1.1.1',
    'network 10.0.6.0 0.0.0.3 area 0',
    'network 10.0.6.4 0.0.0.3 area 0',
    'network 10.101.20.64 0.0.0.0 area 0',
    'network 10.101.0.0 0.0.255.255 area 1',
    'network 10.102.0.0 0.0.255.255 area 2',
    'network 10.103.0.0 0.0.255.255 area 3',
    'network 192.168.100.0 0.0.0.255 area 0',
    'network 192.168.200.0 0.0.0.255 area 0',
    'interface GigabitEthernet0/0/0', 'ip ospf priority 200',
    'interface GigabitEthernet0/0/1', 'ip ospf priority 200'
]

# Define commands needed for OSPFv3 configuration
ospfv3_config = [
    'router ospfv3 1',
    'router-id 1.1.1.1',
    'interface GigabitEthernet0/0/0', 'ospfv3 1 area 0 ipv6', 'ospfv3 1 ipv6 priority 200',
    'interface GigabitEthernet0/0/1', 'ospfv3 1 area 0 ipv6', 'ospfv3 1 ipv6 priority 200'
]

# Define commands needed for static routing configuration
static_route_config = [
    'ip route 0.0.0.0 0.0.0.0 192.168.100.1',
    'ip route 10.10.0.0 255.255.0.0 10.0.6.5',
    'ip route 10.12.1.0 255.255.255.252 192.168.100.1',
    'ip route 10.12.2.0 255.255.255.252 192.168.200.1',
    'ip route 10.69.42.0 255.255.255.252 10.0.6.5',
    'ip route 172.16.0.0 255.255.0.0 192.168.100.1',
    'ip route 192.168.13.0 255.255.255.0 192.168.100.1'
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

# Define Commands needed for SNMP configuration
snmp_config = [
    'snmp-server community comp-comm RO',
    'snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart',
    'snmp-server host 10.10.0.9 version 2c comp-comm'
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

result = connection.send_config_set(radius_config)
print(result)

result = connection.send_config_set(snmp_config)
print(result)

# Disconnect the SSH connection with the device
connection.disconnect()