# Computer Networks (Scaler) — Topics Covered

Every topic named across all 9 classes of **Core Curriculum → SEM 3 (Term 1) → Subject 1: Computer Networks** (`m/402`).

| # | Class | Date | Source used |
|---|-------|------|-------------|
| 1 | Introduction to Computer Networks | 12 Aug 2026 | instructor PDF + class notes |
| 2 | Network Packets and Layered Communication | 19 Aug 2026 | instructor PDF + class notes |
| 3 | IP Addresses and Subnetting I | 21 Aug 2026 | class notes only (no PDF) |
| 4 | IP Addresses and Subnetting II | 2 Sep 2026 | instructor PDF |
| 5 | Graph Algorithms for Networking | 4 Sep 2026 | instructor PDF |
| 6 | Graph Algorithms for Networking II | 9 Sep 2026 | instructor PDF |
| 7 | Routing and Forwarding I | 11 Sep 2026 | **nothing — recording only** |
| 8 | Routing and Forwarding II | 16 Sep 2026 | not yet held |
| 9 | DNS and Internet Applications | 18 Sep 2026 | not yet held |

---

## 1 — Introduction to Computer Networks

**Course logistics**
- Grading split — Assignments 35%, End term 40%, Quiz 25%
- PSPx / assignment section in the End term

**Course roadmap**
- Why networks?
- What travels
- Who are you talking to → IP addresses
- How do we divide networks → Subnetting
- How do we find the destination → Graph algorithms
- How do routers send packets?
- How do humans use domains instead of IPs → DNS
- How do applications communicate → HTTP
- How to make communication reliable
- How do private networks work?
- Troubleshooting
- The complete journey

**The end-to-end journey**
- Typing `www.google.co.in` — request, DNS, server responds with HTML, routers
- Laptop → Wi-Fi router → ISP → Internet → Google server
- Laptop → Wi-Fi router → ISP → Router → Routers → Routers → Google network → Google server
- Who owns the internet?
- Postal-service analogy for packet routing

**Ways two hosts (A ↔ B) can connect**
- Direct connection
- Wi-Fi
- LAN
- Multiple intermediate networks
- Ordered vs. out-of-order delivery of chunks (C1…C5)
- Rate mismatch between sender and receiver (1000 c/s vs 100 c/s)

**Computer network fundamentals**
- Definition — interconnected devices communicating and exchanging data/resources
- Purpose of networks — sharing resources and information across distance
- Nodes and links
- Types of nodes — computers, routers, switches, hubs
- Components of a network
  1. End devices / hosts
  2. Links
  3. Intermediate devices — switch, router, access points
  4. Protocols — HTTP, DNS, TCP, UDP, IP
  5. Types of network — LAN, WAN, Internet
  6. Client and server
- Host → intermediate devices → host
- Client (requests a service) vs. server (provides a service)
- Can the internet be called one very large LAN? (No)

**Internet structure**
- ISP (Internet Service Provider)
- IXP (Internet Exchange Point) — peering between networks
- Device — Router — ISP router — Router — Router — Google network — Google server
- Router hop graph (R1…R8)
- Physical distance matters → latency

**Network edge vs. network core**
- Network edge — end points where communication starts / terminates
- Network core — intermediate devices
- Access networks
- Full flow — Network edge → Access network → Network core (R1→R2→R3→R4) → Access network → Network edge

**Devices**
- Routers — decide where a packet goes (packet → router → N1/N2/N3)
- Switch — connects devices within a LAN

**Packets and switching**
- What is inside a packet — Header + Data
- Circuit switching
- Packet switching
- Interleaving of packets from multiple sources (A/B/C) through a router

**Types of delay**
- Processing delay
- Queuing delay
- Transmission delay
- Propagation delay

**Other terms introduced**
- IP address
- Latency
- Reliability in networks — protocols, error checking, retransmission
- LAN (Local Area Network)
- WAN (Wide Area Network)

---

## 2 — Network Packets and Layered Communication

**Network performance**
- Bandwidth — max rate / capacity of a link (Kbps, Mbps, Gbps)
- Throughput — actual rate of successful transfer
- Bottleneck link along a path (D1 — Router — ISP — R2 — R3 — R4 — D2)
- Latency
- RTT (Round Trip Time)

**Network devices**
- Router
- Switch — forwards Ethernet frames intelligently within a local network (port-based)
- Hub — broadcasts to all connected devices
- MAC address

**Networking layers**
- Why layering — modularity, abstraction, independent evolution
- OSI model (Open Systems Interconnection), 7 layers — Physical, Data Link, Network, Transport, Session, Presentation, Application
- TCP/IP model, 5 layers — Physical, Data Link, Network, Transport, Application
- Protocols per layer — Application (HTTP, DNS, SMTP), Transport (TCP, UDP), Network (IP), Data Link (Ethernet, Wi-Fi), Physical (radio, copper, fiber)
- "Think about" mapping per layer — what / which process + how / where / how to reach next hop / how are bits transmitted
- Layer responsibilities — physical transmission, single-link framing, cross-network packet movement, end-to-end transfer, application protocols
- TCP — guaranteed delivery, flow control, congestion control
- UDP — faster, connectionless

