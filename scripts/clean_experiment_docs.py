from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

ROOT=Path('/home/jjf2009/Documents/ChatGPT/DCCN')
DL=Path('/home/jjf2009/Downloads/Vote_Prabhav_For_GS')
OUT=ROOT/'cleaned_docs'; OUT.mkdir(exist_ok=True)

def remove_p(p):
    p._element.getparent().remove(p._element)

def clean_doc(src, out, keep_fig_prefix, result_text, extra_remove=()):
    d=Document(src)
    draw_count=0
    for p in list(d.paragraphs):
        txt=p.text.strip()
        if any(txt.startswith(x) for x in extra_remove):
            remove_p(p); continue
        if txt.startswith('Figure ') and not txt.startswith(keep_fig_prefix):
            remove_p(p); continue
        if 'Screenshot' in txt and not txt.startswith(keep_fig_prefix):
            remove_p(p); continue
        if 'w:drawing' in p._element.xml:
            draw_count += 1
            if draw_count > 1: remove_p(p)
    for idx, p in enumerate(d.paragraphs):
        if p.text.strip()=='RESULT':
            if idx >= 0 and idx+1 < len(d.paragraphs):
                d.paragraphs[idx+1].text=result_text
            break
    d.save(out)

def add_commands(path, heading, intro, blocks):
    d=Document(path)
    d.add_heading(heading, level=1)
    d.add_paragraph(intro)
    for label, text in blocks:
        d.add_paragraph(label).runs[0].bold=True
        p=d.add_paragraph()
        r=p.add_run(text); r.font.name='Courier New'; r.font.size=Pt(8.5)
    d.save(path)

# Experiment 10
p10=OUT/'Kanak_DCCN_EXPT_10_updated.docx'
clean_doc('/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_10.docx',p10,'Figure 10.1',
 'The FLSM topology was implemented with four routers, four LANs, four WAN links, /27 addressing, and static routing. The setup commands below are the required CLI configuration for the implemented design.',
 extra_remove=('OBSERVATIONS AND VERIFICATION',))
add_commands(p10,'CLI COMMANDS USED FOR SETUP','Use these commands on the four routers after cabling and assigning the PC addresses.',[
('R1 — interfaces and static routes','''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.10.1 255.255.255.224
 no shutdown
interface GigabitEthernet0/1
 ip address 192.168.10.129 255.255.255.224
 no shutdown
interface GigabitEthernet0/2
 ip address 192.168.10.226 255.255.255.224
 no shutdown
ip route 192.168.10.32 255.255.255.224 192.168.10.130
ip route 192.168.10.64 255.255.255.224 192.168.10.130
ip route 192.168.10.96 255.255.255.224 192.168.10.225
ip route 192.168.10.160 255.255.255.224 192.168.10.130
ip route 192.168.10.192 255.255.255.224 192.168.10.225
end
copy running-config startup-config'''),
('R2 — interfaces and static routes','''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.10.33 255.255.255.224
 no shutdown
interface GigabitEthernet0/1
 ip address 192.168.10.130 255.255.255.224
 no shutdown
interface GigabitEthernet0/2
 ip address 192.168.10.161 255.255.255.224
 no shutdown
ip route 192.168.10.0 255.255.255.224 192.168.10.129
ip route 192.168.10.64 255.255.255.224 192.168.10.162
ip route 192.168.10.96 255.255.255.224 192.168.10.162
ip route 192.168.10.192 255.255.255.224 192.168.10.162
ip route 192.168.10.224 255.255.255.224 192.168.10.129
end
copy running-config startup-config'''),
('R3/R4 — repeat the same interface and ip route pattern','''R3: Gi0/0=192.168.10.65/27, Gi0/1=192.168.10.162/27, Gi0/2=192.168.10.193/27
R4: Gi0/0=192.168.10.97/27, Gi0/1=192.168.10.194/27, Gi0/2=192.168.10.225/27
On every router:
show ip interface brief
show ip route
ping <remote-router-or-PC-address>''')])

# Experiment 11
p11=OUT/'Kanak_DCCN_EXPT_11_updated.docx'
clean_doc('/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_11.docx',p11,'Figure 11.1',
 'The VLSM topology was implemented using /26, /27, /28, /29, and /30 networks. DHCP pools and RIPv2 were configured using the CLI commands below; the clients then obtained dynamic addresses.',
 extra_remove=('OBSERVATIONS AND VERIFICATION',))
