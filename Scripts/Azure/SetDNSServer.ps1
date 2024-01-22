# Set DNS server
$dnsServer = "8.8.8.8"
netsh interface ipv4 set dns "Ethernet" static $dnsServer
