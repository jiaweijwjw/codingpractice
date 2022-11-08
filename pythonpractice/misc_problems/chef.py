import heapq
from collections import deque

def calc_bill(time, order_time, prep_time, prep_rate, discount_rate):
    print(time, order_time, prep_time)
    wait_time = time - order_time
    bill = (prep_time*prep_rate) - (wait_time*discount_rate)
    return bill if bill > 0 else 0

def get_bills(orders, prep_rate, discount_rate):
    bills = []
    time = 0
    waiting_list = [] # this waiting list will hold all the orders that have come in and waiting to be prepared
    while len(orders) > 0 or len(waiting_list) > 0: # ensure all orders are processed, including those in the waiting queue
        if len(waiting_list) == 0: # nothing in waiting list
            order_time, prep_time = orders.popleft()
            time = order_time # set the time first before calc
            bills.append(calc_bill(time, order_time, prep_time, prep_rate, discount_rate))
            time += prep_time
        else:
            # note the sequence*
            prep_time, order_time = heapq.heappop(waiting_list) # take from waiting list the one with shortest prep time.
            bills.append(calc_bill(time, order_time, prep_time, prep_rate, discount_rate))
            time += prep_time
        
        for order in list(orders): # freeze the deque
            order_time, prep_time = order
            if order_time <= time:
                orders.popleft()
                heapq.heappush(waiting_list, (prep_time, order_time)) # flip the tuple for sorting by second element

    return bills

if __name__ == "__main__":

    # FOR READING INPUT FROM TERMINAL
    # num_test_cases = int(input())
    # num_orders, prep_rate, discount_rate = list(map(int, input().split())) # the rates are the costs / minute for prepping and waiting respectively
    # orders = []
    # for order in range(num_orders):
    #     order_time, prep_time = list(map(int, input().split()))
    #     orders.append((order_time, prep_time)) # store as a tuple and append to all orders

    # FOR QUICK TESTING
    # orders = [(3,5),(4,2),(4,1),(10,15),(15,2)]
    # prep_rate = 10
    # discount_rate = 1
    # orders = [(2,2),(6,1),(8,5),(10,1),(14,1)]
    # prep_rate = 4
    # discount_rate = 0
    orders = [(1,1),(2,1),(3,3),(3,2),(5,5)]
    prep_rate = 5
    discount_rate = 0

    print(get_bills(deque(orders), prep_rate, discount_rate))