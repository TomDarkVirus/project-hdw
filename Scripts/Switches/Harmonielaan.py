from netmiko import ConnectHandler

# Define device information needed for SSH connection
Harmonielaan = {
    'device_type': 'cisco_sg300',
    'host': '',
    'username': '',
    'password': '',
    'secret': ''
}

# Setup the connection to the device
connection = ConnectHandler(**Harmonielaan)

