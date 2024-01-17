#Class to create an instance of an athlete
class Person:
    def __init__(self, name, height, weight, handedness, pitch_type):
        self.name = name
        self.height = height
        self.weight = weight
        self.handedness = handedness
        self.pitch_types = pitch_type

    def display_info(self):
        print(f"\nPerson Information for {self.name}:")
        print(f"Height: {self.height} inches")
        print(f"Weight: {self.weight} pounds")
        print(f"Handedness: {self.handedness}")
        print("Pitch Types:")
        for pitch_type, metrics in self.pitch_types.items():
            print(f"  {pitch_type}: Velocity: {metrics[0]}, Stuff: {metrics[1]}")


def create_person():
    # Get user input for person details
    name = input("Enter name: ")
    height = float(input(("Enter ") + name + ("'s height (in inches): ")))
    weight = float(input(("Enter ") + name + ("'s weight (in pounds): ")))
    handedness = input(("Enter ") + name + ("'s handedness (e.g., left-handed, right-handed): "))

    # Get user input for pitch types and metrics
    pitch_types = {}
    num_pitch_types = int(input(("Enter the number of pitch types ") + name + (" throws: ")))
    for _ in range(num_pitch_types):
        pitch_type = input("Enter pitch type: ")
        velocity = float(input((f"Enter velocity for ") + pitch_type + (": ")))
        stuff = float(input((f"Enter stuff for ") + pitch_type + (": ")))
        pitch_types[pitch_type] = (velocity, stuff)

    # Create an instance of the Person class
    person = Person(name, height, weight, handedness, pitch_type)

    return person


if __name__ == "__main__":
    # Create a person instance
    new_person = create_person()

    # Display person information
    new_person.display_info()


