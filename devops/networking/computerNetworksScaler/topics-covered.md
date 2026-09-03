# Computer Networks (Scaler) — Topics Covered

Index of every topic that appears across the handwritten lecture PDFs in this folder.
Source PDFs: `Introduction_to_Networks_.pdf` (9 p), `Note.pdf` (12 p), `IP_2_Group_A.pdf` (10 p).

---

## Lecture 1 — Introduction to Networks
*(`Introduction_to_Networks_.pdf`)*

### Course logistics
- Grading split — Assignments 35%, End term 40%, Quiz 25%
- PSPx / assignment section on the End term

### Course roadmap (the questions the course answers)
- Why networks?
- What travels (on a network)
- Who are you talking to → IP addresses
- How do we divide networks → Subnetting
- How do we find the destination → Graph algorithms
- How do routers send packets?
- How do humans use domains instead of IPs → DNS
- How do applications communicate → HTTP
- How to make communication reliable
- How do private networks work?
- Troubleshooting
- The complete journey (end-to-end)

### The end-to-end journey of a request
- Typing `www.google.co.in` — request, DNS lookup, server responds with HTML, routers
- Path: Laptop → Wi-Fi router → ISP → Internet → Google server
- Expanded path: Laptop → Wi-Fi router → ISP → Router → Routers → Google network → Google server
- Who owns the internet?

### Ways two hosts (A ↔ B) can be connected
- Direct connection
- Wi-Fi
- LAN
- Multiple intermediate networks
- Ordered vs. out-of-order delivery of chunks (C1…C5)
- Rate mismatch between sender and receiver (1000 c/s vs 100 c/s)

### Computer network fundamentals
- Definition — interconnected devices communicating and exchanging data/resources
- Components of a network:
  1. End devices / hosts
  2. Links
  3. Intermediate devices — switch, router, access points
  4. Protocols — HTTP, DNS, TCP, UDP, IP
  5. Types of network — LAN, WAN, Internet
  6. Client and server (requests a service vs. provides a service)
- Host → intermediate devices → host
- Can the internet be called one very large LAN? (No)

### Internet structure
- ISP (Internet Service Provider)
- IXP (Internet Exchange Point) — peering between networks
- Full device-to-server chain: Device — Router — ISP router — Router — Router — Google network — Google server
- Router graph / hops (R1…R8) to reach a server
- Physical distance matters → latency

### Network edge vs. network core
- Network edge — end points where communication starts / terminates
- Network core — intermediate devices
- Access networks
- Full flow: Network edge → Access network → Network core (R1→R2→R3→R4) → Access network → Network edge

### Devices
- Routers — decide where a packet goes (packet → router → N1/N2/N3)
- Switch — connects devices within a LAN (PCs ↔ switch)

### Packets
- What is inside a packet — Header + Data
- Packet switching vs. circuit switching
- Interleaving of packets from multiple sources (A/B/C) through a router

---

## Lecture 2 — Network Performance, Layering & Encapsulation
*(`Note.pdf`)*

### Network performance
- Bandwidth — max rate / capacity at which a link can transmit data (Kbps, Mbps, Gbps)
- Throughput — actual rate at which data is successfully transferred
- Bottleneck link along a path (D1 — Router — ISP — R2 — R3 — R4 — D2)
- Latency — time taken for data to travel through a network
- RTT (Round Trip Time)

### Network devices
- Router
- Switch — forwards Ethernet frames intelligently within a local network (port-based)
- Hub — broadcasts to all connected devices
- MAC address

### Networking layers
- Why layering — modularity, abstraction, independent evolution
- OSI model (Open Systems Interconnection), 7 layers:
  1. Physical
  2. Data Link
  3. Network
  4. Transport
  5. Session
  6. Presentation
  7. Application
- Protocols per layer — Application (HTTP, DNS), Transport (TCP, UDP), Network (IP), Data Link (Ethernet, Wi-Fi), Physical (radio, copper, fiber)
- "Think about" mapping per layer (what / which process / where / how to reach next hop / how are bits transmitted)

### Data representation
- "Hello" → ASCII values → binary (72 → 01001000)
- Bit vs. byte
- Units — 8 bits = 1 byte, 1000 bits = 1 Kb, 1000 bytes = 1 KB, Mb, MB
- MB/s vs. Mbps (100 Mbps = 12.5 MB/s)

