# Import the Active Directory module
Import-Module ActiveDirectory

# Define the path to the text file containing user information
$filePath = "users.txt"

# Define the group name
$groupName = "Studenten_HDW"

# Read each line from the file and create users
Get-Content $filePath | ForEach-Object {
    # Split the line into individual pieces of information
    $userInfo = $_ -split ','

    # Assign values to variables
    $firstName = $userInfo[0]
    $lastName = $userInfo[1]
    $username = $userInfo[2]
    $password = $userInfo[3]

    # Create a new user
    New-ADUser -SamAccountName $username -UserPrincipalName "$username@test.com" -GivenName $firstName -Surname $lastName -Name "$firstName $lastName" -DisplayName "$firstName $lastName" -Enabled $true -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) -ChangePasswordAtLogon $true -PasswordNeverExpires $false

    # Add the user to the specified group
    Add-ADGroupMember -Identity $groupName -Members $username

    Write-Host "User '$username' created and added to group '$groupName' successfully."
}
