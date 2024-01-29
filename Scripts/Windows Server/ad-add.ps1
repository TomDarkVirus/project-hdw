# Script to add a server to an existing Active Directory domain

# Specify the existing domain name
$ExistingDomain = "ijsselstreek-university.nl"

# Prompt for domain credentials
$Credential = Get-Credential -Message "Enter domain credentials"

# Add the server to the existing domain
Add-Computer -DomainName $ExistingDomain -Credential $Credential -Restart -Force
