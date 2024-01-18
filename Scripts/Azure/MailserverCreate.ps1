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
$adminUsername = "administrator1"
$adminPassword = "Wachtwoord123!"
$imageOffer = "WindowsServer"
$imageSku = "2016-Datacenter"
$vmSize = "Standard_D4as_v5"

# Getting existing network settings
$virtualNetwork = Get-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Name $virtualNetworkName
$subnetConfig = Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $virtualNetwork -Name $subnetName

# Create a network security group
$nsg = New-AzNetworkSecurityGroup -ResourceGroupName $resourceGroupName -Name "TestNSG" -Location $location

# Allow RDP traffic
$nsg | Add-AzNetworkSecurityRuleConfig -Name "Allow-RDP" -Direction Inbound -Access Allow -Protocol Tcp -Priority 100 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 3389
$nsg | Set-AzNetworkSecurityGroup

# Create a virtual network interface
$nic = New-AzNetworkInterface -ResourceGroupName $resourceGroupName -Name "TestNIC" -Location $location -SubnetId $virtualNetwork.Subnets[0].Id -PublicIpAddressId $publicIpAddress.Id -NetworkSecurityGroupId $nsg.Id

# Define the VM configuration
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize $vmSize | Set-AzVMOperatingSystem -Windows -ComputerName $vmName -Credential (New-Object PSCredential -ArgumentList $adminUsername, (ConvertTo-SecureString -AsPlainText $adminPassword -Force)) | Set-AzVMSourceImage -PublisherName "MicrosoftWindowsServer" -Offer $imageOffer -Skus $imageSku -Version "latest" | Add-AzVMNetworkInterface -Id $nic.Id

# Create the VM
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig -LicenseType "Windows_Server"
