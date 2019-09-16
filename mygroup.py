groupmates = [
	{
		"name" : "Александр",
		"surname" : "Иванов",
		"exams" : ["Информатика", "ЭЭиС", "Web"],
		"marks" : [4, 3, 5]
	},
	{
		"name" : "Владислав",
		"surname" : "Рубанов",
		"exams" : ["История", "ОС", "Web"],
		"marks" : [4, 5, 4]
	},
    {
		"name" : "Артур",
		"surname" : "Кишанов",
		"exams" : ["Философия", "Web", "АиГ"],
		"marks" : [5, 3, 3]
	},
    {
		"name" : "Яна",
		"surname" : "Мухова",
		"exams" : ["КТП", "ОЭиЭЭ", "БЖ"],
		"marks" : [4, 4, 5]
	},
    {
		"name" : "Дмитрий",
		"surname" : "Косин",
		"exams" : ["АИС", "ПИС", "ТП"],
		"marks" : [3, 5, 5]
	}
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)




