# Set DNS server
$dnsServer = "10.10.0.14"
netsh interface ipv4 set dns "Ethernet" static $dnsServer

# Specify domain information
$domainName = "ijsselstreek-university.nl"
$domainAdmin = "administrator1"
$domainAdminPassword = "Wachtwoord123"

# Join the server to the domain
Add-Computer -DomainName $domainName -Credential (Get-Credential -UserName $domainAdmin -Message "Enter domain administrator credentials")

# Install AD DS (Active Directory Domain Services) role
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote the server to a domain controller
Install-ADDSDomainController -InstallDns -DomainName $domainName -Credential (Get-Credential -UserName $domainAdmin -Message "Enter domain administrator credentials") -Force -NoRebootOnCompletion

# Reboot the server
Restart-Computer -Force
