#!/bin/bash

# Check of er genoeg argumenten zijn doorgegeven
if [ "$#" -ne 3 ]; then
    echo "Gebruik: $0 <IP_ADRES> <HOSTNAAM> <GRAYLOG_SERVER_IP>"
    exit 1
fi

IP_ADRES=$1
HOSTNAAM=$2
GRAYLOG_SERVER_IP=$3

# Vraag om SSH inloggegevens
read -p "Voer SSH gebruikersnaam in: " SSH_GEBRUIKER
read -sp "Voer SSH wachtwoord in: " SSH_WACHTWOORD
echo

# Installeer sshpass indien nog niet geïnstalleerd (optioneel, voor niet-interactieve S>
if ! command -v sshpass &> /dev/null
then
    echo "sshpass is niet gevonden, wordt geïnstalleerd..."
    sudo apt-get install -y sshpass  # Of gebruik yum als het een CentOS/RHEL server is
fi

# Functie om NCPA te installeren en rsyslog te configureren op de remote server
installeer_ncpa_en_configureer_rsyslog() {
    echo "NCPA wordt geïnstalleerd en rsyslog wordt geconfigureerd op $HOSTNAAM ($IP_AD>

    sshpass -p "$SSH_WACHTWOORD" ssh -o StrictHostKeyChecking=no $SSH_GEBRUIKER@$IP_ADR>
        # Installeer NCPA
        wget https://assets.nagios.com/downloads/ncpa3/ncpa_3.0.1-latest-1_amd64.deb -O>
        sudo dpkg -i ncpa.deb
        sudo systemctl start ncpa
        sudo systemctl enable ncpa

        # Pas het token aan naar 'Groep5'
        sudo sed -i "s/^community_string =.*/community_string = \"Groep5\"/" /usr/local>
        sudo systemctl restart ncpa

        # Pas log level aan naar 'error'
        sudo sed -i "s/.*loglevel =.*/loglevel = error/" /usr/local/ncpa/etc/ncpa.cfg
        sudo systemctl restart ncpa

        # Installeer en configureer rsyslog
        sudo apt-get install -y rsyslog
        echo "*.* @@'$GRAYLOG_SERVER_IP':1514;RSYSLOG_SyslogProtocol23Format" | sudo te>
        sudo systemctl restart rsyslog
    '
}

# Voer de installatie- en configuratiefunctie uit
installeer_ncpa_en_configureer_rsyslog
