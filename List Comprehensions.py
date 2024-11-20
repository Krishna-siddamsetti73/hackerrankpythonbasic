if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cr=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    
    new=[x for x in cr if(sum(i for i in x)!= n) ]
    print(new)
    
