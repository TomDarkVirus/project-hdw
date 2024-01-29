# Define the URL of the MSI package
$msiUrl = "https://dl.ezfive.com/swng/SyslogWatcherSetup-6.5.7-win64.msi"

# Define the path where you want to save the downloaded MSI file
$downloadPath = "C:\Users\administrator1\Downloads\SyslogWatcherSetup-6.5.7-win64.msi"

# Download the MSI file
Invoke-WebRequest -Uri $msiUrl -OutFile $downloadPath

# Install the MSI package
Start-Process msiexec.exe -ArgumentList "/i $downloadPath /qn" -Wait