#default arguements= they add a default value to choosen parameter to make function calling more flexible and reduce the mannual feeding of arguements 
def net_price(price, discount=0, sales_tax=0.05):#because most people get 0% discount and 0.05% sales tax, feeding those parameter is no longer required, i.e they are optional now
    return price + (1-discount)*(sales_tax)

customer1=net_price(500)#discount and sales tax are defaulted to pre-set value i.e. 0, 0.05 
print(customer1)

customer2=net_price(500, 20)#sales tax defaulted to 0.05% value
print(customer2) 

customer3=net_price(500, 20, 0)
print(customer3)
    