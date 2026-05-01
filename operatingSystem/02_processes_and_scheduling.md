# Processes & CPU Scheduling

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

*Source: Handwritten Lecture Notes — Note_27_Apr_2026 (Scaler)*
*Notes generated: 2026-04-28*
