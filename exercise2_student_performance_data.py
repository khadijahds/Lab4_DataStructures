# Exercise 2: Student Performance Data Analyzer

LAST_NAME = "De Silva"
SEED_NUM = "TUPM_26_4309"
FAVORITE_ARTIST = "Taylor Swift"

students = [f"{LAST_NAME}_S{i}" for i in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

seed = int(SEED_NUM[-1])
scores = [(seed + ord(c)) % 41 + 60 for c in FAVORITE_ARTIST[:5]]

records = list(zip(students, subjects, scores))
records.append(records[1])                 # repeated record
records.append((students[4], "PHYSICS", None))  # incomplete record

print("GENERATED PERFORMANCE DATA:")
print(records)

# Organized data
organized = {}
for student, subject, score in records:
    organized.setdefault(student, []).append((subject, score))

print("\nORGANIZED DATA:")
print(organized)

# Repeated and incomplete records
print("\nREPEATED RECORDS:")
print([x for x in set(records) if records.count(x) > 1])

print("\nINCOMPLETE RECORDS:")
print([x for x in records if x[2] is None])

# Performance categories
print("\nPERFORMANCE CATEGORIES:")
for student, subject, score in records:
    if score is not None:
        category = "PASS" if score >= 75 else "FAIL"
        print(student, subject, score, category)

# Summary
valid_scores = [x[2] for x in records if x[2] is not None]

print("\nSUMMARY:")
print("Highest:", max(valid_scores))
print("Lowest:", min(valid_scores))
print("Average:", sum(valid_scores) / len(valid_scores))

# Ordered results
print("\nORDERED RESULTS:")
print(sorted([x for x in records if x[2] is not None],
             key=lambda x: x[2], reverse=True))