# Install DFS Roles
Install-WindowsFeature -Name FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools

# Get the available disk
$disk = Get-Disk | Where-Object { $_.PartitionStyle -eq 'RAW' }

if ($disk) {
    # Initialize the disk
    Initialize-Disk -Number $disk.Number -PartitionStyle MBR

    # Create a partition
    New-Partition -DiskNumber $disk.Number -UseMaximumSize -AssignDriveLetter | Format-Volume -FileSystem NTFS -NewFileSystemLabel "Fileshare" -Confirm:$false

    # Assign drive letter
    $driveLetter = $disk.DriveLetter
    if (-not $driveLetter) {
        $driveLetter = Get-Partition -DiskNumber $disk.Number | Get-Partition | Get-Volume | Select-Object -ExpandProperty DriveLetter
    }

    # Check if drive letter is available
    if ($driveLetter) {
        # Create share1 and share2 folders
        New-Item -ItemType Directory -Path "$($driveLetter):\Fileshare"
        New-Item -ItemType Directory -Path "$($driveLetter):\Fileshare\share1"
        New-Item -ItemType Directory -Path "$($driveLetter):\Fileshare\share2"
        New-Item -ItemType Directory -Path "$($driveLetter):\Fileshare\User_Maps"
        New-Item -ItemType Directory -Path "$($driveletter):\Admin"
        New-Item -ItemType Directory -Path "$($driveletter):\Admin\Quota_Management"
        
    }

    #Remove-SmbShare -Name Fileshare
    New-SmbShare –Name Fileshare –Path "$($driveLetter):\Fileshare" -ReadAccess "Authenticated Users"

    # Create DFS Namespace
    New-DfsnRoot -Path "\\banaan.nl\Fileshare" -Type DomainV2 -TargetPath "\\FRANKENSTEIN\Fileshare"

    # Add Folder Targets
    New-DfsnFolder -Path "\\banaan.nl\Fileshare\folder1" -TargetPath "\\FRANKENSTEIN\Fileshare\share1"
    New-DfsnFolder -Path "\\banaan.nl\Fileshare\folder2" -TargetPath "\\FRANKENSTEIN\Fileshare\share2"
    New-DfsnFolder -Path "\\banaan.nl\Fileshare\User Mappen" -TargetPath "\\FRANKENSTEIN\Fileshare\User_Maps"

    # quota management
    # Specify the quota limit in bytes (500 MB in bytes)
    $quotaLimitBytes = 500MB

    # Specify the template name and description
    $templateName = "500MB Limit"
    $templateDescription = "Quota template to limit folder to 500 MB"

    # Try to create a new quota template (it may already exist)
    try {
        New-FsrmQuotaTemplate -Name $templateName -Description $templateDescription -Size $quotaLimitBytes -ErrorAction Stop
    } catch {
        Write-Host "Quota template '$templateName' already exists."
    }

    # Get the created quota template
    $template = Get-FsrmQuotaTemplate -Name $templateName

    # Apply the template to a folder
    Set-FsrmQuota -Path "\\DC01-ijs\Fileshare\ADMIN\Quota management" -TemplateName $template.Name
}
else {
    Write-Host "No uninitialized disks found."
}
