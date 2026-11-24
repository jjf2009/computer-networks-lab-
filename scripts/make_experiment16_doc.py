from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT

ROOT=Path('/home/jjf2009/Documents/ChatGPT/DCCN')
DOC=Document()
sec=DOC.sections[0]
sec.top_margin=Inches(.65); sec.bottom_margin=Inches(.65)
styles=DOC.styles
styles['Normal'].font.name='Arial'; styles['Normal'].font.size=Pt(10)
for s in ['Title','Heading 1','Heading 2']:
    styles[s].font.name='Arial'

def title(t): DOC.add_heading(t,0)
def para(t=''): DOC.add_paragraph(t)
def table(headers, rows):
    t=DOC.add_table(rows=1, cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'
    for c,h in zip(t.rows[0].cells,headers): c.text=h
    for row in rows:
        cells=t.add_row().cells
        for c,v in zip(cells,row): c.text=str(v); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
    return t
def code(t):
    p=DOC.add_paragraph(); r=p.add_run(t); r.font.name='Courier New'; r.font.size=Pt(8.5)
def figure(caption,path):
    p=DOC.add_paragraph(caption); p.runs[0].bold=True
    q=DOC.add_picture(str(path),width=Inches(6.4)); DOC.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
    DOC.add_paragraph('Evidence captured from the live Cisco Packet Tracer project through the Packet Tracer automation interface.')

title('EXPERIMENT 16')
p=DOC.add_paragraph('Implementation of Network Services Using Cisco Packet Tracer')
p.alignment=WD_ALIGN_PARAGRAPH.CENTER
para('Name: ______________________________    Roll No.: ____________________')
para('Date: _______________________________')
DOC.add_heading('Aim',1)
para('To design and implement Web, FTP, DNS, DHCP, Telnet, SSH, and email services in Cisco Packet Tracer and verify each service from client devices.')
DOC.add_heading('Objectives',1)
for x in ['Configure a web server and access an HTML page using HTTP.','Configure an FTP server and authenticate a client.','Configure DNS records and resolve a host name.','Configure a DHCP server and obtain client addressing dynamically.','Configure Telnet and SSH remote access on a Cisco 2911 router.','Configure two email servers with four user accounts and test SMTP/POP3 mail delivery.']:
    DOC.add_paragraph(x,style='List Bullet')
DOC.add_heading('Network Topology',1)
para('The implementation uses one LAN with a router, two switches, four client PCs, and dedicated Packet Tracer Server-PT devices. A clean Cisco 2911 router R1 provides the verified Telnet/SSH service.')
figure('Figure 16.1: Implemented Packet Tracer topology',Path('/home/jjf2009/PacketTracerMCP/screenshots/experiment16_servers_topology.png'))
DOC.add_heading('Addressing Plan',1)
table(['Device','IPv4 address','Role'],[
['R1 Gi0/0','192.168.10.254/24','Telnet/SSH gateway'],
['Router0 Fa3/0','192.168.10.1/24','Existing LAN gateway'],
['Web Server','192.168.10.2/24','HTTP'],
['FTP_Server','192.168.10.3/24','FTP'],
['DNS_Server','192.168.10.4/24','DNS'],
['DHCP_Server','192.168.10.5/24','DHCP'],
['SSH_Telnet_Server','192.168.10.6/24','Server label / reference host'],
['Email_Server_1','192.168.10.7/24','SMTP/POP3: Alice, Bob'],
['Email_Server_2','192.168.10.8/24','SMTP/POP3: Carol, Dave'],
['PC0–PC3','DHCP leases .101–.104','Clients']])
DOC.add_heading('Service Configuration',1)
DOC.add_heading('1. Web server',2)
code('Web Server > Services > HTTP > On\nHTTP page: index.html\nURL tested: http://192.168.10.2')
DOC.add_heading('2. FTP server',2)
code('FTP_Server > Services > FTP > On\nUsername: ftpuser\nPassword: ftp123\nPermissions: RWDNL')
DOC.add_heading('3. DNS server',2)
code('DNS_Server > Services > DNS > On\nwww.dccn.local  A  192.168.10.2\nftp.dccn.local  A  192.168.10.3\nmail1.dccn.local A 192.168.10.7\nmail2.dccn.local A 192.168.10.8')
DOC.add_heading('4. DHCP server',2)
code('DHCP_Server > Services > DHCP > On\nPool: serverPool\nNetwork: 192.168.10.0 /24\nStart address: 192.168.10.100\nMaximum users: 50\nDefault gateway: 192.168.10.1\nDNS server: 192.168.10.4')
DOC.add_heading('5. Telnet and SSH server',2)
code('R1(config)# interface GigabitEthernet0/0\nR1(config-if)# ip address 192.168.10.254 255.255.255.0\nR1(config-if)# no shutdown\nR1(config)# ip domain-name dccn.local\nR1(config)# username admin privilege 15 secret Admin123\nR1(config)# enable secret Enable123\nR1(config)# crypto key generate rsa general-keys modulus 1024\nR1(config)# ip ssh version 2\nR1(config)# line vty 0 2\nR1(config-line)# login local\nR1(config-line)# transport input telnet\nR1(config)# line vty 3 4\nR1(config-line)# login local\nR1(config-line)# transport input ssh')
para('The VTY lines are split so Telnet and SSH are both enabled and independently verified.')
DOC.add_heading('6. Email servers',2)
code('Email_Server_1: domain dccn.local, SMTP On, POP3 On\n  alice / alice123\n  bob / bob123\nEmail_Server_2: domain dccn.local, SMTP On, POP3 On\n  carol / carol123\n  dave / dave123')
DOC.add_heading('Verification and Results',1)
para('All requested services were configured in the live Packet Tracer project. The following evidence records the successful tests.')
figure('Figure 16.2: Service configuration verification',ROOT/'exp16_evidence/service_summary.png')
figure('Figure 16.3: HTTP page retrieved by PC2',ROOT/'exp16_evidence/web.png')
figure('Figure 16.4: FTP authentication and directory listing',ROOT/'exp16_evidence/ftp.png')
figure('Figure 16.5: DNS name resolution',ROOT/'exp16_evidence/dns.png')
figure('Figure 16.6: DHCP client lease',ROOT/'exp16_evidence/dhcp.png')
figure('Figure 16.7: Telnet login and router command',ROOT/'exp16_evidence/telnet.png')
figure('Figure 16.8: SSH version-2 login and verification',ROOT/'exp16_evidence/ssh.png')
figure('Figure 16.9: Email account and SMTP/POP3 verification',ROOT/'exp16_evidence/email.png')
DOC.add_heading('Observed Results',1)
table(['Service','Verification performed','Result'],[
['HTTP','PC2 retrieved index.html from 192.168.10.2','Successful'],
['FTP','PC3 authenticated as ftpuser and listed the directory','Successful'],
['DNS','nslookup www.dccn.local using 192.168.10.4','Resolved to 192.168.10.2'],
['DHCP','PC0 obtained 192.168.10.102 dynamically','Lease successful'],
['Telnet','PC0 logged into R1 and ran show ip interface brief','Successful'],
['SSH','PC1 logged into R1; show ip ssh reported version 2.0','Successful'],
['Email','Alice sent mail to Carol; Carol issued POP3 receive','Successful']])
DOC.add_heading('Result',1)
para('A working Cisco Packet Tracer service network was implemented. HTTP, FTP, DNS, DHCP, Telnet, SSH, SMTP, and POP3 were configured and tested. Two email servers were used with four total users: Alice, Bob, Carol, and Dave.')
DOC.add_heading('Conclusion',1)
para('The experiment demonstrated the configuration and operation of common application-layer network services. Client-side tests confirmed web access, file transfer, name resolution, dynamic addressing, secure and insecure remote login, and email delivery.')
DOC.add_heading('Project File',1)
para('Saved Packet Tracer project: experiment16_servers_completed.pkt')
DOC.save(ROOT/'Experiment_16_Server_Protocols.docx')

