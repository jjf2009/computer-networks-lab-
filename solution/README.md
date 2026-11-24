# DCCN One-Stop Lab Solution

This folder is an organized solution pack for the DCCN experiments. It contains the source experiment documents, finalized reports, working Cisco Packet Tracer projects, Python socket programs, and Wireshark guidance.

## Start here

1. Read [the Packet Tracer guide](guides/packet_tracer_lab.md).
2. Open the finalized reports in [docs/final](docs/final).
3. Open the matching `.pkt` file from [packet-tracer/final](packet-tracer/final).
4. Use [the Python README](python/README.md) for the socket programs.
5. Use [the Wireshark guide](wireshark/wireshark_lab.md) for protocol inspection.

## Final Packet Tracer projects

| Experiment | Project | Contents |
|---|---|---|
| 4 | `experiment4_cables_connectors.pkt` | Straight, crossover, coaxial, serial, and fiber links |
| 6 | `experiment6_topologies.pkt` | Bus, star, ring, mesh, and hybrid topologies |
| 10 | `experiment10_flsm_static.pkt` | FLSM addressing and static routing |
| 11 | `experiment11_vlsm_dhcp_ripv2.pkt` | VLSM, DHCP, and RIPv2 |
| 13 | `experiment13_rip.pkt`, `experiment13_ospf.pkt`, `experiment13_eigrp.pkt` | Dynamic-routing protocol variants |
| 16 | `experiment16_servers_completed.pkt` | HTTP, FTP, DNS, DHCP, Telnet, SSH, SMTP, and POP3 |

## Reports

- `docs/source` contains the original supplied documents for Experiments 4–9.
- `docs/final` contains the cleaned/finalized reports for Experiments 10, 11, 13, and 16.

The `packet-tracer/legacy` directory contains older or duplicate `.pkt` files retained for reference. Use the files in `packet-tracer/final` for submission.

## Important note

Experiment 4 is a physical-media study. Packet Tracer can demonstrate cable media and links, but it cannot physically model every connector sample such as RJ-45, BNC, SC, ST, LC, or USB connector construction.

All projects were saved from Packet Tracer automation and should be opened with Cisco Packet Tracer.
