# What is the probability that a customer purchases the product, 
# given that we know they visited the product page?
#THE main quetion is why I  used this why not this other is..
# We already know something happened, so we change our sample space and calculate the probability inside that smaller group.
import matplotlib.pyplot as plt 
class conditionalprob :
    def __init__(self , total_customers , no_visited , no_purchase) :
        self.total_customers = total_customers
        self.no_visited = no_visited 
        self.no_purchase = no_purchase
    def calclate (self) :
        p_A_and_p_B = self.no_purchase / self.total_customers
        p_B = self.no_visited / self.total_customers
        return p_A_and_p_B / p_B
total_customer = int(input("enter total no of customers"))
no_visited = int(input("enter your no_visited people"))
no_purchase = int(input("enter the no_puchase ahs done"))
S = conditionalprob(total_customer , no_visited , no_purchase)
k = S.calclate()
print("probability of people purchased who are visited" , k )
values = [no_visited , no_purchase]
labels = ["no_visited" , no_purchase]
plt.pie(values , labels = labels , autopct = "%1.1f%%")
plt.title("Purchase Probability Among Visitors")
plt.show()


        
        