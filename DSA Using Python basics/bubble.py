stock_price=[2,1,3,4,3,5,6,4,3,8,57,2,3,]
for i in range(len(stock_price)-1):
    for j in range(len(stock_price)-1):
        if stock_price[j]>stock_price[j+1]:
            temp=stock_price[j]
            stock_price[j]=stock_price[j+1]
            stock_price[j+1]=temp
print(stock_price)            
            