### Delays
- Transmission delay — `d_trans = L / R` (packet length / transmission rate)
- Propagation delay — `d_prop = distance / propagation speed`

### Encapsulation & decapsulation
- Bits → frames → contains IP packet → contains transport data → contains application data
- Application layer — HTTP request (`GET /index.html HTTP/1.1`) → application data
- Transport layer — TCP header + application data = TCP segment; TCP payload
- Network layer — IP header + payload = IP packet / IP datagram
- Data link layer — Ethernet header + IP packet = Ethernet frame
- Physical layer
- Nesting: `[Ethernet [IP [TCP [Data]]] FCS]` — segment / packet / frame
- Definition of encapsulation
- What is a payload
- PDUs (Protocol Data Units)
- Decapsulation — receive bits → data link → network → transport → application
- Peer-layer communication between sender and receiver
- Router processing — only up to network/link layers (D1 → Router → D2)

### Header fields walked through
1. Application data — `GET /index.html HTTP/1.1`, `Host: www.google.co.in`
2. TCP header — source port, destination port, sequence / ACK, data
3. IP layer — source IP, destination IP, protocol, TCP segment; TTL decrementing across R1 → R2 → R3
4. Ethernet header — destination MAC, source MAC, EtherType, IP packet
- FCS — Frame Check Sequence
- Full nested frame diagram (Ethernet frame ⊃ IP packet ⊃ TCP segment ⊃ application data ⊃ FCS)
- How MAC changes hop-by-hop while IP stays end-to-end (D1 → R1 → R2 → D2; M1→M2, M2→M3, M3→M4)
- The three addresses — MAC address, IP address, port number

---

## Lecture 3 — IP Addressing II: Subnetting, VLSM & NAT
*(`IP_2_Group_A.pdf`)*

### Agenda
1. Local + remote + default gateway
2. Subnet
3. VLSM
4. IPv6 addresses *(listed on the agenda but not covered in these pages)*

### CIDR & masks
- Common CIDR reference table — /8, /16, /24, /25, /26, /27, /28, /30, /32 with subnet masks, usable hosts and common uses
- Reading a mask (255.255.224.0, /23) and computing 2^9 − 2 usable hosts

### Gateway & routing between networks
- Default gateway (e.g. 192.168.1.1) and the gateway router
- Networks A/B/C/D connected through an IXP

### Subnetwork
- Network address vs. host address (e.g. 144.255.1.36/24 → network 144.255.1.0/24)
- Number of unique IPs = 2^host-bits; usable hosts = 2^host-bits − 2
- Splitting a /24 into four /26 subnets (SST, SSB, Academy, AI Labs)
- For each subnet: network address, broadcast address, usable host range
- Steps for subnetting:
  1. Determine how many hosts you need
  2. Find smallest 2^N ≥ (hosts + 2)
  3. Host bits = N, prefix = 32 − N
  4. Subnet size (block) = 2^N
  5. Usable hosts = 2^N − 2
- Quick reference: hosts needed → min 2^N → prefix → usable hosts
- Practice: 50 hosts per subnet within 10.0.0.0/24

### VLSM (Variable Length Subnet Mask)
- Golden rule — allocate the largest subnet first, then work downwards
- Worked example on 192.168.10.0/24 for departments: Engineering (60), Marketing (30), HR (10), Management (5)
  - Engineering → /26 → 192.168.10.0/26, broadcast .63, hosts .1–.62
  - Marketing → /27 → 192.168.10.64/27, broadcast .95, hosts .65–.94
  - HR → /28 → 192.168.10.96/28, broadcast .111, hosts .97–.110
  - Management → /29 → 192.168.10.112/29, broadcast .119, hosts .113–.118
- Binary bit-splitting method for deriving each block
- Tracking the remaining range after each allocation

### NAT (Network Address Translation)
- Private IP ranges — 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 (sizes and common uses)
- NAT translation table — (private IP : private port) → (public IP : translated port)
- Worked example with public IP 203.0.113.5 and two internal hosts
- NAT variants:
  - SNAT — outgoing, replaces IP only (not port)
  - DNAT — incoming, port + IP
  - PAT (Port Address Translation) — many devices share one IP (port + IP)

---

## Notes
- `IP_2_Group_A.pdf` lists **IPv6 addresses** in its agenda, but the remaining pages stop at NAT — no IPv6 content is present in these files.
- There is no "IP 1" PDF in this folder, so local/remote addressing and the IPv4 address classes (if taught) are not captured here.
