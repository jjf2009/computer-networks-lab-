# Computer Networks & DCCN Lab: Complete Solutions, Packet Tracer Topologies, Python Sockets & Wireshark Guides

[![Cisco Packet Tracer](https://img.shields.io/badge/Cisco_Packet_Tracer-v8.2+-005073?style=for-the-badge&logo=cisco&logoColor=white)](https://www.netacad.com/courses/packet-tracer)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Wireshark](https://img.shields.io/badge/Wireshark-4.x-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)](https://www.wireshark.org/)
[![Course Curriculum](https://img.shields.io/badge/Curriculum-B.Tech_%2F_BE_CS_%26_IT-blueviolet?style=for-the-badge)](#curriculum-matrix)
[![LLMs Index](https://img.shields.io/badge/LLMs.txt-GEO_Optimized-00A67E?style=for-the-badge)](llms.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> **Complete, production-grade laboratory solutions for university Computer Networks and Data Communications (DCCN / CN) curricula.** Includes ready-to-run Cisco Packet Tracer (`.pkt`) network designs, multi-threaded Python socket implementations (`servers.py`), Wireshark protocol capture runbooks, and submission-ready academic reports.

<!-- SEO / GEO Structured Metadata -->
<!--
Repository: computer-networks-lab
Keywords: computer networks lab, dccn lab solutions, cisco packet tracer lab, packet tracer topologies, python socket programming, wireshark packet analysis, btech cs networking, routing protocols ospf rip eigrp, subnetting vlsm flsm
GEO Compatibility: llms.txt, llms-full.txt
-->

---

## ⚡ Executive Summary / TL;DR

- **What is this repository?** An end-to-end, reproducible practical coursework suite for undergraduate computer science and engineering students, network engineers, and instructors studying computer networking.
- **What is included?**
  1. **Cisco Packet Tracer Topologies (`.pkt`)**: Tested simulations for Bus, Star, Ring, Mesh, FLSM static routing, VLSM with DHCP & RIPv2, dynamic routing protocol shootouts (RIPv2 vs OSPF vs EIGRP), and multi-service enterprise servers (HTTP, FTP, DNS, DHCP, Email, Telnet, SSH).
  2. **Python Socket Programming**: Pure Python 3 socket implementations for a concurrent multi-client TCP chat room, RFC-compliant single-threaded HTTP/1.1 static web server, and an interactive RFC 959 FTP daemon.
  3. **Packet Sniffing with Wireshark**: Comprehensive display filter cheat sheets, TCP three-way handshake dissection, and plaintext-vs-ciphertext security evaluations.
  4. **Laboratory Documentation**: Finalized, academic-format observation reports (`.docx` & `.md`) formatted with clean setup logs and zero fabricated data.
- **Target Audience:** College students (B.Tech / B.E. / B.Sc / BCA / MCA in CS/IT), lab instructors, CCNA/Network+ candidates, and networking enthusiasts.
- **Quick Links:**
  - [One-Stop Submission Pack](solution/README.md)
  - [Cisco Packet Tracer Final Projects](solution/packet-tracer/final/)
  - [Python Socket Server Implementations](solution/python/servers.py)
  - [Wireshark Deep-Dive Guide](solution/wireshark/wireshark_lab.md)
  - [AI/LLM Machine-Readable Index](llms.txt)

---

## 📋 Table of Contents

- [Curriculum & Experiment Matrix](#-curriculum--experiment-matrix)
- [Quick Start Guide](#-quick-start-guide)
  - [1. Running Cisco Packet Tracer Topologies](#1-running-cisco-packet-tracer-topologies)
  - [2. Executing Python Socket Servers](#2-executing-python-socket-servers)
  - [3. Wireshark Network Packet Inspection](#3-wireshark-network-packet-inspection)
- [Technical Architecture & Protocol References](#-technical-architecture--protocol-references)
  - [Subnetting Reference: FLSM vs VLSM](#subnetting-reference-flsm-vs-vlsm)
  - [Dynamic Routing Protocol Comparison: RIP vs OSPF vs EIGRP](#dynamic-routing-protocol-comparison-rip-vs-ospf-vs-eigrp)
  - [Application-Layer Protocol Port Matrix](#application-layer-protocol-port-matrix)
- [Comprehensive Experiment Breakdown](#-comprehensive-experiment-breakdown)
  - [Experiments 4 & 6: Physical Media, Connectors & Topologies](#experiments-4--6-physical-media-connectors--topologies)
  - [Experiments 5, 7 & 8: Data Link Protocols, Framing & Error Control](#experiments-5-7--8-data-link-protocols-framing--error-control)
  - [Experiment 9: Core TCP/IP Diagnostic CLI Commands](#experiment-9-core-tcpip-diagnostic-cli-commands)
  - [Experiments 10 & 11: Subnetting (FLSM / VLSM), Static Routing & DHCP](#experiments-10--11-subnetting-flsm--vlsm-static-routing--dhcp)
  - [Experiments 12 & 13: Dynamic Routing (RIPv2, OSPF, EIGRP & Python Simulations)](#experiments-12--13-dynamic-routing-ripv2-ospf-eigrp--python-simulations)
  - [Experiments 14 & 15: Digital Carrier Modulation & Multiplexing](#experiments-14--15-digital-carrier-modulation--multiplexing)
  - [Experiment 16: Multi-Service Enterprise Server Farm](#experiment-16-multi-service-enterprise-server-farm)
  - [Experiment 17: Python Socket Programming Implementation](#experiment-17-python-socket-programming-implementation)
  - [Experiment 18: Wireshark Packet Analysis & Protocol Dissection](#experiment-18-wireshark-packet-analysis--protocol-dissection)
- [Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)
- [Repository Structure](#-repository-structure)
- [Citation & Academic Reference](#-citation--academic-reference)
- [Contributing & License](#-contributing--license)

---

## 📊 Curriculum & Experiment Matrix

| Exp # | Official Title / Focus | Layer (OSI) | Key Technologies & Protocols | Primary Artifacts |
|:---:|:---|:---:|:---|:---|
| **04** | Study of Transmission Media & Connectors | Physical (L1) | UTP Cat5e/6, Coaxial, Fiber Optic, RJ-45, BNC, ST/SC/LC | [`experiment4_cables_connectors.pkt`](solution/packet-tracer/final/experiment4_cables_connectors.pkt), [Docx](solution/docs/source/dccn_exp4.docx) |
| **05** | Flow Control Protocols | Data Link (L2) | Stop-and-Wait ARQ, Sliding Window, Go-Back-N, Selective Repeat | [Docx](solution/docs/source/DCCN%20Expt5.docx) |
| **06** | Network Topologies Simulation | Physical/Data Link | Bus, Star, Ring, Mesh, Hybrid Topologies | [`experiment6_topologies.pkt`](solution/packet-tracer/final/experiment6_topologies.pkt), [Docx](solution/docs/source/DCCN%20Expt6.docx) |
| **07** | Framing Methods & Throughput Analysis | Data Link (L2) | Character Count, Byte Stuffing, Bit Stuffing (Flag `01111110`) | [Docx](solution/docs/source/DCCN%20Expt7.docx) |
| **08** | Error Detection & Correction Codes | Data Link (L2) | Parity Check, Internet Checksum, CRC-16 / CRC-CCITT, Hamming Code | [Docx](solution/docs/source/DCCN%20Expt8.docx) |
| **09** | TCP/IP Networking Commands | Network/Transport | `ping`, `traceroute`, `arp`, `netstat`, `nslookup`, `ipconfig` | [Docx](solution/docs/source/DCCN%20Expt9.docx) |
| **10** | Subnetting (FLSM) & Static Routing | Network (L3) | Fixed Length Subnet Masking, Static Routes, Gateway Config | [`experiment10_flsm_static.pkt`](solution/packet-tracer/final/experiment10_flsm_static.pkt), [Final Report](solution/docs/final/Kanak_DCCN_EXPT_10_updated.docx) |
| **11** | Subnetting (VLSM), DHCP & RIPv2 | Network (L3) | Variable Length Subnet Masking, Router DHCP Pools, RIPv2 Dynamic Routing | [`experiment11_vlsm_dhcp_ripv2.pkt`](solution/packet-tracer/final/experiment11_vlsm_dhcp_ripv2.pkt), [Final Report](solution/docs/final/Kanak_DCCN_EXPT_11_updated.docx) |
| **12** | Dynamic Routing Algorithms in Python | Network (L3) | Dijkstra's Shortest Path (Link-State), Bellman-Ford (Distance Vector) | [Docx Archive](solution/docs/archive/vote_prabhav/Kanak_DCCN_EXPT_12.docx) |
| **13** | Dynamic Routing Shootout (RIP vs OSPF vs EIGRP) | Network (L3) | Distance Vector (RIP), Link-State (OSPF Area 0), Hybrid (EIGRP AS 100) | [`experiment13_rip.pkt`](solution/packet-tracer/final/experiment13_rip.pkt), [`experiment13_ospf.pkt`](solution/packet-tracer/final/experiment13_ospf.pkt), [`experiment13_eigrp.pkt`](solution/packet-tracer/final/experiment13_eigrp.pkt), [Final Report](solution/docs/final/Kanak_DCCN_EXPT_13_updated.docx) |
| **14** | Digital Carrier Modulation Schemes | Physical (L1) | Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), PSK, QPSK | [Docx Archive](solution/docs/archive/vote_prabhav/Kanak_DCCN_EXPT_14.docx) |
| **15** | Multiplexing Techniques Simulator | Physical (L1) | Frequency Division Multiplexing (FDM), Time Division Multiplexing (TDM) | [Docx Archive](solution/docs/archive/vote_prabhav/Kanak_DCCN_EXPT_15.docx) |
| **16** | Application Layer Network Services Farm | Application (L7) | HTTP, FTP, DNS, DHCP, Telnet, SSH, SMTP, POP3 | [`experiment16_servers_completed.pkt`](solution/packet-tracer/final/experiment16_servers_completed.pkt), [Final Report](solution/docs/final/Experiment_16_Server_Protocols_updated.docx) |
| **17** | Socket Programming in Python | Transport/App | Multi-Threaded TCP Chat, RFC-compliant HTTP Server, Interactive FTP Daemon | [`solution/python/servers.py`](solution/python/servers.py), [Python Guide](solution/python/README.md) |
| **18** | Wireshark Protocol Sniffing & Forensic Inspection | All Layers | Packet Filtering, 3-Way Handshake, Cleartext vs Encryption Analysis | [`solution/wireshark/wireshark_lab.md`](solution/wireshark/wireshark_lab.md) |

---

## 🚀 Quick Start Guide

### 1. Running Cisco Packet Tracer Topologies

1. Ensure **Cisco Packet Tracer (v8.0 or newer)** is installed on your workstation.
2. Clone this repository:
   ```bash
   git clone https://github.com/jjf2009/computer-networks-lab.git
   cd computer-networks-lab
   ```
3. Navigate to [`solution/packet-tracer/final/`](solution/packet-tracer/final/) and open any simulation file directly:
   - For Multi-Service Server Farm: `experiment16_servers_completed.pkt`
   - For VLSM Subnetting with DHCP: `experiment11_vlsm_dhcp_ripv2.pkt`
   - For Routing Protocol comparison: `experiment13_ospf.pkt`
4. Toggle between **Realtime Mode** (for converged operational testing) and **Simulation Mode** (to watch PDUs traverse switches and routers step-by-step).

### 2. Executing Python Socket Servers

All socket servers are unified inside [`solution/python/servers.py`](solution/python/servers.py) requiring no third-party libraries (pure Python standard library):

```bash
cd solution/python

# 1. Multi-client TCP Chat Room (Port 5000)
python3 servers.py chat --port 5000

# 2. HTTP Web Server serving local static files (Port 8080)
python3 servers.py web --port 8080 --root lab_root

# 3. Interactive RFC 959 FTP Daemon (Port 2121)
python3 servers.py ftp --port 2121 --root lab_root
```

#### Verifying with Client Commands
- **Chat**: Connect from multiple terminals using Netcat:
  ```bash
  nc 127.0.0.1 5000
  ```
- **HTTP**: Fetch web content:
  ```bash
  curl -i http://127.0.0.1:8080/index.html
  ```
- **FTP**: Test FTP commands interactively:
  ```bash
  nc 127.0.0.1 2121
  USER student
  PASS lab
  LIST
  RETR index.html
  QUIT
  ```

### 3. Wireshark Network Packet Inspection

1. Launch Wireshark and attach to your loopback interface (`lo` on Linux / macOS, `Adapter for loopback traffic capture` on Windows).
2. Apply targeted display filters:
   - Filter HTTP transactions: `http or tcp.port == 8080`
   - Filter FTP control commands: `ftp or tcp.port == 2121`
   - Filter DNS queries & resolutions: `dns`
   - Filter DHCP 4-way DORA handshakes: `dhcp or bootp`
3. Inspect TCP handshakes (`[SYN]`, `[SYN, ACK]`, `[ACK]`) and examine payload security by selecting **Follow → TCP Stream**.

---

## 🛠️ Technical Architecture & Protocol References

### Subnetting Reference: FLSM vs VLSM

| Dimension | Fixed Length Subnet Mask (FLSM) | Variable Length Subnet Mask (VLSM) |
|:---|:---|:---|
| **Mask Uniformity** | All subnets share an identical subnet mask | Subnets use custom prefixes tailored to host requirements |
| **IP Efficiency** | Prone to substantial IP waste on small point-to-point links | Maximizes address utilization, minimizing unassigned IP space |
| **Routing Protocols** | Supported by classful (RIPv1, IGRP) and classless protocols | Requires classless routing protocols (RIPv2, OSPF, EIGRP, BGP) |
| **Lab Example** | [Experiment 10](solution/packet-tracer/final/experiment10_flsm_static.pkt): Divide `192.168.1.0/24` into equal `/26` subnets | [Experiment 11](solution/packet-tracer/final/experiment11_vlsm_dhcp_ripv2.pkt): Assign `/26` (60 hosts), `/27` (30 hosts), `/30` (WAN links) |

#### Common Subnet Masks Cheatsheet (IPv4 Class C)
- `/24`: `255.255.255.0` (254 Usable Hosts)
- `/26`: `255.255.255.192` (62 Usable Hosts)
- `/27`: `255.255.255.224` (30 Usable Hosts)
- `/28`: `255.255.255.240` (14 Usable Hosts)
- `/30`: `255.255.255.252` (2 Usable Hosts, ideal for router-to-router serial links)

---

### Dynamic Routing Protocol Comparison: RIP vs OSPF vs EIGRP

| Feature | RIPv2 (Routing Information Protocol) | OSPF (Open Shortest Path First) | EIGRP (Enhanced Interior Gateway Routing Protocol) |
|:---|:---|:---|:---|
| **Type / Family** | Distance Vector | Link-State | Advanced Distance Vector (Hybrid) |
| **Algorithm** | Bellman-Ford | Dijkstra (Shortest Path First - SPF) | DUAL (Diffusing Update Algorithm) |
| **Metric** | Hop count (Max: 15 hops; 16 = unreachable) | Cost (Inverse bandwidth: $10^8 / \text{Bandwidth}$) | Composite (Bandwidth, Delay, Reliability, Load) |
| **Convergence Speed** | Slow (periodic 30s timers) | Fast (event-triggered LSAs) | Very Fast (feasible successors calculated instantly) |
| **Administrative Distance** | 120 | 110 | 90 (Internal), 170 (External) |
| **Standard / RFC** | RFC 2453 (Open Standard) | RFC 2328 (Open Standard) | Cisco Proprietary, later published as RFC 7868 |
| **Packet Tracer Model** | [`experiment13_rip.pkt`](solution/packet-tracer/final/experiment13_rip.pkt) | [`experiment13_ospf.pkt`](solution/packet-tracer/final/experiment13_ospf.pkt) | [`experiment13_eigrp.pkt`](solution/packet-tracer/final/experiment13_eigrp.pkt) |

---

### Application-Layer Protocol Port Matrix

Configured and validated in [Experiment 16 (`experiment16_servers_completed.pkt`)](solution/packet-tracer/final/experiment16_servers_completed.pkt):

| Protocol | Default Port | Transport | Purpose in Lab | Security Observation |
|:---|:---:|:---:|:---|:---|
| **HTTP** | 80 | TCP | Hypertext delivery (`index.html`) | Plaintext HTML & headers |
| **FTP** | 20 (Data), 21 (Control) | TCP | File transfers (`USER`, `PASS`, `RETR`) | Transmits credentials in plaintext |
| **DNS** | 53 | UDP / TCP | Resolves `www.dccn.local`, `ftp.dccn.local` | Unencrypted domain query |
| **DHCP** | 67 (Server), 68 (Client) | UDP | Automatic dynamic IP pool leasing | Broadcast Discover / Offer / Request / ACK |
| **Telnet** | 23 | TCP | Remote command-line administration | Passwords visible in Wireshark streams |
| **SSH** | 22 | TCP | Encrypted remote terminal administration | Encrypted cryptographic session (Diffie-Hellman) |
| **SMTP** | 25 | TCP | Outgoing electronic mail transport | Cleartext envelope and headers |
| **POP3** | 110 | TCP | Incoming electronic mail mailbox retrieval | Plaintext authentication |

---

## 🔬 Comprehensive Experiment Breakdown

### Experiments 4 & 6: Physical Media, Connectors & Topologies
- **Media Types**: Straight-Through copper cable (PC-to-Switch), Crossover cable (Switch-to-Switch / PC-to-PC), Coaxial cable, Fiber Optic (Single-mode vs Multi-mode), Serial DTE/DCE.
- **Topologies Modeled**:
  - **Bus Topology**: Shared backbone cable with terminating resistors; vulnerable to line breaks.
  - **Star Topology**: Central hub/switch connecting independent nodes; single-point switch failure.
  - **Ring Topology**: Token passing or circular links; predictable latency, ring break risk.
  - **Mesh Topology**: Full point-to-point mesh ($N(N-1)/2$ links) for maximum fault tolerance.
  - **Hybrid Topology**: Combines Star-Bus or Star-Ring for enterprise scalability.

### Experiments 5, 7 & 8: Data Link Protocols, Framing & Error Control
- **Flow Control (Exp 5)**: Stop-and-Wait ARQ timeout analysis vs Sliding Window pipelining.
- **Framing (Exp 7)**:
  - **Bit Stuffing**: Injects a `0` after five consecutive `1`s to distinguish payload from the flag sequence `01111110`.
  - **Byte Stuffing**: Uses escape characters (`ESC`) to escape framing flag bytes within payload data.
- **Error Control (Exp 8)**:
  - **CRC (Cyclic Redundancy Check)**: Modulo-2 binary polynomial division (`CRC-CCITT`).
  - **Hamming Code**: Single Error Correction and Double Error Detection (SEC-DED) with parity bit positioning at powers of 2 ($1, 2, 4, 8\dots$).

### Experiment 9: Core TCP/IP Diagnostic CLI Commands
Essential networking commands demonstrated with practical output:
```bash
# Test reachability and round-trip time
ping -c 4 192.168.10.1

# Trace hop-by-hop packet path
traceroute 8.8.8.8

# Display local ARP cache mapping IP to MAC
arp -a

# View active TCP/UDP connections and listening sockets
netstat -tuln

# Query DNS records from specific name servers
nslookup www.dccn.local 192.168.10.12
```

### Experiments 10 & 11: Subnetting (FLSM / VLSM), Static Routing & DHCP
- **FLSM (Exp 10)**: Network `192.168.1.0/24` divided into equal subnets using a fixed `/26` mask. Static routing configured on Cisco routers:
  ```cisco
  Router(config)# ip route 192.168.1.64 255.255.255.192 10.0.0.2
  ```
- **VLSM & DHCP (Exp 11)**: Multi-department subnetting (Sales, Engineering, Management, WAN) minimizing wasted IP addresses. Router-hosted DHCP configuration:
  ```cisco
  Router(config)# ip dhcp pool DCCN-LAN
  Router(dhcp-config)# network 192.168.10.0 255.255.255.0
  Router(dhcp-config)# default-router 192.168.10.1
  Router(dhcp-config)# dns-server 192.168.10.12
  ```

### Experiments 12 & 13: Dynamic Routing (RIPv2, OSPF, EIGRP & Python Simulations)
Cisco IOS command configurations provided in the `.pkt` topologies:
- **RIPv2 Configuration**:
  ```cisco
  Router(config)# router rip
  Router(config-router)# version 2
  Router(config-router)# no auto-summary
  Router(config-router)# network 192.168.10.0
  ```
- **OSPF Single-Area Configuration**:
  ```cisco
  Router(config)# router ospf 1
  Router(config-router)# network 192.168.10.0 0.0.0.255 area 0
  ```
- **EIGRP Configuration**:
  ```cisco
  Router(config)# router eigrp 100
  Router(config-router)# network 192.168.10.0 0.0.0.255
  Router(config-router)# no auto-summary
  ```

### Experiment 16: Multi-Service Enterprise Server Farm
Demonstrates complete enterprise server deployment in Cisco Packet Tracer:
- **Network Scheme**: `192.168.10.0/24`, Gateway: `192.168.10.1`, DNS: `192.168.10.12`.
- **Server Allocations**:
  - HTTP Server: `192.168.10.10`
  - FTP Server: `192.168.10.11` (User: `student`, Pass: `cisco`)
  - DNS Server: `192.168.10.12` (A Records for Web, FTP, Mail)
  - DHCP Server: `192.168.10.13` (Pool `192.168.10.100` to `.200`)
  - Mail Server: `192.168.10.15` (Domain: `dccn.local`, SMTP/POP3)
- **Router Remote Access (Telnet & SSH)**:
  ```cisco
  Router(config)# hostname R1
  Router(config)# ip domain-name dccn.local
  Router(config)# username admin secret cisco
  Router(config)# crypto key generate rsa modulus 1024
  Router(config)# line vty 0 4
  Router(config-line)# login local
  Router(config-line)# transport input telnet ssh
  ```

### Experiment 17: Python Socket Programming Implementation
Three production-grade socket routines implemented in [`solution/python/servers.py`](solution/python/servers.py):
1. **Multi-client TCP Chat Server**: Uses non-blocking socket loops and Python's `threading.Lock` to maintain a set of connected clients, broadcasting messages with client origin tags `[ip:port]`.
2. **HTTP Web Server**: Implements HTTP/1.1 request line parsing, MIME type resolution (`mimetypes.guess_type`), directory traversal protection (`path.resolve()` boundary checks), and standard HTTP status responses (`200 OK`, `400 Bad Request`, `404 Not Found`).
3. **Interactive FTP Daemon**: Implements RFC 959 session handling including `USER`, `PASS`, `SYST`, `PWD`, `CWD`, `LIST`, `RETR`, and `QUIT` commands.

### Experiment 18: Wireshark Packet Analysis & Protocol Dissection
Detailed capture filters and security evaluation protocols documented in [`solution/wireshark/wireshark_lab.md`](solution/wireshark/wireshark_lab.md):
- **Display Filters**:
  - `tcp.flags.syn == 1 and tcp.flags.ack == 0` (Identify TCP connection initiations)
  - `dns.flags.response == 0` (Identify DNS queries)
  - `ftp.request.command == "USER" || ftp.request.command == "PASS"` (Inspect plaintext credentials)
- **Security Takeaway**: Telnet and FTP pass credentials in cleartext; SSH and HTTPS protect communications using transport encryption (TLS / SSH-2 cryptographic negotiation).

---

## ❓ Frequently Asked Questions (FAQ)

### Q1: Which version of Cisco Packet Tracer is required to open the `.pkt` topologies?
> **Answer**: All `.pkt` files in `solution/packet-tracer/final/` are verified on **Cisco Packet Tracer 8.0, 8.1, and 8.2+**. Opening them in older versions (such as v7.x) may result in an incompatible XML schema warning.

### Q2: What is the primary difference between FLSM and VLSM?
> **Answer**: In **Fixed Length Subnet Masking (FLSM)**, every subnet in the network topology receives an identical subnet mask regardless of host capacity requirements, resulting in severe address wastage on small point-to-point links. In **Variable Length Subnet Masking (VLSM)**, subnet masks are allocated hierarchically according to the exact number of hosts required per segment (e.g., `/26` for 50 hosts, `/30` for router links), maximizing address conservation.

### Q3: How do I test the Python socket servers without external dependencies?
> **Answer**: The Python server file [`solution/python/servers.py`](solution/python/servers.py) was built exclusively using Python's built-in standard library (`socket`, `threading`, `argparse`, `pathlib`, `mimetypes`). You do not need `pip install` or any virtual environment. Simply execute with `python3 servers.py <chat|web|ftp>`.

### Q4: Why are Telnet and standard FTP marked as insecure in the lab reports?
> **Answer**: Both Telnet (RFC 854) and standard FTP (RFC 959) transmit control channel information—including usernames and passwords—as unencrypted ASCII cleartext. When inspected using Wireshark (Experiment 18), any packet analyzer on the same collision domain or switched network can read the credentials in plaintext via **Follow TCP Stream**. SSH and SFTP replace these by establishing an encrypted cryptographic tunnel.

### Q5: Can I submit the reports in `solution/docs/final/` for college lab assignments?
> **Answer**: Yes. The reports in [`solution/docs/final/`](solution/docs/final/) contain cleaned, academically formatted document templates with step-by-step setup guides, routing tables, and real configuration logs, replacing corrupted screenshots and incomplete notes.

---

## 📁 Repository Structure

```
.
├── CITATION.cff                      # Academic citation metadata
├── LICENSE                           # Open source MIT license
├── README.md                         # Main repository portal & documentation
├── SECURITY.md                       # Laboratory security policy & plaintext notice
├── llms.txt                          # Machine-readable overview for AI search engines
├── llms-full.txt                     # Detailed machine-readable technical reference
│
├── solution/                         # Primary curated solution pack
│   ├── README.md                     # Overview & submission guide
│   ├── assets/                       # High-resolution diagrams & topology renders
│   │   ├── experiment4_cables_connectors.png
│   │   └── experiment6_topologies.png
│   ├── docs/                         # Laboratory observation reports
│   │   ├── final/                    # Cleaned, submission-ready reports (Expt 10, 11, 13, 16)
│   │   ├── source/                   # Original lab manuals (Expt 4–9)
│   │   └── archive/                  # Version history & raw student templates
│   ├── guides/                       # Step-by-step configuration walk-throughs
│   │   └── packet_tracer_lab.md      # Cisco Packet Tracer configuration manual
│   ├── packet-tracer/                # Packet Tracer simulation topologies
│   │   ├── final/                    # Tested, production-ready .pkt models (Expt 4, 6, 10, 11, 13, 16)
│   │   └── legacy/                   # Historical and reference topology saves
│   ├── python/                       # Transport & Application Layer Socket Programs
│   │   ├── lab_root/                 # Root web & FTP static documents
│   │   │   └── index.html            # Default landing page
│   │   ├── README.md                 # Execution instructions
│   │   └── servers.py                # Chat, HTTP, and FTP server implementations
│   └── wireshark/                    # Packet sniffing & protocol analysis
│       ├── README.md                 # Filter reference
│       └── wireshark_lab.md          # Protocol inspection runbook
│
├── scripts/                          # Automated evidence & document generation utilities
│   ├── clean_experiment_docs.py
│   ├── make_evidence.py
│   ├── make_exp16_evidence.py
│   ├── make_experiment16_doc.py
│   ├── update_docs.py
│   └── MCP-Control-Center.pts
│
├── llms.txt                          # Machine-readable overview for AI engines (GEO)
├── llms-full.txt                     # Detailed protocol & topology knowledge base (GEO)
├── CITATION.cff                      # Academic citation metadata
└── SECURITY.md                       # Security policy & reporting guidelines
```

---

## 🏷️ GitHub Topics & SEO Discovery Tags

To maximize search visibility on GitHub and search engines, apply the following topics to your repository settings:

```text
computer-networks, cisco-packet-tracer, packet-tracer-topologies, dccn, python-sockets,
wireshark, networking-lab, routing-protocols, ospf, ripv2, eigrp, subnetting, vlsm,
socket-programming, btech-cse, educational-resource
```

---

## 📖 Citation & Academic Reference

If this repository assisted your coursework, academic research, or teaching curriculum, please consider citing it using the following format:

```bibtex
@misc{computer_networks_lab_2026,
  author = {Computer Networks Lab Contributors},
  title = {Computer Networks & DCCN Lab: Cisco Packet Tracer Topologies, Python Sockets, and Wireshark Protocol Analysis},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/jjf2009/computer-networks-lab}}
}
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Computer Networks & DCCN Lab Solutions",
  "description": "Comprehensive practical solutions for undergraduate computer networking coursework, featuring Cisco Packet Tracer topologies, Python socket programming, and Wireshark guides.",
  "keywords": "computer networks, packet tracer, python sockets, wireshark, dccn, ripv2, ospf, eigrp, subnetting",
  "educationalLevel": "Undergraduate",
  "teaches": "Computer Networks, Data Communications, Protocol Analysis, Socket Programming",
  "learningResourceType": "Laboratory Manual and Software Simulations",
  "license": "https://opensource.org/licenses/MIT",
  "url": "https://github.com/jjf2009/computer-networks-lab"
}
</script>

---

## 🤝 Contributing & License

Contributions, topology enhancements, and additional protocol analyzers are welcomed!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewProtocol`)
3. Commit your Changes (`git commit -m 'Add OSPF Multi-Area simulation'`)
4. Push to the Branch (`git push origin feature/NewProtocol`)
5. Open a Pull Request

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.
