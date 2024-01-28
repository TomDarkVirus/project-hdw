from netmiko import ConnectHandler
import getpass

# Define variables to prompt the user for ip address and login credentials
ip_address = input('Please enter the IP ADDRESS of the device to connect to: ')
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
enable = getpass.getpass('Please enter the EXEC password: ')
new_line_password = getpass.getpass('Please enter the new line password for vty 0 15: ')

# Create a dictionary with device information needed for SSH connection
Device = {
    "device_type": "cisco_ios",
    "host": ip_address,
    "username": username,
    "password": password,
    "secret": enable
}

# Setup the SSH connection to the device
connection = ConnectHandler(**Device)
connection.enable()

# Change the line password for vty 0 15
config_commands = [f'line vty 0 15', f'password {new_line_password}']
output = connection.send_config_set(config_commands)
print(output)

# Disconnect the SSH connection with the device
connection.disconnect()
