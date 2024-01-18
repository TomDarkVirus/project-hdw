# Define parameters
$domainName = "test.local"
$domainAdministrator = "administrator1"
$domainAdminPassword = Read-Host -Prompt "Enter password for $domainAdministrator" -AsSecureString

# Install Active Directory Domain Services
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Create a new Active Directory forest
Install-ADDSForest -DomainName $domainName -DomainMode Default -ForestMode Default -CreateDnsDelegation:$false -Force:$true -InstallDns

# Promote the server to a domain controller
Install-ADDSDomainController -DomainName $domainName -InstallDns -Credential (New-Object System.Management.Automation.PSCredential($domainAdministrator, $domainAdminPassword)) -Force:$true

Write-Host "Domain creation and promotion to domain controller completed successfully."
