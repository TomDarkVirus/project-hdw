# Define parameters
$domainName = "ijsselstreek-university.nl"
$domainAdministrator = "administrator1"
$domainAdminPassword = Read-Host -Prompt "Enter password for $domainAdministrator" -AsSecureString

# Install Active Directory Domain Services
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Create a new Active Directory forest
Install-ADDSForest -DomainName $domainName -DomainNetBIOSName TEST -InstallDNS
