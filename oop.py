class student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name}  from {student.house}")



def get_student():
    name = input("name:")
    house = input("house:")
    return student(name, house)


if __name__ == "__main__":
    main()