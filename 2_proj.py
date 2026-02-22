import numpy as np

students = {
    "Rahul": np.array([86.5]),
    "Aman": np.array([91.2]),
    "Priya": np.array([78.4]),
    "Sneha": np.array([88.9]),
    "Arjun": np.array([95.0]),
    "Karan": np.array([67.3]),
    "Meena": np.array([72.6]),
    "Riya": np.array([84.1])
}
#Its just an ideo how to use numpy in th epython you have learned
for name, percentage in students.items():
    print(name, ":", percentage[0], "%")

all_percentage = np.array(list(students.values()))
print("Average of the class is: ", np.mean(all_percentage),"%")

topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper], "%")