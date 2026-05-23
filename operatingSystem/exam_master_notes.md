# Comprehensive OS & OOP Master Exam Notes

> [!NOTE]
> This master document consolidates Introduction to Operating Systems, Processes, CPU Scheduling, Numerical Problem Solving, and Object-Oriented Programming (OOP) into a single, high-yield exam preparation guide.

## Module 1: Introduction to Operating Systems

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




## Module 2: Processes & Threading Foundations

---

## TL;DR

A **process** is a running instance of a program — dynamic, in-memory, and managed by the OS. Because CPUs are singular resources shared among many processes, the OS uses **CPU scheduling** and **context switching** to give each process a time slice, creating the illusion of parallelism. The cost of these switches is non-zero, so scheduling strategy directly impacts system throughput and responsiveness.

---

## Core Concepts

### Program vs. Process

| | Program | Process |
|---|---|---|
| **Nature** | Static | Dynamic |
| **Location** | Disk (file) | RAM (execution state) |
| **Instances** | One | Many (e.g., Chrome runs multiple processes per tab) |

> **Why it matters:** A single `.exe` / binary can spawn dozens of processes simultaneously. Understanding this distinction is foundational — "killing a program" is actually terminating a *process*.

---

### How a CPU Actually Works

A single CPU core executes **one instruction at a time**. It contains:

```
┌─────────────────────────────┐
│         CPU Core            │
│  ┌───────┐  ┌───────────┐  │
│  │  ALU  │  │ Registers │  │
│  └───────┘  └───────────┘  │
│        ┌─────────┐         │
│        │  Cache  │         │
│        └─────────┘         │
└────────────┬────────────────┘
             │ Bus
      ┌──────┴───────┐
      │              │
   Memory           I/O
```

- **Registers:** Ultra-fast storage holding current instruction operands, the program counter (PC), flags.
- **Cache:** Small, fast memory tier between registers and RAM.
- **Bus:** Communication channel connecting CPU to Memory and I/O devices.

---

### What Is a Process?

A process is a **program in execution** — it holds:
- The program's code and data (loaded from disk into RAM)
- A **stack** (function calls, local vars) and **heap** (dynamic memory)
- A **PCB** (Process Control Block) — the OS's metadata record for this process

---

### Process Control Block (PCB)

The PCB is the OS's per-process data structure. It is saved/restored on every context switch.

```
PCB = {
  PID,          // Unique Process ID
  State,        // New | Ready | Running | Blocked | Suspended
  PC,           // Program Counter — next instruction address
  Registers,    // Snapshot of all CPU registers
  Memory Limits,// Base & bound, or page table pointer
  Open Files,   // File descriptor table
}
```

---

### Process States (Full State Machine)

```
         Admit
  NEW ──────────► READY ◄──────────────────────────────┐
                   │  ▲          Event Occurs           │
          Dispatch │  │ Timeout                    Blocked/Waiting
                   ▼  │                                 │
                RUNNING ──── Event/Wait/Interrupt ──────┘
                   │
                   └──── Release ──► STOP (Terminated)
```

**Extended with suspend states:**

| Transition | Trigger |
|---|---|
| New → Ready | OS admits the process |
| Ready → Running | Scheduler **dispatches** it (CPU assigned) |
| Running → Ready | **Timeout** — time quantum expired |
| Running → Blocked | Process waits for I/O or an event |
| Blocked → Ready | Awaited event occurs |
| Ready / Blocked → Suspended | OS swaps process out to disk (Medium-Term Scheduler) |
| Suspended → Ready | Swapped back in |
| Running → Stop | Process calls `exit()` or is killed |

---

### Context Switching

When the OS switches the CPU from one process to another:

1. **Save** the current process's CPU state (PC, registers) into its PCB.
2. **Load** the next process's state from its PCB.
3. CPU resumes execution of the new process exactly where it left off.

```
Timeline:
─────────────────────────────────────────────────────
CPU:  [ Executing P1 ] → [Save PCB1] → [Load PCB2] → [ Executing P2 ]
                                    ↑
                           Context Switch (overhead)
─────────────────────────────────────────────────────
```

**Key costs:**
- Happens **thousands of times per second**.
- Is **not free** — saving/loading state takes CPU cycles.
- **Too many switches** → overhead dominates → system slows down.
- **Too few switches** → poor responsiveness / starvation.

---

### CPU Scheduling

