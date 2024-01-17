import tkinter as tk
from tkinter import messagebox

class BaseballApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pitch Sequencer")

        # Create a Person instance using the PersonInputGUI
        self.person = self.create_person()

        # Create a 5x5 matrix
        self.matrix_size = 5
        self.matrix = Matrix(self.matrix_size, self.matrix_size)
        self.matrix.populate_matrix()

        # GUI components
        self.label_pitch_type = tk.Label(master, text="Enter Pitch Type:")
        self.entry_pitch_type = tk.Entry(master)

        self.label_location = tk.Label(master, text="Enter Location (1 to 25):")
        self.entry_location = tk.Entry(master)

        self.button_submit = tk.Button(master, text="Submit", command=self.submit_pitch)

        self.button_reset_count = tk.Button(master, text="Reset Count", command=self.reset_count)

        self.label_suggestion = tk.Label(master, text="Suggested Next Pitch Type:")

        self.label_count = tk.Label(master, text=f"Count: 0-0")


        # Create buttons for each matrix position
        self.buttons_matrix = []
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                position = self.matrix.matrix[i][j]
                button = tk.Button(master, text=str(position), command=lambda p=position: self.set_location(p))
                button.grid(row=i + 6, column=j, padx=5, pady=5)
                self.buttons_matrix.append(button)

    def create_person(self):
        # Create a Tkinter root window for the PersonInputGUI
        input_root = tk.Tk()
        input_app = PersonInputGUI(input_root)

        # Start the Tkinter event loop for the input window
        input_root.mainloop()

        # Access the created Person instance after the input window is closed
        return getattr(input_app, 'person', None)

    def set_location(self, position):
        self.entry_location.delete(0, tk.END)
        self.entry_location.insert(0, str(position))

    def submit_pitch(self):
        pitch_type = self.entry_pitch_type.get()
        location = int(self.entry_location.get())

        if pitch_type not in self.person.pitch_types:
            messagebox.showerror("Error", "Invalid pitch type. Please enter a valid pitch type.")
            return

        if not (1 <= location <= 25):
            messagebox.showerror("Error", "Invalid location. Please enter a location between 1 and 25.")
            return

        metrics = self.person.pitch_types[pitch_type]
        suggestion = self.get_suggested_pitch(metrics)
        self.show_suggestion(suggestion)

        # Update pitch count 
        self.update_count(self)

    def get_suggested_pitch(self, metrics):
        # Example: You can implement your logic to suggest the next pitch type based on metrics.
        # Here, we simply return the pitch type with the highest metric1.
        return max(self.person.pitch_types, key=lambda pitch_type: metrics[0])

    def show_suggestion(self, suggestion):
        self.label_suggestion.config(text=f"Suggested Next Pitch Type: {suggestion}")

    def update_count(self, pitch_type):
        # Example: You can implement your logic to update the pitch count (balls and strikes).
        # Here, we increment the strikes counter each time a pitch is submitted.
        current_strikes = int(self.label_count.cget('text').split(' - ')[1])
        current_balls = int(self.label_count.cget('text').split(' - ')[0])

        if int(self.entry_location.get()) != 1 or 2 or 3 or 4 or 5 or 6 or 10 or 11 or 15 or 16 or 20 or 21 or 25:
            new_strikes = current_strikes + 1
        else:
            new_balls = current_balls + 1

        if new_strikes == 3:
            # Reset counter
            new_strikes = 0
            new_balls = 0

            # Perform actions for a strikeout (e.g., reset counters)
            messagebox.showinfo("Strikeout!", "Batter struck out!")
            self.label_count.config(text=f"Count: {new_balls}-{new_strikes}")

        elif new_balls == 4:
            # Reset counter
            new_balls = 0
            new_strikes = 0

            # Perform actions for a walk (e.g., reset counters)
            messagebox.showinfo("Walk!", "Batter walked!")
            self.label_count.config(text=f"Count: {new_balls}-{new_strikes}")

        else:
            self.label_count.config(text=f"Count: {current_balls}-{current_strikes}")

    def reset_count(self):
        # Reset the balls and strikes counter
        self.label_count.config(text="Count: 0-0")

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def populate_matrix(self):
        count = 1
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = count
                count += 1

class Person:
    def __init__(self, name, height, weight, handedness, pitch_type):
        self.name = name
        self.height = height
        self.weight = weight
        self.handedness = handedness
        self.pitch_type = pitch_type

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
            for pitch_types_input in pitch_types_input:
                
                # Open a new window for entering metrics
                metrics_window = tk.Toplevel(self.master)
                metrics_window.title(f"Metrics for " + pitch_type)

                # Initialize variables to store metrics
                metric1_var = tk.DoubleVar()
                metric2_var = tk.DoubleVar()
                metric3_var = tk.DoubleVar()

                # GUI components for metric input
                tk.Label(metrics_window, text=f"Enter metrics for {pitch_type}:").grid(row=0, column=0, columnspan=2, pady=5)

                tk.Label(metrics_window, text="Horizontal Break:").grid(row=1, column=0, pady=5)
                tk.Entry(metrics_window, textvariable=metric1_var).grid(row=1, column=1, pady=5)

                tk.Label(metrics_window, text="Vertical Break:").grid(row=2, column=0, pady=5)
                tk.Entry(metrics_window, textvariable=metric2_var).grid(row=2, column=1, pady=5)

                tk.Label(metrics_window, text="Velocity:").grid(row=1, column=0, pady=5)
                tk.Entry(metrics_window, textvariable=metric3_var).grid(row=1, column=1, pady=5)

                tk.Button(metrics_window, text="Submit", command=lambda pt=pitch_type, m1=metric1_var, m2=metric2_var, m3=metric3_var, w=metrics_window: self.submit_metrics(pt, m1, m2, w)).grid(row=3, column=0, columnspan=2, pady=10)


            # Create a Person instance
            self.person = Person(name, height, weight, handedness, pitch_type)

            # Close the input window
            self.master.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def submit_metrics(self, pitch_type, metric1_var, metric2_var, metric3_var, window):
        try:
            # Validate numerical inputs
            metric1 = metric1_var.get()
            metric2 = metric2_var.get()
            metric3 = metric3_var.get()

            if not isinstance(metric1, (float, int)) or not isinstance(metric2, (float, int)) or not isinstance(metric3, (float, int)):
                raise ValueError("Metrics must be numeric.")

            # Add the metrics to the pitch type dictionary
            self.person.pitch_type[pitch_type] = (metric1, metric2, metric3)

            # Close the metrics input window
            window.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))            


if __name__ == "__main__":
    root = tk.Tk()
    app = BaseballApp(root)
    root.mainloop()
