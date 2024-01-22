# Define Variables
$webSiteName = "MoodleTest"
$webSitePath = "C:\inetpub\wwwroot\$webSiteName"
$phpInstallerUrl = "https://windows.php.net/downloads/releases/archives/php-8.3.1-nts-Win32-vs16-x64.zip"
$mariadbInstallerUrl = "https://mirrors.xtom.de/mariadb/mariadb-11.4.0/winx64-packages/mariadb-11.4.0-winx64.msi"
$moodleInstallerUrl = "https://download.moodle.org/download.php/direct/stable403/moodle-4.3.2.zip"
$moodlePath = "C:\inetpub\wwwroot\$webSiteName"

# Install IIS
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
Write-Host "Installed Windows features"

# Download and install PHP
Invoke-WebRequest -Uri $phpInstallerUrl -OutFile "C:\php.zip"
Expand-Archive -Path "C:\php.zip" -DestinationPath "C:\php"
robocopy "C:\php" "$webSitePath" /E
Write-Host "Installed PHP"

# Download and install MariaDB
Invoke-WebRequest -Uri $mariadbInstallerUrl -OutFile "C:\mariadb.msi"
Start-Process -Wait -FilePath "msiexec.exe" -ArgumentList "/i C:\mariadb.msi SERVICENAME=MariaDB /qn /l*v C:\mariadb_install.log"
Write-Host "Installed MariaDB"

# Start MariaDB service
Start-Service -Name "MariaDB"
Write-Host "Started MariaDB"

# Download and install Moodle
Invoke-WebRequest -Uri $moodleInstallerUrl -OutFile "C:\moodle.zip"
Expand-Archive -Path "C:\moodle.zip" -DestinationPath $webSitePath
Write-Host "Installed Moodle"

# Configure IIS for PHP
Add-WebConfiguration -Filter /system.webServer/handlers -Value @{
    path = "*.php"
    scriptProcessor = "C:\php\php-cgi.exe"
    verb = "GET,HEAD,POST"
    modules = @{
        FastCgiModule = @{
            "ResourceType" = "Unspecified"
            "RequireAccess" = "Script"
        }
    }
} -PSPath "IIS:\" -WhatIf
Write-Host "Configured IIS"

# Create a new IIS site
New-WebSite -Name $webSiteName -PhysicalPath $webSitePath -Port 80
Write-Host "Created IIS website"

# Restart IIS
Restart-WebAppPool -Name "DefaultAppPool"
Restart-Service -Name "W3SVC"
Write-Host "Restarted IIS"