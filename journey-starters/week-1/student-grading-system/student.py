from grading import  calculate_percentage, determine_grade

class Student:
    def __init__(self, marks: list[float]):
        self.marks=marks
    
    def get_percentage(self) -> float:
        return calculate_percentage(self.marks)
    
    def get_grade(self)-> str:
        return determine_grade(self.get_percentage())