**CPU Scheduling** = the OS mechanism to select *which* process from the **Ready Queue** gets to run next on the CPU.

#### Time Slice / Quantum

Each process gets a small fixed **time quantum** (e.g., 5ms). After it expires, the scheduler preempts the process and picks the next one.

**Example with 4 processes:**
```
Time:  |  P1 (5s)  |  P2 (5s)  |  P3 (2s)  |  P4 (5s)  |  P1 (5s)  |  P4 (5s)  | ...
```
If P1 needs 70s total, after its first 5s slice → 65s remaining. It goes back to Ready Queue.

#### Wait Queues

Multiple I/O devices → multiple wait queues:
- **HDD Wait Queue** — processes blocked waiting for disk
- **Printer Wait Queue** — processes blocked waiting for printer

A process blocked on I/O sits in the appropriate device's wait queue until the device signals completion (via **interrupt**).

---

### Types of Schedulers

| Level | Name | Responsibility |
|---|---|---|
| **Long-Term (LTS)** | Admission Scheduler | Controls which new processes enter the Ready Queue; regulates **degree of multiprogramming** |
| **Medium-Term (MTS)** | Swapping Scheduler | Swaps processes in/out of memory to disk to manage RAM pressure |
| **Short-Term (STS)** | CPU Scheduler | Picks the next process from the Ready Queue to run; runs most frequently |

---

### Multitasking & `fork()`

**Multitasking** = running multiple processes concurrently by interleaving CPU time.

The OS provides `fork()` — a system call to create a **child process** that is an exact copy of the parent.

#### `fork()` Return Values

| Return Value | Meaning |
|---|---|
| `pid > 0` | You are the **Parent** — `pid` is the child's PID |
| `pid == 0` | You are the **Child** |
| `pid < 0` | **Error** — OS could not create child (e.g., resource limit) |

---

## Syntax & Examples

### `fork()` in C

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();   // OS creates a child process here

    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // --- CHILD PROCESS ---
        printf("Child: PID=%d, Parent PID=%d\n", getpid(), getppid());
    } else {
        // --- PARENT PROCESS ---
        printf("Parent: PID=%d, Child PID=%d\n", getpid(), pid);
        wait(NULL);   // Wait for child to finish before exiting
    }

    return 0;
}
```

**Execution without context switching:**
```
Parent runs completely → Child runs completely
```

**Execution with context switching (typical):**
```
Parent → Child → Parent → Child → ... (interleaved)
```

---

### Context Switch — What the CPU Sees

```
CPU Timeline:
┌──────────────┬──────────────────┬───────────────────┬──────────────┐
│ Executing P0 │  Save → PCB1     │  Reload ← PCB0    │ Executing P0 │
│              │  (Idle / Switch) │  (Idle / Switch)  │              │
└──────────────┴──────────────────┴───────────────────┴──────────────┘
                      ↑ overhead          ↑ overhead
