# Import the Exchange Management Shell module
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn

# Get a list of users from Active Directory
$users = Get-ADUser -Filter * -SearchBase "OU=Studenten,DC=ijsselstreek-university,DC=nl" -Properties DisplayName, UserPrincipalName, SamAccountName

# Loop through each user and check if they already have a mailbox
foreach ($user in $users) {
    $userPrincipalName = $user.UserPrincipalName
    $displayName = $user.DisplayName

    # Check if DisplayName is not null or empty
    if (-not [string]::IsNullOrWhiteSpace($displayName)) {
        # Check if the mailbox already exists
        $existingMailbox = Get-Mailbox -Identity $userPrincipalName -ErrorAction SilentlyContinue

        if ($existingMailbox -eq $null) {
            # Create the mailbox
            Enable-Mailbox -Identity $userPrincipalName -Alias $user.SamAccountName -DisplayName $displayName

            # Set mailbox quotas
            Set-Mailbox -Identity $userPrincipalName -IssueWarningQuota 400mb -ProhibitSendQuota 500mb -ProhibitSendReceiveQuota 600mb -UseDatabaseQuotaDefaults $false
        } else {
            Write-Host "Skipping user $userPrincipalName because a mailbox already exists."
        }
    } else {
        Write-Host "Skipping user $userPrincipalName because DisplayName is null or empty."
    }
}
