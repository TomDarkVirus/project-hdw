# Deze commando's moeten handmatig worden uigevoerd zodat er een SSH verbinding mogelijk is voor automatisering.
# Bij de regels waar ##### staat dient de gebruiker een eigen gebruikersnaam en wachtwoord in te voeren.
# De gebruiker en wachtwoord op de switch worden handmatig ingevoerd na een reset van het apparaat.

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