# Security Policy

## Scope & Educational Nature
This repository contains reference solutions, Cisco Packet Tracer (`.pkt`) topologies, and Python socket programs designed **strictly for academic laboratory exercises and computer networking education**.

## Vulnerability & Plaintext Protocol Notice
Several experiments in this repository explicitly demonstrate unencrypted and legacy legacy networking protocols:
- **Experiment 16 & 17 (FTP, Telnet, HTTP, POP3/SMTP)**: These protocols transmit credentials and packet payloads in plaintext over the wire.
- **Experiment 18 (Wireshark)**: Specifically analyzes how packet sniffers capture unencrypted authentication sessions to contrast with secure protocols like **SSH** and **HTTPS**.

### Operational Safeguards
1. **Localhost & Isolated Subnets Only**: Run the Python socket servers (`chat`, `web`, `ftp`) exclusively bound to `127.0.0.1` or isolated virtual laboratory LAN subnets (e.g., `192.168.10.0/24`).
2. **Never Transmit Sensitive Data**: Do not use real production passwords, institutional credentials, or sensitive files when testing FTP or Telnet commands.
3. **No Production Use**: The Python server scripts are minimal teaching implementations and lack production hardening (rate limiting, TLS termination, multi-tier auth).

## Reporting a Security Concern
If you discover a security vulnerability or security defect in this repository's tooling or automation scripts, please submit an issue or contact the repository maintainers.