**Data representation**
- "Hello" → ASCII values → binary (72 → 01001000)
- Bit vs. byte
- Units — 8 bits = 1 byte, 1000 bits = 1 Kb, 1000 bytes = 1 KB, 1000 Kb = 1 Mb, 1000 KB = 1 MB
- MB/s vs. Mbps (100 Mbps = 12.5 MB/s)

**Delays**
- Transmission delay — `d_trans = L / R`
- Propagation delay — `d_prop = distance / propagation speed`

**Encapsulation and decapsulation**
- Bits → frames → contains IP packet → contains transport data → contains application data
- Application layer — HTTP request (`GET /index.html HTTP/1.1`) → application data
- Transport layer — TCP header + application data = TCP segment; TCP payload
- Network layer — IP header + payload = IP packet / IP datagram
- Data link layer — Ethernet header + IP packet = Ethernet frame
- Physical layer
- Nesting — `[Ethernet [IP [TCP [Data]]] FCS]` — segment / packet / frame
- Definition of encapsulation
- What is a payload
- PDUs (Protocol Data Units)
- Decapsulation — receive bits → data link → network → transport → application
- Peer-layer communication between sender and receiver
- Router processing — only up to network / link layers (D1 → Router → D2)

**Header fields walked through**
1. Application data — `GET /index.html HTTP/1.1`, `Host: www.google.co.in`
2. TCP header — source port, destination port, sequence / ACK, data
3. IP layer — source IP, destination IP, protocol, TCP segment
4. Ethernet header — destination MAC, source MAC, EtherType, IP packet
- TTL and TTL decrementing across R1 → R2 → R3
- FCS — Frame Check Sequence
- Full nested Ethernet frame diagram
- MAC changes hop-by-hop while IP stays end-to-end (D1 → R1 → R2 → D2; M1→M2, M2→M3, M3→M4)

**The three addresses**
- MAC address
- IP address
- Port number

---

## 3 — IP Addresses and Subnetting I

> No instructor PDF uploaded. Topics below come from the auto-generated class notes.

**MTU and fragmentation**
- MTU (Maximum Transmission Unit)
- Ethernet standard MTU — 1500 bytes
- IP fragmentation
- Fragmenting a 2000-byte packet across a 1500-byte MTU
- Fragmentation overhead — more packets, more processing
- MSS (Maximum Segment Size)
- How TCP avoids fragmentation using MSS

**Ethernet frame structure**
- Preamble (8 bytes) — receiver clock synchronisation
- Destination MAC address (6 bytes)
- Source MAC address (6 bytes)
- EtherType (2 bytes)
- Payload (46–1500 bytes)
- Frame Check Sequence / FCS (4 bytes)

**MAC vs. IP addressing**
- MAC addresses — unique per device, local identification
- IP addresses — hierarchical and logical, used for routing across networks

**IP addressing and subnetting**
- IPv4 address composition — 32-bit, four decimal octets, 0–255
- Subnet mask — splits an address into network and host portions
- Classful addressing
  - Class A — first octet 1–127, first 8 bits network
  - Class B — first octet 128–191, first 16 bits network
  - Class C — first octet 192–223, first 24 bits network
- Network ID vs. Host ID
- CIDR (Classless Inter-Domain Routing)

**Protocol Data Unit (PDU) per layer**
- Application layer — application data
- Transport layer — TCP segment / UDP datagram
- Network layer — IP packet
- Data link layer — frame

**Key protocols**
- ARP (Address Resolution Protocol) — IP → MAC via broadcasting
- DNS (Domain Name System) — phonebook of the internet, URL → IP

---

## 4 — IP Addresses and Subnetting II

**Agenda**
1. Local + remote + default gateway
2. Subnet
3. VLSM
4. IPv6 addresses

**CIDR and masks**
- Common CIDR reference table — /8, /16, /24, /25, /26, /27, /28, /30, /32 with subnet masks, usable hosts, common uses
- Reading a mask — 255.255.224.0, /23, 2^9 − 2 = 510 usable hosts

**Gateway and routing between networks**
- Default gateway (e.g. `192.168.1.1`)
- Gateway router
- Networks A/B/C/D connected through an IXP

**Subnetwork**
- Network address vs. host address (`144.255.1.36/24` → `144.255.1.0/24`)
- Number of unique IPs = 2^host-bits
- Usable hosts = 2^host-bits − 2
- Splitting a /24 into four /26 subnets (SST, SSB, Academy, AI Labs)
- Per subnet — network address, broadcast address, usable host range
- Steps for subnetting
  1. Determine how many hosts you need
  2. Find smallest 2^N ≥ (hosts + 2)
  3. Host bits = N, prefix = 32 − N
  4. Subnet size (block) = 2^N
  5. Usable hosts = 2^N − 2
- Quick reference — hosts needed → min 2^N → prefix → usable hosts
- Practice — 50 hosts per subnet within `10.0.0.0/24`

