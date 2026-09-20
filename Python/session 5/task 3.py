#Write a function remove_last_item(order_list) that pops the last item from a Zomato order list and returns the removed item.
#  Test it with a sample order_list

def remove_last_item(order_list):
    removed_items = order_list.pop()
    return removed_items
order_list= ["Pizza","Burger","Chilli Potato","ice-cream","coffee"]
print("The original list:-", order_list)
removed_items=remove_last_item(order_list)

print("Removed Items:-", removed_items)

print("The updated List are:-", order_list)