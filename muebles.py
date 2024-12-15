import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd

# Preload the DataFrame
variables = pd.DataFrame({
    'MUEBLE': ['A', 'B', 'C'],
    'X': [1, 3, 2],
    'Y': [2, 5, 1],
    'Z': [5, 4, 3],
    'COSTO': [3000, 3300, 1900]
})

# Function to solve the costs for X, Y, Z
def calculate_costs():
    try:
        # Extracting user input for X, Y, Z, and COSTO
        x1, y1, z1, costo1 = float(entry_x1.get()), float(entry_y1.get()), float(entry_z1.get()), float(entry_costo1.get())
        x2, y2, z2, costo2 = float(entry_x2.get()), float(entry_y2.get()), float(entry_z2.get()), float(entry_costo2.get())
        x3, y3, z3, costo3 = float(entry_x3.get()), float(entry_y3.get()), float(entry_z3.get()), float(entry_costo3.get())
        
        # Construct the A matrix (X, Y, Z values)
        A = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
        # Construct the b vector (COSTO values)
        b = np.array([[costo1], [costo2], [costo3]])
        
        # Solve the system to get the costs of X, Y, Z
        x = np.linalg.solve(A, b)
        costo_x, costo_y, costo_z = x[0][0], x[1][0], x[2][0]

        # Display calculated costs in the table below
        for widget in results_frame.winfo_children():
            widget.destroy()  # Clear previous results

        # Creating headers for the result table
        tk.Label(results_frame, text="Mueble", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=pad, pady=pad)
        tk.Label(results_frame, text="Costo X", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=pad, pady=pad)
        tk.Label(results_frame, text="Costo Y", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=pad, pady=pad)
        tk.Label(results_frame, text="Costo Z", font=("Helvetica", 12, "bold")).grid(row=0, column=3, padx=pad, pady=pad)

        # Populating the result table with the calculated costs
        tk.Label(results_frame, text="A", font=("Helvetica", 12)).grid(row=1, column=0, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_x:.2f}", font=("Helvetica", 12)).grid(row=1, column=1, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_y:.2f}", font=("Helvetica", 12)).grid(row=1, column=2, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_z:.2f}", font=("Helvetica", 12)).grid(row=1, column=3, padx=pad, pady=pad)

        tk.Label(results_frame, text="B", font=("Helvetica", 12)).grid(row=2, column=0, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_x:.2f}", font=("Helvetica", 12)).grid(row=2, column=1, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_y:.2f}", font=("Helvetica", 12)).grid(row=2, column=2, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_z:.2f}", font=("Helvetica", 12)).grid(row=2, column=3, padx=pad, pady=pad)

        tk.Label(results_frame, text="C", font=("Helvetica", 12)).grid(row=3, column=0, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_x:.2f}", font=("Helvetica", 12)).grid(row=3, column=1, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_y:.2f}", font=("Helvetica", 12)).grid(row=3, column=2, padx=pad, pady=pad)
        tk.Label(results_frame, text=f"{costo_z:.2f}", font=("Helvetica", 12)).grid(row=3, column=3, padx=pad, pady=pad)

        # Enable the next section for calculating the total cost
        submit_costs_button.config(state=tk.NORMAL)

        # Save costs globally
        global costo_x_val, costo_y_val, costo_z_val
        costo_x_val, costo_y_val, costo_z_val = costo_x, costo_y, costo_z

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos para todas las celdas.")

# Function to calculate the total cost based on quantities of A, B, and C
def calculate_total_cost():
    try:
        # Get the number of pieces to produce
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        
        # Calculate the total cost using the given formula
        total_cost = a * (costo_x_val + 2 * costo_y_val + 5 * costo_z_val) + \
                     b * (3 * costo_x_val + 5 * costo_y_val + 4 * costo_z_val) + \
                     c * (2 * costo_x_val + costo_y_val + 3 * costo_z_val)
        
        # Display total cost
        label_total_cost.config(text=f"El costo total de producir {a} muebles A, {b} muebles B y {c} muebles C es: {total_cost:.2f} pesos")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos para las cantidades.")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Calculadora de Costo de Producción de Muebles")

# Make the window resizable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

# Set padding
pad = 10

# Create labels for the table of values
tk.Label(root, text="Ingrese los valores para los muebles", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=6, sticky="nsew", padx=pad, pady=pad)

# Table headers
tk.Label(root, text="Mueble", font=("Helvetica", 14, "bold")).grid(row=1, column=0, sticky="nsew", padx=pad, pady=pad)
tk.Label(root, text="X", font=("Helvetica", 14, "bold")).grid(row=1, column=1, sticky="nsew", padx=pad, pady=pad)
tk.Label(root, text="Y", font=("Helvetica", 14, "bold")).grid(row=1, column=2, sticky="nsew", padx=pad, pady=pad)
tk.Label(root, text="Z", font=("Helvetica", 14, "bold")).grid(row=1, column=3, sticky="nsew", padx=pad, pady=pad)
tk.Label(root, text="Costo", font=("Helvetica", 14, "bold")).grid(row=1, column=4, sticky="nsew", padx=pad, pady=pad)

