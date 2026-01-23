def calculate_percentage(marks: list[float]) -> float:
    if not marks:
        raise ValueError("Marks list cannot be empty")
    
    for  mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 to 100")
        
    total = sum(marks)
    percentage= (total /(len(marks) * 100)) * 100
    return percentage

def determine_grade(percentage: float) -> str:
    if percentage < 0 or percentage > 100:
        raise ValueError("Invaild percentage value")
    
    if percentage >= 70:
        return "First Class"
    elif percentage >=60:
        return "Second Class"
    elif percentage >=50:
        return "Third Class"
    elif percentage >=40:
        return "Pass"
    else:
        return "Fail"