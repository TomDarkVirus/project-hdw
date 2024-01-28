# Specify the destination folder where you want to save and extract the Exchange Server files
$destinationFolder = "C:\Exchange2016"

# Function to install Windows features
function Install-WindowsFeatures {
    $features = "RSAT-Clustering", "RSAT-Clustering-Mgmt","RSAT-Clustering-Powershell","RSAT-Clustering-CmdInterface", "RPC-over-HTTP-proxy", "RSAT-ADDS", "Web-Server", "Web-Static-Content", "Web-Default-Doc", "Web-Http-Errors", "Web-Asp-Net", "Web-Net-Ext", "Web-ISAPI-Ext", "Web-ISAPI-Filter", "Web-Http-Logging", "Web-Log-Libraries", "Web-Request-Monitor", "Web-Http-Tracing", "Web-Basic-Auth", "Web-Windows-Auth", "Web-Client-Auth", "Web-Filtering", "Web-Stat-Compression", "Web-Dyn-Compression", "NET-WCF-HTTP-Activation45", "Web-Asp-Net45", "Web-Mgmt-Tools", "Web-Scripting-Tools", "Web-Mgmt-Compat", "Server-Media-Foundation"

    Install-WindowsFeature -Name $features -IncludeAllSubFeature -IncludeManagementTools

    Start-BitsTransfer -Source 'https://go.microsoft.com/fwlink/?linkid=2088631'  -Destination "$Env:Temp\Net4.8.exe"; & "$Env:Temp\Net4.8.exe" /q /norestart

    # Create the destination folder if it doesn't exist
    New-Item -ItemType Directory -Force -Path $destinationFolder
    Invoke-WebRequest -Uri "https://download.microsoft.com/download/2/C/4/2C47A5C1-A1F3-4843-B9FE-84C0032C61EC/UcmaRuntimeSetup.exe" -OutFile "C:\Exchange2016\UcmaRuntimeSetup.exe"
    cd "C:\Exchange2016"
    .\UcmaRuntimeSetup.exe /passive /norestart

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://vcredist.com/install.ps1'))
}

# Function to mount Exchange Server 2016
function Mount-Exchange {
    param (
        [string]$isoPath = "\\DC01-ijs\fileshare\admin\ExchangeServer2016.iso"
    )

    # Create the destination folder if it doesn't exist
    #New-Item -ItemType Directory -Force -Path $destinationFolder

    # Mount the ISO file
    $mountedDisk = Mount-DiskImage -ImagePath $isoPath -PassThru

    # Get the drive letter of the mounted ISO
    $Global:driveLetter = ($mountedDisk | Get-Volume).DriveLetter

    # Specify the destination folder for extracting the files
    $extractedFolder = Join-Path $destinationFolder "Extracted"

    # Create the destination folder if it doesn't exist
    New-Item -ItemType Directory -Force -Path $extractedFolder

    # Copy the contents of the mounted ISO to the destination folder
    Copy-Item -Path "$($driveLetter):\*" -Destination "$($extractedFolder)" -Recurse -Force

    # Dismount the ISO
    Dismount-DiskImage -ImagePath $isoPath -Confirm:$false

    Write-Host "Exchange Server 2016 files has been copied"
}

# Function to install Exchange Server 2016
function Install-Exchange {

    # Navigate to the directory where Exchange Server files are extracted
    cd "C:\Exchange2016\Extracted"

    # Prepare AD
    ./setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms
    ./setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms /OrganizationName IJsselstreek-University
    ./setup.exe /PrepareAllDomains /IAcceptExchangeServerLicenseTerms

    # Install Exchange Server 2016
    ./setup.exe /Mode:Install /Role:Mailbox /IAcceptExchangeServerLicenseTerms /OrganizationName IJsselstreek-University
}

# Main script
try {
    # Step 1: Install Windows features
    Install-WindowsFeatures

    # Step 2: Download and extract Exchange Server 2016
    Mount-Exchange

    # Step 3: Install Exchange Server 2016
    Install-Exchange

    Write-Host "Exchange Server 2016 installation completed successfully."
}
catch {
    Write-Host "Error: $_"
}
