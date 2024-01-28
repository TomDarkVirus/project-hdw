# Import the Active Directory module
Import-Module ActiveDirectory

# Define a list of group names
$groupNames = @("Docenten_HDW", "Studenten_HDW", "Gasten")

# Create groups from the list
foreach ($groupName in $groupNames) {
    # Create a new group
    New-ADGroup -Name $groupName -GroupScope Global -GroupCategory Security -DisplayName $groupName -Description "$groupName Group"
    
    Write-Host "Group '$groupName' created successfully."
}