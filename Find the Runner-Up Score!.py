if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    r=set(arr)
    r=list(r)
    r.sort(reverse=True)
    print(r[1])
