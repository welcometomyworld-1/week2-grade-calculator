"""
Student Grade Calculator
Week 2 Project - Control Flow & Data Structures
Author: Sushant Kumar Gupta
"""

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent! Keep up the great work!"
    elif avg >= 80:
        return "B", "Very Good! You're doing well."
    elif avg >= 70:
        return "C", "Good. Room for improvement."
    elif avg >= 60:
        return "D", "Needs Improvement. Please study more."
    return "F", "Failed. Please seek help from teacher."

def get_valid_mark(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input!")

def save_results(results):
    with open("results.txt", "w") as f:
        for r in results:
            f.write(str(r) + "\n")
    print("Results saved to results.txt")

def main():
    results = []

    while True:
        print("\n1. Enter Students")
        print("2. Search Student")
        print("3. Save Results")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            while True:
                try:
                    n = int(input("Number of students: "))
                    if n > 0:
                        break
                except ValueError:
                    pass

            for i in range(n):
                print(f"\nStudent {i+1}")
                name = input("Name: ")
                m1 = get_valid_mark("Math: ")
                m2 = get_valid_mark("Science: ")
                m3 = get_valid_mark("English: ")

                avg = (m1 + m2 + m3) / 3
                grade, comment = calculate_grade(avg)

                results.append({
                    "name": name,
                    "average": round(avg, 2),
                    "grade": grade,
                    "comment": comment
                })

            print("\nRESULTS")
            for r in results:
                print(f"{r['name']} | {r['average']} | {r['grade']} | {r['comment']}")

            avgs = [x["average"] for x in results]
            print("\nClass Statistics")
            print("Class Average:", round(sum(avgs)/len(avgs), 2))
            print("Highest:", max(avgs))
            print("Lowest:", min(avgs))

        elif choice == "2":
            search = input("Student name: ").lower()
            found = False
            for r in results:
                if r["name"].lower() == search:
                    print(r)
                    found = True
            if not found:
                print("Student not found")

        elif choice == "3":
            save_results(results)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
