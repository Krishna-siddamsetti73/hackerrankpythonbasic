if __name__ == '__main__':
    lsscr=[]
    pair=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pair.append([name,score])
        lsscr.append(score)
        
    lsscr=set(lsscr)
    lsscr=list(lsscr)
    lsscr.sort()
    r=lsscr[1]
    new=[x for x in pair if r in x]
    n=[]
    
  
    for x in new:
        for i in x:
            if type(i)==str:
                n.append(i)
    n.sort()
    for i in n:
        print(i)
    
