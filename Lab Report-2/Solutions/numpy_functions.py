import numpy as np
def highest_average_student(scores):
    average_scores = np.mean(scores, axis=1)
    highest_average_index = np.argmax(average_scores)
    highest_average_score = average_scores[highest_average_index]
    print()
    print(f"The student with the highest average score is Student {highest_average_index + 1} with an average score of {highest_average_score:.2f}")
    print()
if __name__ == "__main__":
    student_scores = np.array([[85, 90, 78],
                                [92, 88, 95],
                                [70, 75, 80],
                                [88, 92, 85]])
    highest_average_student(student_scores)