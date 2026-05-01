# Introduction to Operating Systems

---

## TL;DR

An Operating System is a **resource manager and abstraction layer** that sits between hardware and user applications, providing a clean interface to complex hardware while enforcing fair, safe sharing of CPU, memory, and I/O devices. It is the most privileged software on the system, running in **kernel mode**, with direct hardware access. Without an OS, every application would have to manage hardware itself — making software near-impossible to write portably.

---

## Core Concepts

### What Is an Operating System?

An OS is a **system software** that:
1. **Manages hardware resources** — CPU time, RAM, disk, I/O devices.
2. **Provides abstractions** — files instead of raw disk sectors, processes instead of raw CPU states, sockets instead of raw network packets.
3. **Enforces isolation and protection** — prevents processes from corrupting each other or the kernel.

> **Why it matters:** Without an OS, two programs running simultaneously could write to the same memory address or fight over the CPU, causing chaos. The OS is the referee.

---

### The Dual-Mode Architecture (Kernel vs. User Mode)

Modern CPUs support at least two privilege levels:

| Mode        | Who Runs Here      | What It Can Do                            |
|-------------|--------------------|-------------------------------------------|
| Kernel Mode | OS Kernel          | Execute **any** instruction, access **any** memory, control hardware |
| User Mode   | Applications       | Restricted instruction set; must ask kernel via **system calls** |