add_commands(p11,'CLI COMMANDS USED FOR SETUP','Configure the interfaces, DHCP pools, and RIPv2 on the three routers.',[
('R1 — Engineering and Server Farm','''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.192
 no shutdown
interface GigabitEthernet0/1
 ip address 192.168.1.113 255.255.255.248
 no shutdown
ip dhcp excluded-address 192.168.1.1 192.168.1.10
ip dhcp excluded-address 192.168.1.113 192.168.1.114
ip dhcp pool ENG_POOL
 network 192.168.1.0 255.255.255.192
 default-router 192.168.1.1
 dns-server 8.8.8.8
ip dhcp pool SERVER_POOL
 network 192.168.1.112 255.255.255.248
 default-router 192.168.1.113
 dns-server 8.8.8.8
router rip
 version 2
 no auto-summary
 network 192.168.1.0
end
copy running-config startup-config'''),
('R2 — Sales and WAN','''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.65 255.255.255.224
 no shutdown
interface Serial0/0/0
 ip address 192.168.1.122 255.255.255.252
 no shutdown
interface Serial0/0/1
 ip address 192.168.1.125 255.255.255.252
 no shutdown
ip dhcp excluded-address 192.168.1.65 192.168.1.70
ip dhcp pool SALES_POOL
 network 192.168.1.64 255.255.255.224
 default-router 192.168.1.65
 dns-server 8.8.8.8
router rip
 version 2
 no auto-summary
 network 192.168.1.0
end
copy running-config startup-config'''),
('R3 — HR and WAN','''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.97 255.255.255.240
 no shutdown
interface Serial0/0/0
 ip address 192.168.1.126 255.255.255.252
 no shutdown
interface Serial0/0/1
 ip address 192.168.1.129 255.255.255.252
 no shutdown
ip dhcp excluded-address 192.168.1.97 192.168.1.100
ip dhcp pool HR_POOL
 network 192.168.1.96 255.255.255.240
 default-router 192.168.1.97
 dns-server 8.8.8.8
router rip
 version 2
 no auto-summary
 network 192.168.1.0
end
copy running-config startup-config'''),
('Client and verification commands','''PC1, PC2, PC3, PC4: Desktop > IP Configuration > DHCP
Router#show ip dhcp binding
Router#show ip route
PC>ipconfig /renew
PC>ping <remote-PC-address>''')])

# Experiment 13
p13=OUT/'Kanak_DCCN_EXPT_13_updated.docx'
clean_doc('/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_13.docx',p13,'Figure 13.1',
 'RIPv2, OSPFv2, and EIGRP were implemented on the same four-router topology. The commands below provide the protocol setup and verification; no unsupported terminal screenshots or fabricated timing measurements are used.',
 extra_remove=('EXPERIMENTAL PERFORMANCE EVALUATION','To compare performance','Figure 13.2','Key Analytical Findings','Convergence Speed:','LSA Recalculation:','Protocol Overhead:','Resource Utilization:'))
add_commands(p13,'CLI COMMANDS USED FOR SETUP','Apply one routing protocol at a time on all four routers, then use the verification commands.',[
('Common interface addressing','''R1: Gi0/0 10.0.1.1/24, Gi0/1 10.0.12.1/30, Gi0/2 10.0.14.1/30
R2: Gi0/0 10.0.2.1/24, Gi0/1 10.0.12.2/30, Gi0/2 10.0.23.1/30
R3: Gi0/0 10.0.3.1/24, Gi0/1 10.0.23.2/30, Gi0/2 10.0.34.1/30
R4: Gi0/0 10.0.4.1/24, Gi0/1 10.0.34.2/30, Gi0/2 10.0.14.2/30
interface <interface>
 ip address <address> <mask>
 no shutdown'''),
('RIPv2 — on every router','''router rip
 version 2
 no auto-summary
 network 10.0.0.0
end
copy running-config startup-config
show ip route rip'''),
('OSPFv2 — example for R1; change networks/router-id per router','''no router rip
router ospf 1
 router-id 1.1.1.1
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.14.0 0.0.0.3 area 0
end
copy running-config startup-config
show ip ospf neighbor
show ip route ospf'''),
('EIGRP — on every router','''no router ospf 1
router eigrp 100
 eigrp router-id 1.1.1.1
 no auto-summary
 network 10.0.0.0
end
copy running-config startup-config
show ip eigrp neighbors
show ip route eigrp'''),
('End-to-end verification','''PC1>ping 10.0.3.10
Router#show ip interface brief
Router#show ip route
Repeat the same verification after selecting each routing protocol.''')])

# Experiment 16 in the same structure
d=Document()
d.sections[0].top_margin=Inches(.65); d.sections[0].bottom_margin=Inches(.65)
d.styles['Normal'].font.name='Arial'; d.styles['Normal'].font.size=Pt(10)
d.add_paragraph('Experiment No: 16\tDate: 24/11/2026')
d.add_paragraph('Aim: Implement Web, FTP, DNS, DHCP, Telnet, SSH, and email services using Cisco Packet Tracer.')
d.add_paragraph('Theory:')
d.add_paragraph('Application-layer services provide common network functions. HTTP delivers web pages, FTP transfers files, DNS maps names to IP addresses, DHCP provides dynamic host configuration, Telnet and SSH provide remote CLI access, and SMTP/POP3 provide email delivery and retrieval.')
d.add_paragraph('REQUIREMENTS')
for x in ['1 Cisco 2911 router','2 Cisco 2960-24TT switches','8 Server-PT devices / service endpoints','4 PCs','Copper straight-through cables','Cisco Packet Tracer']:
    d.add_paragraph(x)
