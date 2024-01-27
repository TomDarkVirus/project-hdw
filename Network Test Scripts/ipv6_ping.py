from netmiko import ConnectHandler
import getpass
import re

# Define variables to prompt the user for ip address and login credentials
ip_address = input('Please enter the IP ADDRESS of the device to connect to: ')
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
enable = getpass.getpass('Please enter the EXEC password: ')

# Create a dictionary with device information needed for SSH connection
Device = {
    "device_type": "cisco_ios",
    "host": ip_address,
    "username": username,
    "password": password,
    "secret": enable
}

# Ping commands with device and interface information
ping_commands = [
    {'router_name': 'R1-Deventer', 'command': 'ping 200:100:20:1:A611:BBFF:FE86:6590', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R1-Deventer', 'command': 'ping 200:100:20:3:A611:BBFF:FE86:6591', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R2-Ermelo', 'command': 'ping 200:100:20:2:A611:BBFF:FE85:F360', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R2-Ermelo', 'command': 'ping 200:100:20:1:A611:BBFF:FE85:F361', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R2-Ermelo', 'command': 'ping 200:150:20:1:A611:BBFF:FE85:F3E4', 'interface': 'VLAN8'},
    {'router_name': 'R3-Epe', 'command': 'ping 200:100:20:3:A611:BBFF:FE3B:1EE0', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R3-Epe', 'command': 'ping 200:100:20:2:A611:BBFF:FE3B:1EE1', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R4-Harderwijk', 'command': 'ping 200:200:20:2:A611:BBFF:FE3B:1160', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R4-Harderwijk', 'command': 'ping 200:200:20:1:A611:BBFF:FE3B:1161', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R5-Nunspeet', 'command': 'ping 200:200:20:3:A611:BBFF:FE86:51E0', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R5-Nunspeet', 'command': 'ping 200:200:20:1:A611:BBFF:FE86:51E1', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R6-Putten', 'command': 'ping 200:200:20:2:A611:BBFF:FE85:C9C0', 'interface': 'GigabitEthernet0/0/0'},
    {'router_name': 'R6-Putten', 'command': 'ping 200:200:20:3:A611:BBFF:FE85:C9C1', 'interface': 'GigabitEthernet0/0/1'},
    {'router_name': 'R6-Putten', 'command': 'ping 200:150:20:1:A611:BBFF:FE85:CA44', 'interface': 'VLAN8'}
]

# Connect to the device, execute ping commands and print the result with device information
def run_ping_commands(device, ping_commands):
    try:
        connection = ConnectHandler(**device)
        print(" ")
        print(f"Connected to {device['host']}")
        print(" ")

        for ping_info in ping_commands:
            router_name = ping_info['router_name']
            ping_command = ping_info['command']
            interface = ping_info['interface']

            output = connection.send_command(ping_command)
            ping_result = re.search(r"Success rate is (\d+)", output)
            success_rate = ping_result.group(1) if ping_result else "N/A"
            print(f"{router_name:13s} | {interface:20s} | {ping_command:38s} | Success Rate: {success_rate}%")

    except Exception as e:
        print(f"Error connecting to {device['host']}: {str(e)}")

    finally:
        connection.disconnect()
        print(" ")
        print(f"Disconnected from {device['host']}\n")

# Execute ping commands for the specified router
run_ping_commands(Device, ping_commands)