```

- The CPU is **idle** during the save/reload window — pure overhead.
- The OS minimizes this by keeping PCB saves as minimal as possible.

---

## Mental Models / Analogies

### 🎯 The OS Scheduler as a Restaurant Kitchen

Imagine a **single chef** (CPU) and multiple **orders** (processes) coming in:

- Each order gets **5 minutes of chef time** (time quantum) before the chef moves to the next order — no single dish monopolizes the kitchen.
- The **order tickets** on the rail = the **Ready Queue**.
- When a dish needs the oven (I/O wait), the chef sets it aside in a **wait area** (blocked queue) and immediately picks up the next order.
- The **head chef** (Short-Term Scheduler) decides order priority; the **manager** (Long-Term Scheduler) controls how many orders enter at once so the kitchen isn't overwhelmed.
- **Switching between orders** (context switch) takes a moment to read the new ticket and pick up the right ingredients — that's the overhead. Too much switching and the chef spends more time reading tickets than cooking.

This captures **preemption, queuing, I/O blocking, and scheduling overhead** in one model.

---

## Common Pitfalls

- **Context switches happen in kernel mode.** The switch itself is not free user code — the OS does it, consuming CPU cycles that no user process benefits from.
- **`fork()` copies the entire process state.** After `fork()`, both parent and child have *independent* copies of variables. Modifying a variable in the child does **not** affect the parent (copy-on-write in practice, but logically independent).
- **`wait()` is mandatory to avoid zombies.** If a parent never calls `wait()` after the child exits, the child's PCB lingers as a **zombie process** — holding a PID slot indefinitely.
- **A blocked process is NOT on the Ready Queue.** It's on a device-specific wait queue. Only when its event occurs does it move back to Ready. Confusing these leads to wrong scheduling analysis.
- **Time quantum size is a trade-off.** Too small → excessive context switch overhead. Too large → poor interactivity (processes feel unresponsive). Typical Linux default: ~4–15ms.
- **Long-Term Scheduler is absent in many systems.** Interactive OSes (Linux desktop, Windows) admit processes on-demand, effectively bypassing LTS. MTS (swapping) handles overflow.
- **Multiprogramming ≠ parallelism.** On a single core, only one process runs at a time. The illusion of simultaneity is created purely by fast context switching.

---

## Self-Test

1. **PCB Deep Dive:** When a context switch occurs, exactly *which* fields of the PCB must be saved/restored, and why? What would happen if the Program Counter was not saved correctly?

2. **Scheduler Levels:** Your system has 200 processes competing for a single CPU. Describe the role each scheduler type (LTS, MTS, STS) plays in keeping the system stable and responsive. Which one runs most frequently?

3. **`fork()` Logic:** Given this code, how many times is `"Hello"` printed, and from how many distinct processes?
   ```c
   int main() {
       fork();
       fork();
       printf("Hello\n");
       return 0;
   }
   ```

---





## Module 3: CPU Scheduling Algorithms & Code

### Core Criteria
1. **CPU Utilization**: Percentage of time the CPU is active (Maximize).
2. **Throughput**: Number of processes completed per unit time (Maximize).
3. **Turnaround Time (TAT)**: Total time from arrival to completion (`TAT = CT - AT`) (Minimize).
4. **Waiting Time (WT)**: Total time spent in the ready queue (`WT = TAT - BT`) (Minimize).
5. **Response Time**: Time from arrival to first CPU allocation (Minimize).

### Standard Algorithms
| Algorithm | Type | Description |
|-----------|------|-------------|
| **FCFS** (First-Come, First-Serve) | Non-preemptive | Simple FIFO queue. Suffers from the **Convoy Effect** (short processes wait for a long one). |
| **SJF** (Shortest Job First) | Non-preemptive | Executes the process with the smallest burst time. Gives minimum average WT but requires burst time prediction. Can cause starvation. |
| **SRTF** (Shortest Remaining Time First) | Preemptive | Preemptive version of SJF. If a new process arrives with a shorter burst time than what's remaining on the current process, it preempts it. |
| **Priority** | Both | Executes highest priority first. Tie-breakers: lower arrival time, then smaller PID. Can cause starvation (solved via **Aging**). |
| **Round Robin (RR)** | Preemptive | Each process gets a fixed time quantum. Fair, but high context switch overhead if quantum is too small. Degrades to FCFS if quantum is very large. |
| **Multilevel Queue** | - | Processes divided into fixed queues (e.g., system vs. user) with own algorithms. No movement between queues. |
| **MLFQ** | Preemptive | Processes move between queues based on behavior (CPU bound vs I/O bound). Dynamic priority. |

> [!IMPORTANT]
> **Tie-Breaking Rules (Standard Assumptions):**
> 1. If priority is the same → Choose the one that arrived earlier (lower AT).
> 2. If arrival time is also the same → Choose the process with the smaller Process ID (PID).
> 3. Higher priority number = Higher priority.

### Java Implementations

#### SJF (Shortest Job First) Implementation Details
```java
// Logic snippet for Non-Preemptive SJF
int currentTime = 0;
int completedCount = 0;
int n = processes.length;

