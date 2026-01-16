students=[("Abdullah", 88),("Sara",97),("Zara",74),("Aman",64)]
studentsSorted=sorted(students, key = lambda x: x[1], reverse=True)
print(f"Top 3 Students: {studentsSorted[:3]}")