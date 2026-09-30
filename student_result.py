def calculate_result(mark):
    """Return the result based on a student's mark."""
    if mark >= 40:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    mark = 65
    print("Student Mark:", mark)
    print("Result:", calculate_result(mark))
