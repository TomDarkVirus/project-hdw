param (
    [string]$vmName = "",
    [string]$adminUsername = "",
    [string]$adminPassword = ""
)

# Azure subscription and resource group details
$subscriptionId = "f4e2fe0a-4149-447b-b2f2-69f68c72e320"
$resourceGroupName = "Groep-N1-1-Harderwijk"
$location = "West Europe"

# Use existing network
$virtualNetworkName = "VNet-Harderwijk"
$subnetName = "default"

# Virtual machine details
#$vmName = "TESTDC"
#$adminUsername = "administrator1"
#$adminPassword = "Wachtwoord123!"
$imageOffer = "WindowsServer"
$imageSku = "2019-Datacenter"
$vmSize = "Standard_B2ms"

# Getting existing network settings
$virtualNetwork = Get-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Name $virtualNetworkName
$subnetConfig = Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $virtualNetwork -Name $subnetName

# Create a network security group
$nsg = New-AzNetworkSecurityGroup -ResourceGroupName $resourceGroupName -Name $vmName -Location $location

# Allow RDP traffic
$nsg | Add-AzNetworkSecurityRuleConfig -Name "Allow-RDP" -Direction Inbound -Access Allow -Protocol Tcp -Priority 100 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 3389
$nsg | Set-AzNetworkSecurityGroup

# Create a virtual network interface
$nic = New-AzNetworkInterface -ResourceGroupName $resourceGroupName -Name $vmName -Location $location -SubnetId $virtualNetwork.Subnets[0].Id -PublicIpAddressId $publicIpAddress.Id -NetworkSecurityGroupId $nsg.Id

# Define the VM configuration
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize $vmSize | Set-AzVMOperatingSystem -Windows -ComputerName $vmName -Credential (New-Object PSCredential -ArgumentList $adminUsername, (ConvertTo-SecureString -AsPlainText $adminPassword -Force)) | Set-AzVMSourceImage -PublisherName "MicrosoftWindowsServer" -Offer $imageOffer -Skus $imageSku -Version "latest" | Add-AzVMNetworkInterface -Id $nic.Id

# Add an additional data disk
$diskConfig = New-AzDiskConfig -SkuName "Standard_LRS" -Location $location -CreateOption Empty -DiskSizeGB 256
$dataDisk = New-AzDisk -ResourceGroupName $resourceGroupName -DiskName "${vmName}DataDisk1" -Disk $diskConfig
$vmConfig = Add-AzVMDataDisk -VM $vmConfig -Name "${vmName}DataDisk1" -CreateOption Attach -ManagedDiskId $dataDisk.Id -Lun 0

# Set DNS server using Custom Script Extension
$scriptConfig = @{
    scriptPath = "C:\Users\tomku\Documents\School\Github\project-hdw\Scripts\Azure\setDNSServer.ps1"  # Path to a script that sets DNS server (see example below)
}

# Create the VM
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig -LicenseType "Windows_Server"
