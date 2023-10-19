grades = []
while True:
    grade = input("Ingrese una calificación o salir para terminar").lower()
    if grade == "salir": break
    else: grades.append(float(grade))   
average = sum(grades)/len(grades)
print(f"El promedio es: {average}")