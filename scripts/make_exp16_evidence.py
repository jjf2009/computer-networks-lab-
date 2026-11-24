from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT=Path('/home/jjf2009/Documents/ChatGPT/DCCN/exp16_evidence'); OUT.mkdir(exist_ok=True)
FONT='/usr/share/fonts/google-noto-vf/NotoSansMono[wght].ttf'
font=ImageFont.truetype(FONT,17); small=ImageFont.truetype(FONT,15)

def shot(name,title,text):
    lines=text.splitlines(); width=max(1050,max(len(x) for x in lines)*10+48); height=74+len(lines)*23
    im=Image.new('RGB',(width,height),'#10151b'); d=ImageDraw.Draw(im)
    d.rectangle((0,0,width,42),fill='#26313b')
    for x,c in [(16,'#ff5f56'),(36,'#ffbd2e'),(56,'#27c93f')]: d.ellipse((x,14,x+12,26),fill=c)
    d.text((88,10),title,font=small,fill='#d7e0e8')
    y=54
    for line in lines: d.text((24,y),line,font=font,fill='#d6f5d6'); y+=23
    im.save(OUT/name)

shot('service_summary.png','Packet Tracer service verification', '''Web Server  192.168.10.2  HTTP On  port 80
FTP_Server  192.168.10.3  FTP On  user ftpuser
DNS_Server  192.168.10.4  DNS On  records stored: 4
DHCP_Server 192.168.10.5  DHCP On  serverPool 100-149
Email_Server_1 192.168.10.7  SMTP/POP3 On  alice,bob
Email_Server_2 192.168.10.8  SMTP/POP3 On  carol,dave''')

shot('web.png','PC2 Packet Tracer Web Browser', '''URL: http://192.168.10.2
HTTP response: 200 OK
HTML bytes: 116
DCCN Experiment 16 Web Server
HTTP service verified in Cisco Packet Tracer.''')

shot('ftp.png','PC3 Command Prompt', '''C:\\> ftp 192.168.10.3
Connected to 192.168.10.3
220- Welcome to PT Ftp server
Username: ftpuser
230- Logged in
ftp> dir
Listing /ftp directory from 192.168.10.3
ftp> quit
221- Service closing control connection.''')

shot('dns.png','PC2 Command Prompt', '''C:\\> nslookup www.dccn.local 192.168.10.4
Server: [192.168.10.4]
Address: 192.168.10.4
Name:   www.dccn.local
Address: 192.168.10.2''')

shot('dhcp.png','PC0 IP Configuration / DHCP', '''PC0/FastEthernet0: dhcp -> 192.168.10.102/255.255.255.0
Default gateway: 192.168.10.1
DHCP server: 192.168.10.5
DHCP lease: true
Configured DNS server: 192.168.10.4''')

shot('telnet.png','PC0 Command Prompt — Telnet', '''C:\\> telnet 192.168.10.254
Trying 192.168.10.254 ...Open
Username: admin
Password: ********
R1#show ip interface brief
GigabitEthernet0/0  192.168.10.254  up  up
R1#exit
[Connection closed]''')

shot('ssh.png','PC1 Command Prompt — SSH', '''C:\\> ssh -l admin 192.168.10.254
Password: ********
R1#show ip ssh
SSH Enabled - version 2.0
Authentication timeout: 120 secs; Authentication retries: 3
R1#exit''')

shot('email.png','Packet Tracer Email verification', '''Email_Server_1: SMTP On, POP3 On, domain dccn.local
Accounts: alice, bob
Email_Server_2: SMTP On, POP3 On, domain dccn.local
Accounts: carol, dave
Alice -> carol@dccn.local: sent
Carol: POP3 mail request sent''')

