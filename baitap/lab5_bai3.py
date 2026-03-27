grade_book = [
    ["An", 8.0, 7.5, 9.0],
    ["Binh", 9.5, 9.0, 9.5],
    ["Cuong", 5.0, 6.0, 7.0]
]
highest_avg = -1
best_student_name = ""

print("--- Điểm trung bình của từng sinh viên ---")

for student_data in grade_book:   
    name = student_data[0]       
    scores = student_data[1:]   
    avg_score = sum(scores) / len(scores)   
    print(f"Sinh viên: {name:8} | Điểm TB: {avg_score:.2f}")
    
    if avg_score > highest_avg:
        highest_avg = avg_score
        best_student_name = name

print("-" * 40)
print(f"Sinh viên có điểm trung bình cao nhất là: {best_student_name} ({highest_avg:.2f})")