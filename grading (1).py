def calculate_grade(average_score):
    if 70 <= average_score <= 100:
        return 'A'
    elif 60 <= average_score <= 69:
        return 'B'
    elif 50 <= average_score <= 59:
        return 'C'
    elif 40 <= average_score <= 49:
        return 'D'
    else:
        return 'FAIL'

def main():
    marks = []
    for i in range(3):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100 inclusive. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    average_score = sum(marks) / len(marks)
    grade = calculate_grade(average_score)

    print(f"Average score: {average_score:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
