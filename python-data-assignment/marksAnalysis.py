marks=[40,56,78,90,87,67,45,34,23,89]

print("Marks of students: ", marks)
print("First 3 marks: ", marks[:3])
print("Last 3 marks: ", marks[-3:])

maxMark=max(marks)
minMark=min(marks)
avg=sum(marks)/len(marks)
print("Highest: ", maxMark)
print("Lowest: ", minMark)
print("Average: ", avg)