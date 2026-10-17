# Exercise 1: Engineering Test Data Organizer

LAST_NAME = "De Silva"
SEED_NUM = "TUPM_26_4309"
FAVORITE_ARTIST = "Taylor Swift"

sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

# Generate values using the seed and artist
seed = 9
values = [(seed + ord(c)) % 100 for c in FAVORITE_ARTIST[:5]]

# Test records
records = list(zip(sources, categories, values))
records.append(records[0])  # repeated record
records += [(sources[1], "VOLTAGE", 50), (sources[1], "VOLTAGE", 60)]

print("GENERATED TEST DATA:")
print(records)

# Organize by category
organized = {}
for source, category, value in records:
    organized.setdefault(category, []).append(value)

print("\nORGANIZED DATA:")
print(organized)

# Distinct and repeated data
print("\nDISTINCT DATA:")
print(set(records))

print("\nREPEATED DATA:")
print([x for x in set(records) if records.count(x) > 1])

# Numerical summary
nums = [x[2] for x in records]
print("\nSUMMARY:")
print("Count:", len(nums))
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Average:", sum(nums) / len(nums))

# Categorical summary
print("\nCATEGORY SUMMARY:")
for category, vals in organized.items():
    print(category, "Count:", len(vals), "Average:", sum(vals) / len(vals))

# Ordered results
print("\nORDERED RESULTS:")
print(sorted(records, key=lambda x: x[2]))

# Final summary
print("\nFINAL SUMMARY:")
print("Total records:", len(records))
print("Distinct records:", len(set(records)))
print("Repeated records:", len(records) - len(set(records)))