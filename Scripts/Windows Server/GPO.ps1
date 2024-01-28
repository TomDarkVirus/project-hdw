# Define variables
$domainName = "ijsselstreek-university.nl"
$backgroundImagePath = "\\DC01-ijs\fileshare\background\background.jpg"
$softwareInstallerPath = "\\DC01-ijs\fileshare\ADMIN\background\LibreOffice_7.6.4_Win_x86-64.ms"

# Import the Group Policy module
Import-Module GroupPolicy

# Create a new GPO for changing the background
$backgroundGPOName = "ChangeBackgroundGPO"
New-GPO -Name $backgroundGPOName

# Link the GPO to the domain
$domain = Get-GPDomain -Name $domainName
$gpo = Get-GPO -Name $backgroundGPOName
New-GPLink -Name $backgroundGPOName -Target $domain -LinkEnabled Yes -GPO $gpo

# Configure background settings in the GPO
$backgroundSettings = @{
    "WallpaperStyle" = "2"  # 2 for Centered, you can choose other values as per your preference
    " Wallpaper" = $backgroundImagePath
}
Set-GPRegistryValue -Name $backgroundGPOName -Key "HKEY_CURRENT_USER\Control Panel\Desktop" -ValueName $backgroundSettings

# Create a new GPO for software installation
$softwareGPOName = "InstallSoftwareGPO"
New-GPO -Name $softwareGPOName

# Link the GPO to the domain
$gpo = Get-GPO -Name $softwareGPOName
New-GPLink -Name $softwareGPOName -Target $domain -LinkEnabled Yes -GPO $gpo

# Configure software installation settings in the GPO
$softwareDeploymentSettings = @{
    "PackageName" = $softwareInstallerPath
    "AllowDowngrades" = "false"
    "Action" = "Install"
}
Add-GPPackage -Name $softwareGPOName -Package $softwareDeploymentSettings

# Force Group Policy update on client machines
gpupdate /force

Write-Host "Group Policy Objects created successfully."