# Entries for the values of furniture A, B, and C (preload data from the dataframe)
tk.Label(root, text="A", font=("Helvetica", 12)).grid(row=2, column=0, sticky="nsew", padx=pad, pady=pad)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=2, column=1, sticky="nsew", padx=pad, pady=pad)
entry_x1.insert(0, variables.loc[0, 'X'])  # Preload data
entry_y1 = tk.Entry(root)
entry_y1.grid(row=2, column=2, sticky="nsew", padx=pad, pady=pad)
entry_y1.insert(0, variables.loc[0, 'Y'])  # Preload data
entry_z1 = tk.Entry(root)
entry_z1.grid(row=2, column=3, sticky="nsew", padx=pad, pady=pad)
entry_z1.insert(0, variables.loc[0, 'Z'])  # Preload data
entry_costo1 = tk.Entry(root)
entry_costo1.grid(row=2, column=4, sticky="nsew", padx=pad, pady=pad)
entry_costo1.insert(0, variables.loc[0, 'COSTO'])  # Preload data

tk.Label(root, text="B", font=("Helvetica", 12)).grid(row=3, column=0, sticky="nsew", padx=pad, pady=pad)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=3, column=1, sticky="nsew", padx=pad, pady=pad)
entry_x2.insert(0, variables.loc[1, 'X'])  # Preload data
entry_y2 = tk.Entry(root)
entry_y2.grid(row=3, column=2, sticky="nsew", padx=pad, pady=pad)
entry_y2.insert(0, variables.loc[1, 'Y'])  # Preload data
entry_z2 = tk.Entry(root)
entry_z2.grid(row=3, column=3, sticky="nsew", padx=pad, pady=pad)
entry_z2.insert(0, variables.loc[1, 'Z'])  # Preload data
entry_costo2 = tk.Entry(root)
entry_costo2.grid(row=3, column=4, sticky="nsew", padx=pad, pady=pad)
entry_costo2.insert(0, variables.loc[1, 'COSTO'])  # Preload data

tk.Label(root, text="C", font=("Helvetica", 12)).grid(row=4, column=0, sticky="nsew", padx=pad, pady=pad)
entry_x3 = tk.Entry(root)
entry_x3.grid(row=4, column=1, sticky="nsew", padx=pad, pady=pad)
entry_x3.insert(0, variables.loc[2, 'X'])  # Preload data
entry_y3 = tk.Entry(root)
entry_y3.grid(row=4, column=2, sticky="nsew", padx=pad, pady=pad)
entry_y3.insert(0, variables.loc[2, 'Y'])  # Preload data
entry_z3 = tk.Entry(root)
entry_z3.grid(row=4, column=3, sticky="nsew", padx=pad, pady=pad)
entry_z3.insert(0, variables.loc[2, 'Z'])  # Preload data
entry_costo3 = tk.Entry(root)
entry_costo3.grid(row=4, column=4, sticky="nsew", padx=pad, pady=pad)
entry_costo3.insert(0, variables.loc[2, 'COSTO'])  # Preload data

# Button to submit the values and calculate the costs of X, Y, Z
submit_button = tk.Button(root, text="Calcular Costos", command=calculate_costs, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
submit_button.grid(row=5, columnspan=5, sticky="nsew", padx=pad, pady=pad)

# Frame for displaying results in table format
results_frame = tk.Frame(root)
results_frame.grid(row=6, columnspan=5, sticky="nsew", padx=pad, pady=pad)

# Section for calculating total cost
tk.Label(root, text="Ingrese las cantidades de muebles a producir", font=("Helvetica", 16, "bold")).grid(row=7, columnspan=5, sticky="nsew", padx=pad, pady=pad)

tk.Label(root, text="Muebles A", font=("Helvetica", 12)).grid(row=8, column=0, sticky="nsew", padx=pad, pady=pad)
entry_a = tk.Entry(root)
entry_a.grid(row=8, column=1, sticky="nsew", padx=pad, pady=pad)

tk.Label(root, text="Muebles B", font=("Helvetica", 12)).grid(row=8, column=2, sticky="nsew", padx=pad, pady=pad)
entry_b = tk.Entry(root)
entry_b.grid(row=8, column=3, sticky="nsew", padx=pad, pady=pad)

tk.Label(root, text="Muebles C", font=("Helvetica", 12)).grid(row=8, column=4, sticky="nsew", padx=pad, pady=pad)
entry_c = tk.Entry(root)
entry_c.grid(row=8, column=5, sticky="nsew", padx=pad, pady=pad)

# Button to calculate total cost
submit_costs_button = tk.Button(root, text="Calcular Costo Total", command=calculate_total_cost, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), state=tk.DISABLED)
submit_costs_button.grid(row=9, columnspan=6, sticky="nsew", padx=pad, pady=pad)

# Label for displaying total cost result
label_total_cost = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
label_total_cost.grid(row=10, columnspan=6, sticky="nsew", padx=pad, pady=pad)

# Start the Tkinter event loop
root.mainloop()
