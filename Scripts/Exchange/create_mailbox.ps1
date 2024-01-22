# Import the Exchange Management Shell module
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn

# Get a list of users from Active Directory
$users = Get-ADUser -Filter * -SearchBase "OU=Studenten,DC=banaan,DC=nl" -Properties DisplayName

# Loop through each user and create a mailbox
foreach ($user in $users) {
    $userPrincipalName = $user.UserPrincipalName
    $displayName = $user.DisplayName

    # Check if DisplayName is not null or empty
    if (-not [string]::IsNullOrWhiteSpace($displayName)) {
        # Create the mailbox
        Enable-Mailbox -Identity $userPrincipalName -Alias $user.SamAccountName -DisplayName $displayName
    } else {
        Write-Host "Skipping user $userPrincipalName because DisplayName is null or empty."
    }
}
