# Variables
$resourceGroupName = "Groep-N1-1-Harderwijk"
$location = "West Europe"
$vnetName = "TestVNet"
$vnetAddressPrefix = "192.168.0.0/16"
$subnetName = "TestSubnet"
$subnetAddressPrefix = "192.168.0.0/24"

# Create a subnet configuration
$subnetConfig = @{
    Name = $subnetName
    AddressPrefix = $subnetAddressPrefix
}

# Create a new virtual network with the subnet configuration
$vnet = New-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Name $vnetName -Location $location -AddressPrefix $vnetAddressPrefix -Subnet $subnetConfig

# Output information
Write-Output "Virtual Network '$vnetName' created with subnet '$subnetName'."