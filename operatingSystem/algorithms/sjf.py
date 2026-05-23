import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    processes = []
    idx = 1
    for i in range(n):
        bt = int(input_data[idx])
        at = int(input_data[idx+1])
        processes.append([i, at, bt])
        idx += 2
        
    processes.sort(key=lambda x: (x[1], x[0]))
    
    completed = 0
    current_time = 0
    is_completed = [False] * n
    ct = [0] * n
    tat = [0] * n
    wt = [0] * n
    
    while completed < n:
        available = []
        for p in processes:
            if not is_completed[p[0]] and p[1] <= current_time:
                available.append(p)
        
        if not available:
            for p in processes:
                if not is_completed[p[0]]:
                    current_time = p[1]
                    break
            continue
            
        available.sort(key=lambda x: (x[2], x[1], x[0]))
        selected = available[0]
        pid = selected[0]
        
        current_time += selected[2]
        ct[pid] = current_time
        tat[pid] = ct[pid] - selected[1]
        wt[pid] = tat[pid] - selected[2]
        
        is_completed[pid] = True
        completed += 1
        
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    
    print(*(ct))
    print(*(tat))
    print(*(wt))
    print(f"{avg_wt:.2f} {avg_tat:.2f}")

if __name__ == '__main__':
    main()
