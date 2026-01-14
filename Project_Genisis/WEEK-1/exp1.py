# 1. Create a list (The House)
list_a = [1, 2, 3]

# 2. Assign it to 'list_b' (The Trap)
list_b = list_a

# 3. Check their "Home Addresses"
print(f"Address of A: {hex(id(list_a))}")
print(f"Address of B: {hex(id(list_b))}")

# 4. Modify ONLY list_b
print("\nAdding '99' to list_b...")
list_b.append(99)

# 5. Check list_a (The Spooky Action)
print(f"List A is now: {list_a}")