while (completedCount < n) {
    int selected = -1;
    int minBurst = Integer.MAX_VALUE;

    // Find the arrived process with the smallest Burst Time
    for (int i = 0; i < n; i++) {
        if (processes[i].at <= currentTime && !processes[i].completed) {
            if (processes[i].bt < minBurst) {
                minBurst = processes[i].bt;
                selected = i;
            }
            // Tie breaker for same BT: earlier arrival or lower PID handled implicitly if sorted
        }
    }

    if (selected == -1) {
        currentTime++; // Idle CPU, wait for process to arrive
        continue;
    }

    // Execute the selected process
    currentTime += processes[selected].bt;
    processes[selected].ct = currentTime;
    processes[selected].tat = processes[selected].ct - processes[selected].at;
    processes[selected].wt = processes[selected].tat - processes[selected].bt;
    processes[selected].completed = true;
    completedCount++;
}
```



## Module 4: Worked Numerical Examples

> [!TIP]
> **The 5-Step Numerical Methodology**
> 1. Draw Gantt Chart
> 2. Calculate Completion Time (CT)
> 3. Calculate Turnaround Time (TAT = CT - AT)
> 4. Calculate Waiting Time (WT = TAT - BT)
> 5. Compute Averages

### 1. FCFS Example
**Input Data:**
| Process | AT | BT |
|---------|----|----|
| P1      | 0  | 4  |
| P2      | 1  | 3  |
| P3      | 2  | 2  |

**Execution:**
- **Gantt Chart**: `| P1 (0-4) | P2 (4-7) | P3 (7-9) |`
- P1: CT=4, TAT=4, WT=0
- P2: CT=7, TAT=6, WT=3
- P3: CT=9, TAT=7, WT=5
- **Averages**: `WT = (0+3+5)/3 = 2.66`, `TAT = (4+6+7)/3 = 5.66`

### 2. SRTF (Preemptive SJF) Example
**Input Data:**
| Process | AT | BT |
|---------|----|----|
| P1      | 0  | 5  |
| P2      | 1  | 3  |
| P3      | 2  | 4  |
| P4      | 4  | 1  |

**Execution Trace:**
- `t=0`: P1 arrives (BT=5). Starts.
- `t=1`: P2 arrives (BT=3). P1 has 4 left. 3 < 4, so **P2 preempts P1**.
- `t=2`: P3 arrives (BT=4). P2 has 2 left. 2 < 4, so P2 continues.
- `t=4`: P4 arrives (BT=1). P2 finished at `t=4`. Ready Queue: P1(4), P3(4), P4(1).
- `t=4`: P4 (BT=1) is shortest. Runs to `t=5`.
- `t=5`: Ready Queue: P1(4), P3(4). Tie breaker: P1 arrived earlier.
- `t=5`: P1 runs to completion (`t=9`).
- `t=9`: P3 runs to completion (`t=13`).

**Gantt Chart:** `| P1 (0-1) | P2 (1-4) | P4 (4-5) | P1 (5-9) | P3 (9-13) |`



## Module 5: Object-Oriented Programming (OOP) Revisited

### Classes vs. Objects
- **Class**: The blueprint, template, or general design. Contains no actual real-world data, just variables and methods declarations. Example: `class Student`.
- **Object (Instance)**: The real-world entity created from the class blueprint, holding actual data in memory. Example: `Student s = new Student();`.

### Constructors
- Must have the **exact same name** as the class.
- **No return type** (not even `void`).
- Runs **automatically** when the object is instantiated using the `new` keyword.
- Primary purpose is to initialize object properties.

### Inheritance & Overriding
- **Inheritance (`extends`)**: Allows a child class to inherit common attributes/methods from a parent. E.g., `class Teacher extends Person`.
- **Method Overriding**: When a child provides its own specific implementation of a method already defined in its parent.
  > **OS Analogy**: A base `Task` class has an `execute()` method. `PrintTask`, `DownloadTask`, and `BackupTask` classes override `execute()` to perform specific operations while sharing the same method signature.

### Runtime Polymorphism ("Many Forms")
- **Concept**: A parent class reference can hold a child class object. The JVM resolves *which* method to call at runtime based on the **actual object type**, not the reference type.
```java
Animal a1 = new Dog();
Animal a2 = new Cat();
a1.sound(); // Output: Bark! (Executes Dog's version)
a2.sound(); // Output: Meow! (Executes Cat's version)
```

### Abstract Classes vs. Interfaces

| Feature | Abstract Class | Interface |
|---------|----------------|-----------|
| **Role** | Incomplete parent class (blueprint with common features) | Pure contract / rulebook |
| **Methods** | Can have both normal methods (with body) and abstract methods (no body) | Methods are `public abstract` by default (no body) |
| **Instantiation** | Cannot create objects directly (`new Vehicle()` is invalid) | Cannot create objects directly |
| **Keyword** | `abstract` (class and methods), uses `extends` | `interface`, uses `implements` |

> [!NOTE]
> **Why are interfaces critical for Java Operating System programming?**
> Java threads require tasks to run concurrently. Since Java does not support multiple inheritance, it provides the `Runnable` interface. Any class, regardless of what it inherits from, can implement `Runnable` by defining the `run()` method, making the task capable of running on an OS thread.

