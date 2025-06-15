class Person:
    def __init__(self, name: str, color: str, height: float):
        self.name = name
        self.color = color
        self.height = height

    def to_json(self):
        return {
            "name": self.name,
            "color": self.color,
            "height": self.height
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)

# Storage for persons
list_of_persons = []

# 1. Add a person
def add_person(name: str, color: str, height: float):
    person = Person(name, color, height)
    list_of_persons.append(person)
    return person.to_json()

# 2. Get all persons
def list_persons():
    return [person.to_json() for person in list_of_persons]

# 3. Get a person by name
def get_person(name: str):
    for person in list_of_persons:
        if person.name == name:
            return person.to_json()
    return None

# 4. Update a person
def update_person(name: str, color: str = None, height: float = None):
    for person in list_of_persons:
        if person.name == name:
            if color:
                person.color = color
            if height is not None:
                person.height = height
            return person.to_json()
    return None

# 5. Remove a person
def remove_person(name: str):
    global list_of_persons
    for person in list_of_persons:
        if person.name == name:
            list_of_persons.remove(person)
            return person.to_json()
    return None

# === DEMO ===
print("Adding persons:")
print(add_person("manasa", "white", 5.5))
print(add_person("manu", "black", 5.8))


print(list_persons())


print(get_person("manu"))

print(update_person("manu", height=6.0))


print(list_persons())

print(remove_person("manasa"))
print(list_persons())









