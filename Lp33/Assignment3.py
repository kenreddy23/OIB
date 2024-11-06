class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost = value / weight  # Cost per weight unit

def fractional_knapsack(capacity, items):
    # Sort items by cost (value/weight) in descending order
    items.sort(key=lambda item: item.cost, reverse=True)

    total_value = 0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            # Take the whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take the fraction of the remaining item
            total_value += item.cost * capacity
            capacity = 0  # Knapsack is now full

    return total_value

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    for _ in range(n):
        value = float(input("Enter the value of the item: "))
        weight = float(input("Enter the weight of the item: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))

    max_value = fractional_knapsack(capacity, items)
    print("Maximum value in the knapsack:", max_value)
    
    
    
    
    
    
    
    
    
    
    
    
    #input
#Enter the number of items: 3
#Enter the value of the item: 24
#Enter the weight of the item: 15
#Enter the value of the item: 25
#Enter the weight of the item: 15
#Enter the value of the item: 10
#Enter the weight of the item: 18
#Enter the capacity of the knapsack: 20
#Maximum value in the knapsack: 33.0

