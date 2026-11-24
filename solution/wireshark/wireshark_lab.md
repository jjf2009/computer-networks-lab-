# Wireshark protocol inspection (#18)

Capture on the active interface while running Packet Tracer simulations or the Python servers. Useful display filters:

| Protocol | Filter | What to inspect |
|---|---|---|
| DNS | `dns` | query name, transaction ID, answer record |
| DHCP | `dhcp` or `bootp` | Discover/Offer/Request/ACK, UDP 67/68 |
| HTTP | `http` or `tcp.port == 8080` | GET, status code, headers, payload |
| FTP | `ftp` or `tcp.port == 2121` | USER/PASS/RETR commands; plaintext warning |
| Telnet | `telnet` | plaintext login and commands |
| SSH | `ssh` | encrypted session and handshake metadata |
| SMTP/POP3 | `smtp or pop` | mail commands and headers |

Right-click a packet → Follow → TCP Stream to reconstruct a session. Use Statistics → Protocol Hierarchy and Conversations for an overview. For a report, record source/destination IP, ports, TCP handshake, request/response, and the security observation for each protocol. Never capture credentials on a real network.
