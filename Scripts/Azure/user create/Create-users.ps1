Import-Module ActiveDirectory

# Pad naar de CSV met gebruikersgegevens
$Users = Import-Csv -Path "C:\Users\administrator1\Desktop\user create\Users.csv" -Delimiter ';'

# Pad naar het CSV-bestand voor Moodle-gebruikers
$MoodleOutputFile = "C:\Users\administrator1\Desktop\user create\moodle.csv"

# Loop door elke gebruiker in de CSV
foreach ($User in $Users) {
    $Displayname = $User.displayname
    $SAM = $User.samaccountname

    # Pad naar de home directory op de fileshare
    $HomeDirectory = "\\DC01-ijs\Fileshare\Fileshare\User mappen\$SAM"

    # Maak een map voor de gebruiker op de fileshare als deze nog niet bestaat
    if (!(Test-Path -Path $HomeDirectory)) {
        New-Item -Path $HomeDirectory -ItemType Directory -Force

        Write-Host "Home directory created for $Displayname at $HomeDirectory"
    } else {
        Write-Host "Home directory for $Displayname already exists at $HomeDirectory"
    }

    # Maak de gebruiker aan in Active Directory als deze nog niet bestaat
    if (-not (Get-ADUser -Filter {SamAccountName -eq $SAM})) {
        # Print OU Path for debugging
        Write-Host "OU Path: $($User.OU)"

        # Update the OU path if necessary
        New-ADUser -Name $Displayname -DisplayName $Displayname -SamAccountName $SAM -UserPrincipalName "$SAM@ijsselstreek-university.nl" -GivenName $User.Firstname -Surname $User.Lastname -Description $User.Description -AccountPassword (ConvertTo-SecureString $User.Password -AsPlainText -Force) -Enabled $true -Path $User.OU -ChangePasswordAtLogon $false –PasswordNeverExpires $true

        Write-Host "$Displayname Created in Active Directory"
    } else {
        Write-Host "$Displayname already exists in Active Directory"
    }

    # Voeg gebruikersinformatie toe aan het Moodle CSV-bestand
    $MoodleUserInfo = "$SAM,$($User.Firstname),$($User.Lastname),$($User.Password),$SAM@ijsselstreek-university.nl,Test"
    $MoodleUserInfo | Out-File -FilePath $MoodleOutputFile -Append

    # Stel de toegangsrechten in voor de gebruikersmap op de fileshare
    try {
        # Revoke permissions for all users
        icacls "$HomeDirectory" /inheritance:r /remove "*S-1-5-11" "*S-1-5-32-544" /t

        # Grant Full Control to the specific user and administrators
       # icacls "$HomeDirectory" /grant "$SAM`:(OI)(CI)F" "BUILTIN\Administrators`:(OI)(CI)F" /t

        Write-Host "Access granted to $SAM for $HomeDirectory"
    }
    catch {
        Write-Host "Error granting access to $SAM for $HomeDirectory"
        Write-Host "Error Details: $_"
    }

    # Add user to the specified groups
    $UserGroups = $User.UserGroup -split '_'
    foreach ($Group in $UserGroups) {
        try {
            Add-ADGroupMember -Identity $Group -Members $SAM -ErrorAction Stop
            Write-Host "$SAM added to $Group"
        }
        catch {
            Write-Host "Error adding $SAM to $Group"
            Write-Host "Error Details: $_"
        }
    }
}