from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path('/home/jjf2009/Documents/ChatGPT/DCCN')
PT = Path('/home/jjf2009/PacketTracerMCP/screenshots')
OUT = ROOT / 'updated_docs'
OUT.mkdir(exist_ok=True)

def add_evidence(doc, title, intro, items):
    doc.add_heading(title, level=1)
    p = doc.add_paragraph(intro)
    p.paragraph_format.space_after = Pt(8)
    for caption, image in items:
        doc.add_paragraph(caption).runs[0].bold = True
        pic = doc.add_picture(str(image), width=Inches(6.4))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph('Evidence source: live Cisco Packet Tracer API/CLI verification. Linux Packet Tracer does not expose a native GUI terminal screenshot, so this image preserves the captured command output in terminal form.')

def replace_result(doc, text):
    for idx, p in enumerate(doc.paragraphs):
        if p.text == 'RESULT':
            if idx + 1 < len(doc.paragraphs):
                doc.paragraphs[idx+1].text = text
            return

def process(src, out, result, heading, intro, items):
    doc = Document(src)
    replace_result(doc, result)
    add_evidence(doc, heading, intro, items)
    doc.save(out)

process(
 '/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_10.docx',
 OUT/'Kanak_DCCN_EXPT_10_implemented.docx',
 'The FLSM topology was implemented in Cisco Packet Tracer with four routers, four LANs, four WAN links, /27 addressing, and static routes. Repeated PC1-to-PC3 testing returned 4/4 replies, and R1 showed connected and static entries for the /27 networks.',
 'LIVE IMPLEMENTATION EVIDENCE — EXPERIMENT 10',
 'The following topology and command evidence were captured after implementing and verifying the saved Packet Tracer project experiment10_flsm_static.pkt.',
 [( 'Packet Tracer topology', PT/'experiment10_flsm_topology.png'),
  ( 'PC1-to-PC3 static-routing ping', ROOT/'doc_screenshots/exp10_static_ping.png'),
  ( 'R1 static routing table verification', ROOT/'doc_screenshots/exp10_static_route.png')])

process(
 '/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_11.docx',
 OUT/'Kanak_DCCN_EXPT_11_implemented.docx',
 'The VLSM topology was implemented with /26, /27, /28, /29, and /30 networks. Cisco IOS DHCP pools leased addresses to four PCs, and RIPv2 propagated the variable-length routes. The live binding table showed leases 192.168.1.11, 192.168.1.72, 192.168.1.101, and 192.168.1.115.',
 'LIVE IMPLEMENTATION EVIDENCE — EXPERIMENT 11',
 'The following evidence was captured after implementing and verifying the saved Packet Tracer project experiment11_vlsm_dhcp_ripv2.pkt.',
 [( 'Packet Tracer topology', PT/'experiment11_vlsm_topology.png'),
  ( 'DHCP binding and PC1 renewal verification', ROOT/'doc_screenshots/exp11_dhcp.png'),
  ( 'PC1-to-PC3 RIPv2 reachability test', ROOT/'doc_screenshots/exp11_rip_ping.png')])

process(
 '/home/jjf2009/Downloads/Vote_Prabhav_For_GS/Kanak_DCCN_EXPT_13.docx',
 OUT/'Kanak_DCCN_EXPT_13_implemented.docx',
 'RIPv2, OSPFv2, and EIGRP were implemented and verified on the same four-router testbed. Live route and neighbor commands confirmed learned routes for each protocol, and PC1-to-PC3 tests returned 4/4 replies. The report therefore records verified qualitative behavior; the original unsupported fabricated timing figures have not been retained as measurements.',
 'LIVE IMPLEMENTATION EVIDENCE — EXPERIMENT 13',
 'Three separate saved Packet Tracer states were produced: experiment13_rip.pkt, experiment13_ospf.pkt, and experiment13_eigrp.pkt. The evidence below records live neighbor, route, and reachability checks.',
 [( 'RIP topology', PT/'experiment13_rip_topology.png'),
  ( 'OSPF topology', PT/'experiment13_ospf_topology.png'),
  ( 'EIGRP topology', PT/'experiment13_eigrp_topology.png'),
  ( 'RIP route verification', ROOT/'doc_screenshots/exp13_rip.png'),
  ( 'OSPF neighbor and route verification', ROOT/'doc_screenshots/exp13_ospf.png'),
  ( 'EIGRP neighbor and route verification', ROOT/'doc_screenshots/exp13_eigrp.png')])

