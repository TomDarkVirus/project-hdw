# Set DNS server
$dnsServer = "10.10.0.14"
netsh interface ipv4 set dns "Ethernet" static $dnsServer
