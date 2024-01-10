from netmiko import ConnectHandler

# Define device information needed for SSH connection
Putten = {
    'device_type': 'cisco_ios',
    'host': '',
    'username': '',
    'password': '',
    'secret': ''
}

# Setup the connection to the device
connection = ConnectHandler(**Putten)

