class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0
        self.class_name = "Students in MLOps"

    def enrollStudents(self, count):
        """Enrolls the specified number of students into the class."""
        self.total_students += count

    def dropStudents(self, count):
        """Drops the specified number of students from the class."""
        self.total_students -= count
        # Ensure total_students does not go negative
        if self.total_students < 0:
            self.total_students = 0

    def getTotalStrength(self):
        """Returns the total number of students currently enrolled in the class."""
        return self.total_students

    def getClassName(self):
        """Returns the name of the class."""
        return self.class_name

# Example usage:
if __name__ == "__main__":
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)
    class_instance.dropStudents(2)
    print(f"Total Strength: {class_instance.getTotalStrength()}")
    print(f"Class Name: {class_instance.getClassName()}")
