def nonConstructibleChange(coins):
    i = 1
    if len(coins) == 0:
        return 1
    coins = sorted(coins)
    while coins[i+1] -coins[i] == 0 or 1:
        new = list(range(coins[i],coins[i+1]))
        
        for num in new:
            a = 0
            while True:
                num =  num - coins[a]
                a +=1
                if num == 0:
                    break
                elif num > 0:
                    continue
                elif num < 0:
                    print(num)
        i += 1
        continue
    else:
        i += 1
        

    
    
            
            
           
    





nonConstructibleChange([5,7,1,1,2,3,22])




