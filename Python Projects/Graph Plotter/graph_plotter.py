import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
import math  # Import math module for standard math functions

"""
- Only plots t ox
"""

class GraphPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Graph Plotter")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Frame for plot settings
        settings_frame = ttk.Frame(self.root)
        settings_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Label and Entry for function input
        ttk.Label(settings_frame, text="Enter function (e.g., sin(x), x**2):").grid(row=0, column=0, padx=5, pady=5)
        self.function_entry = ttk.Entry(settings_frame, width=50)
        self.function_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for x range
        ttk.Label(settings_frame, text="Enter x range (start, end):").grid(row=1, column=0, padx=5, pady=5)
        self.x_range_entry = ttk.Entry(settings_frame, width=25)
        self.x_range_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to plot graph
        plot_button = ttk.Button(settings_frame, text="Plot Graph", command=self.plot_graph)
        plot_button.grid(row=2, columnspan=2, padx=5, pady=10)

        # Canvas for plot
        self.plot_canvas = tk.Canvas(self.root, bg='white', width=500, height=300)
        self.plot_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_function_dict(self):
        # Create a dictionary with common math functions and their corresponding Python functions
        return {
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
            'abs': np.abs,
            'pow': np.power,
            'max': np.maximum,
            'min': np.minimum,
            'floor': np.floor,
            'ceil': np.ceil
        }

    def plot_graph(self):
        function = self.function_entry.get()
        x_range = self.x_range_entry.get()

        try:
            # Parse x range
            start, end = map(float, x_range.split(','))

            # Generate x values
            x = np.linspace(start, end, 500)

            # Create dictionary of math functions
            math_functions = self.create_function_dict()

            # Replace math function names with corresponding numpy functions
            for key in math_functions.keys():
                function = function.replace(key, f"math_functions[key]")

            # Evaluate function
            y = eval(function)

            # Clear previous plot
            self.plot_canvas.delete("all")

            # Plot using matplotlib
            plt.figure(figsize=(5, 3))
            plt.plot(x, y)
            plt.title("Graph Plot")
            xlabel, ylabel = "x", "y"

            # Convert plot to tkinter canvas compatible format
            plot_img = self._plot_to_tk_image()

            # Display plot on canvas
            self.plot_canvas.create_image(0, 0, anchor=tk.NW, image=plot_img)
            self.plot_canvas.image = plot_img  # Keep reference

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _plot_to_tk_image(self):
        # Save plot to a temporary file
        tmp_file = "tmp_plot.png"
        plt.savefig(tmp_file, bbox_inches='tight')

        # Load image as tkinter PhotoImage
        plot_img = tk.PhotoImage(file=tmp_file)

        # Remove temporary file
        os.remove(tmp_file)

        return plot_img

def main():
    root = tk.Tk()
    app = GraphPlotter(root)
    root.mainloop()

if __name__ == '__main__':
    main()
