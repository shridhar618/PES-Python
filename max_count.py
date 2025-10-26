from collections import Counter

items=[]
for i in range(10):
    item=input(f"Enter item {i+1}:")
    items.append(item)
    
count=Counter(items)

max_count=max(count.values())

most_common_items=[]
for item, count in count.items():
    if count==max_count:
        most_common_items.append(item)

print("\nMost common items(s):")
for item in most_common_items:
    print(f"{item} occurs {max_count} times")
    