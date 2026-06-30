customer = {
    "name": "Max",
    "age": 24,
    "city": "Dhaka"
}

print(customer)
print(customer["name"])
print(customer["age"])
print(customer["city"])

customer["name"] = "Lax"
print(customer["name"])
customer["name"] = "Wax"
print(customer["name"])

# print(customer["Game"])

print(customer.get("mail"))
print(customer.get("mail", "@gmail.com"))
print(customer.get("number", "1234"))
