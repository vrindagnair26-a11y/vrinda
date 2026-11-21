import csv

# Creating a dictionary
student = {
    "Roll No": [1, 2, 3, 4],
    "Name": ["Arun", "Anu", "Rahul", "Meera"],
    "Marks": [85, 90, 78, 95]
}

# Writing dictionary data into a CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Writing column headings
    writer.writerow(student.keys())

    # Writing dictionary values
    writer.writerows(zip(*student.values()))

print("Dictionary successfully written to CSV file.")

# Reading and displaying the CSV file
with open("student.csv", "r") as file:
    reader = csv.reader(file)

    print("\nContents of CSV File:")
    for row in reader:
        print(row)