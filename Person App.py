import tkinter as tk
from tkinter import messagebox

class PersonInputGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Person Information Input")

        # Initialize variables to store user information
        self.name_var = tk.StringVar()
        self.height_var = tk.DoubleVar()
        self.weight_var = tk.DoubleVar()
        self.handedness_var = tk.StringVar()
        self.pitch_types_var = tk.StringVar()

        # GUI components
        tk.Label(master, text="Enter Person Information:").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(master, text="Name:").grid(row=1, column=0, pady=5)
        tk.Entry(master, textvariable=self.name_var).grid(row=1, column=1, pady=5)

        tk.Label(master, text="Height (in inches):").grid(row=2, column=0, pady=5)
        tk.Entry(master, textvariable=self.height_var).grid(row=2, column=1, pady=5)

        tk.Label(master, text="Weight (in pounds):").grid(row=3, column=0, pady=5)
        tk.Entry(master, textvariable=self.weight_var).grid(row=3, column=1, pady=5)

        tk.Label(master, text="Handedness:").grid(row=4, column=0, pady=5)
        tk.Entry(master, textvariable=self.handedness_var).grid(row=4, column=1, pady=5)

        tk.Label(master, text="Pitch Types (comma-separated):").grid(row=5, column=0, pady=5)
        tk.Entry(master, textvariable=self.pitch_types_var).grid(row=5, column=1, pady=5)

        tk.Button(master, text="Submit", command=self.submit).grid(row=6, column=0, columnspan=2, pady=10)

    def submit(self):
        try:
            # Validate and retrieve user input
            name = self.name_var.get()
            height = self.height_var.get()
            weight = self.weight_var.get()
            handedness = self.handedness_var.get()
            pitch_types_input = self.pitch_types_var.get().split(',')

            # Validate numerical inputs
            if not (isinstance(height, (float, int)) and isinstance(weight, (float, int))):
                raise ValueError("Height and weight must be numeric.")

            # Create pitch types dictionary
            pitch_type = {}
            for pitch_type_input in pitch_types_input:
                pitch_type = pitch_type_input.strip()
                metric1 = float(input(f"Enter metric1 for {pitch_type}: "))
                metric2 = float(input(f"Enter metric2 for {pitch_type}: "))
                pitch_type[pitch_type] = (metric1, metric2)

            # Create a Person instance
            person = Person(name, height, weight, handedness, pitch_type)

            # Close the input window
            self.master.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))


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
            print(f"  {pitch_type}: {metrics[0]} metric1, {metrics[1]} metric2")


if __name__ == "__main__":
    # Create a Tkinter root window for the PersonInputGUI
    input_root = tk.Tk()
    input_app = PersonInputGUI(input_root)

    # Start the Tkinter event loop for the input window
    input_root.mainloop()

    # Access the created Person instance after the input window is closed
    if hasattr(input_app, 'person'):
        input_app.person.display_info()
