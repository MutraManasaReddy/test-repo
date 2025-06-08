class Person:
    def __init__(self, name, dob, gender):
        self.details = {
            "name": "name",
            "dob": "dob",
            "gender": "gender"
        }

    def add(self, key, value):
        if key in self.details:
            print(f"{key} change the value")
        else:
            self.details[key] = value
            print(f"{key} add successfully")

    def update(self, key, value):
        if key in self.details:
            self.details[key] = value
            print(f"{key} updated successfully")
        else:
            print(f"{key} add to insert new data")

    def remove(self, key):
        if key in self.details:
            del self.details[key]
            print(f"{key} removed successfully")
        else:
            print(f"{key} not found")

    def get_all(self):
        return self.details

    def list_all(self):
        for key, value in self.details.items():
            print(f"{key}: {value}")


p = Person("Manasa", "1999-05-14", "Female")


p.add("colour", "white")


p.update("name", "Manasa M")


p.remove("dob")


print(p.get_all())


p.list_all()




