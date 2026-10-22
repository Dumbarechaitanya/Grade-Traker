from grades import average, letter_grade, highest

def main():
    scores = [90, 85, 72, 60]
    avg = average(scores)
    print(f"Scores:  {scores}")
    print(f"Average: {avg:.2f} ({letter_grade(avg)})")
    print(f"Highest: {highest(scores)}")

if __name__ == "__main__":
    main()
