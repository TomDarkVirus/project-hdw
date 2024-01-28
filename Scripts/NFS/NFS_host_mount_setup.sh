Apt update
Apt upgrade
Apt install nfs-kernel-server
Mkdir /srv/nfs/users
Nano sync_ldap_users.sh

Script
#!/bin/bash
 
# LDAP-serverdetails
LDAP_SERVER="ldap://192.168.13.21"
LDAP_BIND_DN="cn=admin,dc=ijsselstreek-university,dc=nl"
LDAP_PASSWORD="house-tree-animal"
LDAP_BASE_DN="dc=ijsselstreek-university,dc=nl"
 
# NFS-serverdetails
NFS_ROOT="/srv/nfs/users"
 
# Functie om een gebruiker toe te voegen als deze niet bestaat
add_user_if_not_exists() {
    local username=$1
    local uid=$2
    local gid=$3
 
    # Controleer of gebruiker al bestaat
    if ! id "$username" &>/dev/null; then
        # Voeg gebruiker toe
        sudo adduser --uid "$uid" --gid "$gid" --disabled-password --gecos "" "$username"
    fi
}
 
# Functie om NFS-directory toe te voegen als deze niet bestaat
add_nfs_directory_if_not_exists() {
    local username=$1
 
    if [ ! -d "$NFS_ROOT/$username" ]; then
        sudo mkdir -p "$NFS_ROOT/$username"
        sudo chown "$username":"$username" "$NFS_ROOT/$username"
        sudo chmod 700 "$NFS_ROOT/$username"
    fi
}
 
# LDAP-query om gebruikers op te halen
users=$(ldapsearch -x -H "$LDAP_SERVER" -D "$LDAP_BIND_DN" -w "$LDAP_PASSWORD" -b "$LDAP_BASE_DN" "(objectClass=posixAccount)" uid uidNumber gidNumber | grep -E '^uid:|^uidNumber:|^gidNumber:' | awk '{print >
echo "$users"
# Voor elke gebruiker uit LDAP
echo "$users" | while IFS=$'\t' read -r username uid gid; do
    add_user_if_not_exists "$username" "$uid" "$gid"
    add_nfs_directory_if_not_exists "$username"
done
