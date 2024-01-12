# Deze commando's moeten handmatig worden uigevoerd zodat er een SSH verbinding mogelijk is voor automatisering.
# Bij de regels waar ##### staat dient de gebruiker een eigen wachtwoord in te voeren.

# Switches

ip ssh server
ip ssh password-auth

# Routers

ip domain-name IJsselstreek.edu

enable secret level 15 #####
username ##### secret #####

ip ssh version 2
crypt key generate rsa
2048
line vty 0 15
password #####
login local
transport input ssh