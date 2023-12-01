$vnet = Get-AzVirtualNetwork -ResourceGroupName Groep-N1-1-Harderwijk -Name vnet1
Add-AzVirtualNetworkSubnetConfig -Name Studenten -VirtualNetwork $vnet -AddressPrefix 20.1.5.0/24
Set-AzVirtualNetwork -VirtualNetwork $vnet