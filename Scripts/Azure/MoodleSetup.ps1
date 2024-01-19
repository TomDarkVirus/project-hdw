# Define Variables
$webSiteName = "MoodleSite"
$webSitePath = "C:\inetpub\wwwroot\$webSiteName"
$phpInstallerUrl = "https://windows.php.net/downloads/releases/php-8.3.1-nts-Win32-vs16-x64.zip"
$mariadbInstallerUrl = "https://mirrors.xtom.de/mariadb/mariadb-11.4.0/winx64-packages/mariadb-11.4.0-winx64.msi"
$moodleInstallerUrl = "https://download.moodle.org/download.php/direct/stable40/moodle-latest-40.zip"
$moodlePath = "C:\inetpub\wwwroot\$webSiteName"

# Install IIS
Install-WindowsFeature -Name Web-Server -IncludeManagementTools

# Download and install PHP
Invoke-WebRequest -Uri $phpInstallerUrl -OutFile "C:\php.zip"
Expand-Archive -Path "C:\php.zip" -DestinationPath "C:\php"
Copy-Item -Path "C:\php\*" -Destination "$webSitePath"

# Download and install MariaDB
Invoke-WebRequest -Uri $mariadbInstallerUrl -OutFile "C:\mariadb.msi"
Start-Process -Wait -FilePath "msiexec.exe" -ArgumentList "/i C:\mariadb.msi /qn"

# Start MariaDB service
Start-Service -Name "MSSQLServer"

# Download and install Moodle
Invoke-WebRequest -Uri $moodleInstallerUrl -OutFile "C:\moodle.zip"
Expand-Archive -Path "C:\moodle.zip" -DestinationPath $webSitePath

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
} -PSPath "IIS:\"

# Create a new IIS site
New-WebSite -Name $webSiteName -PhysicalPath $webSitePath -Port 80

# Restart IIS
Restart-WebAppPool -Name "DefaultAppPool"
Restart-Service -Name "W3SVC"
