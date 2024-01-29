# Script to automate Active Directory installation and configuration

# Set your domain name and DSRM password
$DomainName = "ijsselstreek-university.nl"
$DSRMPassword = "Wachtwoord123"

# Install Active Directory Domain Services
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -Verbose

# Promote the server to a domain controller
Install-ADDSForest -DomainName $DomainName -DomainMode 4 -ForestMode 4 -InstallDns -Force -Verbose

# Set DSRM password
Set-LocalAdministratorPassword -Password (ConvertTo-SecureString -AsPlainText $DSRMPassword -Force) -Verbose

# Reboot the server
Restart-Computer -Force -Verbose
