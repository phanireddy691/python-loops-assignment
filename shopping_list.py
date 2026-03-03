shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
#Task 1
shopping_list.append({"item": "Butter", "price": 80})
print(shopping_list)

shopping_list.pop(0)
print(shopping_list)

print(len(shopping_list))


#task 2
total_cost = sum(item["price"] for item in shopping_list)
most_expensive = min(shopping_list, key=lambda x: x["price"])


print(f"Most Expensive: {most_expensive['item']} - {most_expensive['price']}")
print(total_cost)

#3 task
# Create the summary dictionary
summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": round(total_cost / len(shopping_list), 2)
}

# Print the summary dictionary
print(summary)

