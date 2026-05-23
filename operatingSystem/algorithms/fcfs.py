def main():
    input_data=sys.stdin.read().split()
    n = int(input_data[0])
    bt = (int(x) for x in input_data[1:n+1])
    wt = [0] * n
    tat = [0] * n
    wt[0] = 0
    tat[0] = bt[0]
    for i in range(n):
        wt[i] = wt[i-1]+bt[i-1]
        tat[i] = wt[i] + bt[i]
    avg_wt=sum(wt)/n
    avg_tat=sum(tat)/n
    print(*(wt),end=' \n')
    print(*(tat),end=' \n')
    print(f"{avg_wt:.2f}{avg_tat:.2f}")

if __name__ == '__main__'
    main()
