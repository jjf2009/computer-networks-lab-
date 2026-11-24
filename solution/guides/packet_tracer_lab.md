# Cisco Packet Tracer lab (#16)

Use one 2960 switch, one router (optional for inter-network testing), six Server-PT devices, and two PCs. Connect with copper straight-through. Suggested LAN: `192.168.10.0/24`; gateway `192.168.10.1`; servers `.10`–`.15`; clients DHCP.

On each Server-PT: Desktop → IP Configuration → static address, then Services:

* HTTP: On; edit `index.html`; test from PC Web Browser: `http://192.168.10.10`.
* FTP: On; add user `student` / `cisco`; test from PC Command Prompt: `ftp 192.168.10.11`.
* DNS: On; add A records `www.dccn.local → 192.168.10.10`, `ftp.dccn.local → 192.168.10.11`, `mail.dccn.local → 192.168.10.15`; point PCs' DNS to `.12`.
* DHCP: On; pool `DCCN-LAN`, default gateway `.1`, DNS `.12`, start `192.168.10.100`, mask `255.255.255.0`; set PCs to DHCP.
* Email: On; domain `dccn.local`; create `alice` and `bob`; test from PC Email client using SMTP/POP3 server `.15`.
* Telnet/SSH: On a router or switch, CLI: `enable`; `conf t`; `hostname R1`; `ip domain-name dccn.local`; `username admin secret cisco`; `crypto key generate rsa`; `line vty 0 4`; `login local`; `transport input telnet ssh`; `end`. Test `telnet 192.168.10.1` and `ssh -l admin 192.168.10.1`.

Save the topology as `dccn_protocols.pkt` after testing each service. Packet Tracer service names are version-dependent; if a service is unavailable on a device, use a dedicated Server-PT for it.
