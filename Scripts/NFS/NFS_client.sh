Apt update
Apt upgrade
Apt install autofs
nano /etc/auto.master
/mountpoint/path /etc/auto.nfs --timeout=60 --ghost
Save and exit
nano /etc/auto.nfs
* -fstype=nfs,rw,soft,intr 192.168.13.14:/srv/nfs/users/&
Save and exit
Systemctl restart autofs