d.add_heading('NETWORK TOPOLOGY ARCHITECTURE',1)
d.add_paragraph('The topology contains a LAN gateway, a server farm, four clients, dedicated service servers, two email servers, and a clean Cisco 2911 router R1 for Telnet and SSH.')
p=d.add_paragraph('Figure 16.1: Experiment 16 network topology')
d.add_picture('/home/jjf2009/PacketTracerMCP/screenshots/experiment16_servers_topology.png',width=Inches(6.4))
d.add_paragraph('ADDRESSING PLAN')
t=d.add_table(rows=1,cols=3); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
for c,v in zip(t.rows[0].cells,['Device','IP address','Service']): c.text=v
for row in [('R1','192.168.10.254/24','Telnet/SSH'),('Web Server','192.168.10.2/24','HTTP'),('FTP_Server','192.168.10.3/24','FTP'),('DNS_Server','192.168.10.4/24','DNS'),('DHCP_Server','192.168.10.5/24','DHCP'),('Email_Server_1','192.168.10.7/24','SMTP/POP3'),('Email_Server_2','192.168.10.8/24','SMTP/POP3'),('PC0-PC3','DHCP','Clients')]:
    cells=t.add_row().cells
    for c,v in zip(cells,row): c.text=v
d.add_paragraph('SERVER CONFIGURATION')
for label,txt in [
('HTTP','Web Server > Services > HTTP > On; edit index.html.'),
('FTP','FTP_Server > Services > FTP > On; user ftpuser, password ftp123, permissions RWDNL.'),
('DNS','DNS_Server > Services > DNS > On; add www.dccn.local → 192.168.10.2, ftp.dccn.local → 192.168.10.3, mail1.dccn.local → 192.168.10.7, mail2.dccn.local → 192.168.10.8.'),
('DHCP','DHCP_Server > Services > DHCP > On; pool serverPool, network 192.168.10.0/24, start 192.168.10.100, maximum 50 users, gateway 192.168.10.1, DNS 192.168.10.4.'),
('Email','Email_Server_1: alice/alice123 and bob/bob123. Email_Server_2: carol/carol123 and dave/dave123. Enable SMTP and POP3 with domain dccn.local.')]:
    d.add_paragraph(label+':').runs[0].bold=True; d.add_paragraph(txt)
d.add_paragraph('CISCO IOS TELNET AND SSH COMMANDS')
p=d.add_paragraph(); r=p.add_run('''enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.10.254 255.255.255.0
 no shutdown
ip domain-name dccn.local
username admin privilege 15 secret Admin123
enable secret Enable123
crypto key generate rsa general-keys modulus 1024
ip ssh version 2
line vty 0 2
 login local
 transport input telnet
line vty 3 4
 login local
 transport input ssh
end
copy running-config startup-config'''); r.font.name='Courier New'; r.font.size=Pt(8.5)
d.add_paragraph('PRACTICAL PROCEDURE')
for x in ['Place the router, switches, servers, and PCs on the Packet Tracer workspace.','Connect the LAN devices with Copper Straight-Through cables.','Assign the static addresses in the addressing plan.','Configure the service tabs and create the email accounts.','Configure R1 with the Telnet and SSH commands.','Set the PCs to DHCP and test each service from the Desktop applications or Command Prompt.']:
    d.add_paragraph(x)
d.add_paragraph('OBSERVATIONS AND VERIFICATION')
d.add_paragraph('Use the following commands to verify the implementation:')
p=d.add_paragraph(); r=p.add_run('''PC>ipconfig /all
PC>ping 192.168.10.2
PC>nslookup www.dccn.local 192.168.10.4
PC>ftp 192.168.10.3
PC>telnet 192.168.10.254
PC>ssh -l admin 192.168.10.254
R1#show ip ssh'''); r.font.name='Courier New'; r.font.size=Pt(8.5)
d.add_paragraph('PRECAUTIONS')
for x in ['Use unique IP addresses for every server.','Use a local username for VTY authentication.','Generate RSA keys before enabling SSH.','Keep the DNS server address consistent with the DHCP pool.','Use different email accounts for SMTP/POP3 testing.']:
    d.add_paragraph(x)
d.add_paragraph('RESULT')
d.add_paragraph('HTTP, FTP, DNS, DHCP, Telnet, SSH, SMTP, and POP3 services were configured in Cisco Packet Tracer. Two email servers were configured for four users.')
d.add_paragraph('Conclusion:')
d.add_paragraph('The experiment demonstrated the implementation and verification of common network application services using Cisco Packet Tracer.')
d.save(OUT/'Experiment_16_Server_Protocols_updated.docx')

print('created', *sorted(str(x) for x in OUT.glob('*.docx')), sep='\n')

