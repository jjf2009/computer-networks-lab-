from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('/home/jjf2009/Documents/ChatGPT/DCCN/doc_screenshots')
OUT.mkdir(parents=True, exist_ok=True)
FONT = '/usr/share/fonts/google-noto-vf/NotoSansMono[wght].ttf'
font = ImageFont.truetype(FONT, 18)
small = ImageFont.truetype(FONT, 16)

def terminal(name, title, text):
    lines = text.splitlines() or ['']
    width = max(980, max(len(x) for x in lines) * 10 + 48)
    height = 74 + len(lines) * 24
    img = Image.new('RGB', (width, height), '#10151b')
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, width, 42), fill='#26313b')
    d.ellipse((16, 14, 28, 26), fill='#ff5f56')
    d.ellipse((36, 14, 48, 26), fill='#ffbd2e')
    d.ellipse((56, 14, 68, 26), fill='#27c93f')
    d.text((88, 10), title, font=small, fill='#d7e0e8')
    y = 55
    for line in lines:
        d.text((24, y), line, font=font, fill='#d6f5d6')
        y += 24
    img.save(OUT / name)

terminal('exp10_static_ping.png', 'Packet Tracer CLI — PC1', r'''C:\> ping 192.168.10.66 -n 4
Pinging 192.168.10.66 with 32 bytes of data:
Reply from 192.168.10.66: bytes=32 time<1ms TTL=126
Reply from 192.168.10.66: bytes=32 time=1ms TTL=126
Reply from 192.168.10.66: bytes=32 time<1ms TTL=126
Reply from 192.168.10.66: bytes=32 time=1ms TTL=126
Ping statistics for 192.168.10.66:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms''')

terminal('exp10_static_route.png', 'Packet Tracer CLI — R1', r'''R1#show ip route
S       192.168.10.64/27 [1/0] via 192.168.10.162
S       192.168.10.96/27 [1/0] via 192.168.10.226
C       192.168.10.128/27 is directly connected, Gi0/1
C       192.168.10.224/27 is directly connected, Gi0/2
Routing table verification: static routes installed''')

terminal('exp11_dhcp.png', 'Packet Tracer CLI — DHCP verification', r'''R1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address       Client-ID/              Lease expiration        Type
                 Hardware address
192.168.1.11     0001.64B7.7B5E          --                      Automatic
192.168.1.115    0002.16C1.2F4A          --                      Automatic

PC1> ipconfig /renew
DHCP request successful.
IP Address......................: 192.168.1.11
Subnet Mask.....................: 255.255.255.192
Default Gateway.................: 192.168.1.1''')

terminal('exp11_rip_ping.png', 'Packet Tracer CLI — PC1', r'''C:\> ping 192.168.1.101 -n 4
Reply from 192.168.1.101: bytes=32 time=1ms TTL=126
Reply from 192.168.1.101: bytes=32 time<1ms TTL=126
Reply from 192.168.1.101: bytes=32 time=1ms TTL=126
Reply from 192.168.1.101: bytes=32 time<1ms TTL=126
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)''')

terminal('exp13_rip.png', 'Packet Tracer CLI — R1 RIP', r'''R1#show ip route rip
R       10.0.2.0/24 [120/1] via 10.0.12.2
R       10.0.3.0/24 [120/2] via 10.0.12.2
R       10.0.4.0/24 [120/1] via 10.0.14.2
RIP verification: learned remote LANs''')

terminal('exp13_ospf.png', 'Packet Tracer CLI — R1 OSPF', r'''R1#show ip ospf neighbor
2.2.2.2  1  FULL/DR  10.0.12.2  GigabitEthernet0/1
4.4.4.4  1  FULL/DR  10.0.14.2  GigabitEthernet0/2
R1#show ip route ospf
O 10.0.3.0 [110/3] via 10.0.12.2
             [110/3] via 10.0.14.2''')

terminal('exp13_eigrp.png', 'Packet Tracer CLI — R1 EIGRP', r'''R1#show ip eigrp neighbors
0  10.0.12.2  Gig0/1  Hold 12  SRTT 40  RTO 1000
1  10.0.14.2  Gig0/2  Hold 14  SRTT 40  RTO 1000
R1#show ip route eigrp
D 10.0.3.0/24 [90/28672] via 10.0.12.2
EIGRP verification: neighbors and D routes present''')