The CPU enforces this via a **mode bit** in a status register (e.g., the `CPL` field in x86's `CS` register, or the `M` bit in RISC-V).

**Transition from User → Kernel:**
- **System Call (syscall):** Application deliberately requests OS service.
- **Interrupt:** Asynchronous signal from hardware (timer, I/O device).
- **Trap / Exception:** Synchronous event caused by an instruction (divide-by-zero, page fault, illegal opcode).

---

### System Calls — The OS API

A **system call** is the formal interface through which user programs request privileged OS services. From the application's perspective it looks like a function call, but under the hood:

1. Arguments are placed in registers / stack.
2. A special instruction (`syscall` / `int 0x80` / `svc`) switches to kernel mode.
3. The OS dispatches to the correct handler via the **syscall table**.
4. Results are returned, mode is switched back to user.

**Common syscall categories:**

| Category         | Examples (Linux)                     |
|------------------|--------------------------------------|
| Process control  | `fork`, `exec`, `exit`, `wait`       |
| File management  | `open`, `read`, `write`, `close`     |
| Device management| `ioctl`, `read`, `write` on device fds |
| Information      | `getpid`, `gettime`, `uname`         |
| Communication    | `pipe`, `socket`, `send`, `recv`     |

---

### What an OS Must Manage

#### 1. Process Management

A **process** is a program in execution — it includes the code, data, stack, heap, and OS metadata (PCB).

- The OS **multiplexes** the CPU among processes using **scheduling**.
- Each process gets an illusion of owning the whole CPU (**time-sharing**).
- **Context switch**: saving one process's CPU state (registers, PC) and loading another's.

**Key data structure:** Process Control Block (PCB)
```
PCB = {
  PID,          // Process identifier
  State,        // Running / Ready / Blocked / Zombie
  PC,           // Program counter
  Registers,    // CPU register snapshot
  Memory maps,  // Page tables / segments
  Open files,   // File descriptor table
  Priority,     // Scheduling priority
}
```

**Process States:**
```
New → Ready → Running → Terminated
                ↓  ↑
              Blocked (waiting for I/O)
```

#### 2. Memory Management

The OS provides each process an illusion of **contiguous, private address space** via **virtual memory**.

- Physical RAM is divided into **frames**; virtual address space into **pages** (typically 4 KB).
- The **page table** maps virtual page numbers → physical frame numbers.
- The **MMU** (Memory Management Unit, hardware) translates addresses on every memory access.
- A **TLB** (Translation Lookaside Buffer) caches recent translations for speed.
- If a page is not in RAM, a **page fault** triggers the OS to load it from disk (**demand paging**).

#### 3. File System Management

Abstracts raw disk blocks into a hierarchical namespace of files and directories.

- Provides uniform `open/read/write/close` semantics regardless of the underlying storage device.
- Manages **inodes** (metadata: size, owner, timestamps, block pointers) separate from data blocks.
- Handles **permissions** (read/write/execute for user/group/others on POSIX).

#### 4. I/O Management

- Provides **device drivers** — kernel modules that translate generic OS I/O commands into device-specific hardware operations.
- Uses **interrupts** so the CPU doesn't busy-wait for slow I/O to complete (interrupt-driven I/O).
- Maintains **I/O buffers** and **caches** to bridge the speed gap between CPU and disk.

#### 5. Security & Protection

- **Memory isolation**: page table entries enforce that process A cannot read process B's memory.
- **Privilege separation**: only the kernel can execute privileged instructions.
- **Access control**: the OS enforces who can read/write/execute files or communicate over networks.

---

### Types of Operating Systems

| Type                  | Characteristics                                        | Examples                  |
|-----------------------|-------------------------------------------------------|---------------------------|
| Batch OS              | Jobs queued and executed sequentially, no interaction | Early IBM mainframes       |
| Multiprogramming OS   | Multiple jobs in memory; CPU switches on I/O wait     | IBM OS/360                |
| Time-Sharing OS       | CPU rapidly switches giving interactive feel           | UNIX, Linux, macOS        |
| Real-Time OS (RTOS)   | Hard timing guarantees; used in embedded systems       | FreeRTOS, VxWorks         |
| Distributed OS        | Manages a cluster as a single coherent system          | Plan 9, Inferno           |
| Embedded OS           | Minimal footprint for constrained devices              | Android (Linux kernel), iOS |

---

### OS Structures / Architectures

| Architecture     | Description                                               | Pros / Cons                                |
|------------------|-----------------------------------------------------------|--------------------------------------------|
| **Monolithic**   | Entire OS in one large kernel binary (Linux, traditional UNIX) | Fast (no IPC overhead); hard to maintain  |
| **Microkernel**  | Only essential services in kernel; rest in user-space servers (Mach, MINIX) | Stable, modular; slower (IPC cost)        |
| **Layered**      | OS built in layers, each using services of the layer below | Clean design; rigid, hard to optimize      |
| **Modular**      | Monolithic core + loadable kernel modules (modern Linux)  | Flexible; widely used in practice          |
| **Exokernel**    | Kernel only multiplexes hardware; all abstraction in user-space libraries | Maximum performance; complex app code     |

---

## Syntax & Examples

### System Call Trace (Linux)

```bash
# Trace every syscall made by a process
strace ls /tmp

# Sample output snippet:
# execve("/usr/bin/ls", ["ls", "/tmp"], envp) = 0
# openat(AT_FDCWD, "/tmp", O_RDONLY|O_DIRECTORY) = 3
# getdents64(3, /* 5 entries */, 32768)  = 168
# write(1, "file1  file2\n", 13)          = 13
# close(3)                               = 0
# exit_group(0)                          = ?
```

> Every file open, directory read, and write to the terminal is a **system call** — the kernel is involved at every step.

---

### Process Lifecycle in Shell (fork + exec)

```c
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();         // Duplicate this process

    if (pid == 0) {
        // Child process
        execl("/bin/ls", "ls", "-l", NULL);  // Replace image with 'ls'
    } else {
        // Parent process
        wait(NULL);             // Block until child exits
    }
    return 0;
}
```

**What happens:**
1. `fork()` → OS clones PCB, page tables (copy-on-write).
2. `execl()` → OS replaces child's address space with `/bin/ls`.
3. `wait()` → Parent blocks; when child exits, OS reaps its PCB.

---

### Virtual Memory Address Translation

```
Virtual Address: 0x00403F10
─────────────────────────────
  VPN  (top bits) : 0x403   → page table lookup → PFN: 0x7A1
  Offset (bottom) : 0xF10
─────────────────────────────
Physical Address : (0x7A1 << 12) | 0xF10  =  0x7A1F10
```

---

## Mental Models / Analogies

### 🏢 The OS as a Hotel Manager

Think of the computer's hardware as a **hotel** with finite rooms (RAM), staff (CPU cores), and shared amenities (I/O devices).

- **Guests = Processes.** Each guest thinks they have a private room, but the manager (OS) controls room assignment and may temporarily store a guest's luggage offsite (swap to disk) when the hotel is full.
- **Room keys = Page Tables.** Each guest's key only opens *their* room — they physically cannot access another guest's room even if they try (memory isolation).
- **Front desk = System Call Interface.** Guests can't walk into the kitchen (kernel). They must ask the front desk (syscall) to get room service (I/O), which dispatches to the appropriate staff.
- **Do-Not-Disturb / Fire Alarm = Interrupts.** The manager can preemptively intervene (timer interrupt = fire alarm) to evict a guest who's overstayed (CPU time quantum exceeded).

This model captures **resource management, isolation, abstraction, and preemption** — the four pillars of an OS — in one coherent picture.

---

## Common Pitfalls

- **Confusing a process with a program.** A program is a static file on disk. A process is a running instance with its own state; the same program can have many processes.
- **Assuming syscalls are free.** Every syscall involves a mode switch (user → kernel → user), flushing pipeline state, and potentially a TLB shootdown. High-frequency syscalls (e.g., tiny `read()`s in a loop) are a known performance anti-pattern.
- **Treating virtual addresses as physical.** In a virtualized system, `&variable` gives you a *virtual* address. The physical location depends on page table mappings and can even be on disk (swapped out).
- **Forgetting that fork() duplicates file descriptors.** Both parent and child share the *same* underlying open-file descriptions (including offset). Closing in one doesn't close in the other unless you `close()` explicitly in each.
- **Assuming interrupts are only from hardware.** Software interrupts / traps (e.g., divide-by-zero, illegal instruction) also transfer control to the kernel and can be confused with hardware interrupts.
- **Thinking multiprogramming = multitasking.** Multiprogramming (keep CPU busy by switching on I/O) ≠ time-sharing (switch rapidly to give each user a responsive feel). Both are CPU scheduling strategies but with different goals.
- **Ignoring the kernel/user mode boundary in security analysis.** A bug in kernel-mode code (e.g., a driver) is far more dangerous than a user-space bug — it can compromise the entire system.

---

## Self-Test

1. **Mode Switch:** A process executes `read()` on a file. Trace the exact sequence of events from the user-space library call all the way to the hardware and back. At which points does the CPU's privilege level change, and why?

2. **Virtual Memory:** Two processes both have a variable at virtual address `0x7fff1234`. Explain why this doesn't cause a conflict, and describe the hardware + OS mechanism that makes this safe.

3. **Architecture Trade-offs:** A self-driving car's control system requires guaranteed sub-millisecond response to sensor input. Would you choose a monolithic OS like Linux or an RTOS like FreeRTOS? Justify your answer using specific OS concepts (scheduling, kernel mode overhead, interrupt latency).

---

*Source: Introduction to Operating Systems — Scaler Topics*
*Notes generated: 2026-04-28*
