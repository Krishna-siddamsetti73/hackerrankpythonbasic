if __name__ == '__main__':
    n = int(input())
    i = map(int, input().split())
    i=tuple(i)
    p=hash(i)
    print(p)
    