**VLSM (Variable Length Subnet Mask)**
- Golden rule — allocate the largest subnet first, then work downwards
- Worked example on `192.168.10.0/24` — Engineering (60), Marketing (30), HR (10), Management (5)
  - Engineering → /26 → `192.168.10.0/26`, broadcast .63, hosts .1–.62
  - Marketing → /27 → `192.168.10.64/27`, broadcast .95, hosts .65–.94
  - HR → /28 → `192.168.10.96/28`, broadcast .111, hosts .97–.110
  - Management → /29 → `192.168.10.112/29`, broadcast .119, hosts .113–.118
- Binary bit-splitting method for deriving each block
- Tracking the remaining range after each allocation

**NAT (Network Address Translation)**
- Private IP ranges — `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` with sizes and common uses
- NAT translation table — (private IP : private port) → (public IP : translated port)
- Worked example with public IP `203.0.113.5` and two internal hosts
- NAT variants
  - SNAT — outgoing, replaces IP only (not port)
  - DNAT — incoming, port + IP
  - PAT (Port Address Translation) — many devices share one IP

---

## 5 — Graph Algorithms for Networking I

**Recap — encapsulation across the path**
- A → Wi-Fi router → ISP network → intermediate routers → destination network → B
- Application (Application + Presentation + Session) → application data
- Transport → src & dest PORT → segment
- Network → IP → network packet
- Data link → MAC → data frame
- Physical → transmitted

**Recap — local vs. remote delivery**
- Hosts on one LAN behind a gateway router (`192.168.1.24`, `192.168.1.27`, mask `255.255.255.0`, /24)
- ARP for resolving a local host's MAC
- Traffic to a different network (`192.168.10.31`) leaving via the gateway router

**IPv6**
- 128 bits = 2^128 ≈ 3.4 × 10^38 addresses
- Format — 8 groups of 4 hex digits separated by colons
- Compression rule 1 — omit leading zeros in each group
- Compression rule 2 — replace one sequence of consecutive zero groups with `::`
- Common IPv6 addresses — `::1` loopback, `::` unspecified/any, `fe80::/10` link-local, `ff00::/8` multicast, `2000::/3` global unicast
- IPv4 vs. IPv6 comparison — size, format, total addresses, header size, broadcast, NAT, ARP vs. NDP, fragmentation

**Network as a graph**
- Graph — collection of nodes and edges connecting them
- Vertices → routers / network devices
- Edges → network links between nodes
- Edge weights → latency, bandwidth, hop cost

**Graph representation**
- Weighted example — Delhi, Mumbai, Bangalore, Hyderabad, Chennai
- Adjacency list — `Map<String, Map<String, int>>`
- Adjacency matrix — 5×5 weight table

**Graph traversal**
- BFS (Breadth First Search)
- BFS code — `HashSet<Node> vst`, `Queue<Node> q`, `HashMap<Node,int> ans`
- BFS time complexity — `O(V + E)`
- BFS with path tracing
- Homework — dry run of BFS (shortest distance), path tracing

---

## 6 — Graph Algorithms for Networking II

**BFS with path trace**
- Worked trace on an 8-node graph (A–H) producing `(node, path)` pairs

**DFS (Depth First Search)**
- Recursive code — `void dfs(source)`
- Time complexity — `O(V + E)`
- Dry run on an 11-node graph (A–K) with visit ordering

**Cycle detection (undirected)**
- `bool isCyclePresent(src, parent)` with `parent` seeded as `NULL`
- Rule — a visited neighbour that is not the parent means a cycle
- Time complexity — `O(V + E)`
- Trace showing tree edges vs. the back edge

**Dijkstra's algorithm**
- 8-node weighted graph and final distance array
- Min-heap of `<dist, Node>`
- `insert(x)` and `extractMin()` — `log(N)`
- Min-heap syntax in Java
- Relaxation — `d_v = d_u + w(u→v)`
- Full hand-trace of every pop with stale entries struck out
- Stale-entry guard — `if (d == ans.get(u))`
- Code — `MinHeap<Pair<int,Node>> mh`, `HashMap<Node,int> ans` initialised to ∞

**Bellman–Ford algorithm**
- Relax all edges V−1 times
- Why edge order changes how fast it converges
- Iteration table across passes I / II / III
- Dry run on a graph with negative edge weights
- Handles negative weights (unlike Dijkstra)

**Routing protocol families**
- Distance Vector Routing (Bellman–Ford)
  - Each router knows costs to its direct neighbours
  - Periodically broadcasts its entire routing table to neighbours
  - Neighbours update their tables from received info
  - Converges over many rounds
  - Problem — count to infinity
  - Protocols — RIP, BGP
- Link State Routing (Dijkstra)
  - Each router floods its local link state (neighbours + costs) to ALL routers
  - Every router builds a complete topology map
  - Every router independently runs Dijkstra
  - Protocols — OSPF, IS-IS

---

## 7 — Routing and Forwarding I

No lecture notes and no class notes were uploaded for this class — only a session recording. Topics unknown.

## 8 — Routing and Forwarding II

Not yet held.

## 9 — DNS and Internet Applications

Not yet held.
