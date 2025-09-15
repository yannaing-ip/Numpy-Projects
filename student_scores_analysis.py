import numpy as np

student_scores = np.array([
    [85, 78, 92, 88, 91],
    [76, 84, 69, 80, 77],
    [90, 92, 95, 89, 94],
    [65, 70, 72, 68, 66],
    [88, 85, 90, 87, 89],
    [79, 82, 78, 81, 80],
    [91, 94, 90, 93, 95],
    [55, 60, 58, 57, 59],
    [83, 85, 82, 80, 84],
    [72, 74, 70, 71, 73],
    [88, 90, 85, 87, 86],
    [79, 81, 77, 78, 80],
    [92, 95, 91, 94, 93],
    [67, 69, 65, 66, 68],
    [84, 86, 82, 83, 85],
    [73, 75, 70, 72, 74],
    [89, 91, 87, 88, 90],
    [78, 80, 76, 77, 79],
    [93, 96, 92, 94, 95],
    [66, 68, 63, 65, 67],
    [81, 83, 79, 80, 82],
    [74, 76, 71, 73, 75],
    [87, 89, 85, 86, 88],
    [77, 79, 75, 76, 78],
    [90, 93, 89, 91, 92],
    [68, 70, 65, 67, 69],
    [82, 85, 80, 83, 81],
    [75, 78, 72, 74, 76],
    [88, 90, 86, 87, 89],
    [79, 82, 77, 80, 81],
    [91, 94, 90, 92, 93],
    [65, 68, 63, 66, 64],
    [84, 86, 81, 83, 85],
    [73, 75, 70, 72, 74],
    [89, 91, 87, 88, 90],
    [78, 80, 76, 77, 79],
    [92, 95, 91, 93, 94],
    [67, 69, 64, 66, 68],
    [81, 83, 78, 80, 82],
    [74, 76, 71, 73, 75],
    [87, 89, 85, 86, 88],
    [77, 79, 75, 76, 78],
    [90, 93, 89, 91, 92],
    [66, 68, 63, 65, 67],
    [83, 85, 80, 82, 84],
    [72, 74, 69, 71, 73],
    [88, 90, 86, 87, 89],
    [79, 81, 76, 78, 80],
    [91, 94, 90, 92, 93],
    [65, 67, 62, 64, 66],
    [85, 87, 82, 84, 86],
    [73, 75, 70, 72, 74],
    [89, 91, 87, 88, 90],
    [78, 80, 75, 77, 79],
    [92, 95, 91, 93, 94],
    [66, 68, 63, 65, 67],
    [82, 85, 80, 82, 81],
    [75, 77, 72, 74, 76],
    [88, 90, 86, 87, 89],
    [79, 81, 76, 78, 80],
    [91, 94, 90, 92, 93],
    [65, 67, 62, 64, 66],
    [84, 86, 81, 83, 85]
])

print("Student Scores Array (62x5):\n", student_scores)

print("Mean per student\n", np.mean(student_scores, axis = 1))

print("Mean per Subject\n", np.mean(student_scores, axis = 0))

print("Median per student\n", np.median(student_scores, axis = 1))

print("Median per Subject\n", np.median(student_scores, axis = 0))

print("Standard deviation per student\n", np.std(student_scores, axis=1))

print("Standard deviation per Subject\n", np.std(student_scores, axis=0))

print("Maximum score per student\n", np.max(student_scores, axis=1))

print("Minimun score per student\n", np.min(student_scores, axis=1))

print("Maximum score per Subject\n", np.max(student_scores, axis=0))

print("Minimun score per Subject\n", np.min(student_scores, axis=0))

def top_students(scores, n = 10):
    student_average_score = np.average(scores, axis=1)
    idx = np.argsort(student_average_score)[::-1]

    top_idx = idx[:n]

    top_students = student_average_score[top_idx]

    for rank, (i, score) in enumerate(zip(top_idx, top_students)):
        print(f"Rank {rank+1} : Student {i+1}, Avg Score => {score}")

def bottom_students(scores, n = 10):
    student_average_score = np.average(scores, axis=1)
    idx = np.argsort(student_average_score)

    bottom_idx = idx[:n]

    bottom_students = student_average_score[bottom_idx]
    for rank, (i, score) in enumerate(zip(bottom_idx, bottom_students)):
        print(f"Rank {rank+1} : Student {i+1}, Avg score => {score}")

print("Top 10 Students")
top_students(student_scores)
print("Bottom 10 Students")
bottom_students(student_scores)

    









