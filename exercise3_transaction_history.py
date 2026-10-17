# Exercise 3: Transaction History Analyzer

LAST_NAME = "De Silva"
SEED_NUM = "TUPM_26_4309"
FAVORITE_ARTIST = "Taylor Swift"

customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]
products = ["NOTEBOOK", "PEN", "USB", "HEADPHONES", "CALCULATOR"]
prices = [50, 20, 150, 500, 300]

seed = int(SEED_NUM[-1])
quantities = [(seed + ord(c)) % 5 + 1 for c in FAVORITE_ARTIST[:5]]

records = [
    (customers[0], products[0], quantities[0]),
    (customers[1], products[1], quantities[1]),
    (customers[2], products[2], quantities[2]),
    (customers[3], products[3], quantities[3]),
    (customers[4], products[4], quantities[4]),
    (customers[0], products[0], quantities[0])  # repeated purchase
]

print("TRANSACTION DATA:")
for customer, product, quantity in records:
    price = prices[products.index(product)]
    print(customer, product, quantity, price, quantity * price)

# Distinct customers and products
print("\nDISTINCT CUSTOMERS:")
print(set(x[0] for x in records))

print("\nDISTINCT PRODUCTS:")
print(set(x[1] for x in records))

# Transaction values
values = [x[2] * prices[products.index(x[1])] for x in records]

print("\nTRANSACTION VALUES:")
print(values)

print("\nTOTAL TRANSACTION VALUE:", sum(values))

# Customer summary
print("\nCUSTOMER SUMMARY:")
for customer in set(x[0] for x in records):
    print(customer, sum(x[2] * prices[products.index(x[1])]
                        for x in records if x[0] == customer))

# Product summary
print("\nPRODUCT SUMMARY:")
for product in set(x[1] for x in records):
    print(product, sum(x[2] for x in records if x[1] == product))

# Ordered results
print("\nORDERED RESULTS:")
print(sorted(records, key=lambda x: x[2], reverse=True))

# Overall summary
print("\nOVERALL SUMMARY:")
print("Transactions:", len(records))
print("Distinct customers:", len(set(x[0] for x in records)))
print("Distinct products:", len(set(x[1] for x in records)))
print("Total value:", sum(values))