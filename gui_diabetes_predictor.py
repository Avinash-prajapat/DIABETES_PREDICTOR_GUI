import tkinter as tk
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("diabetes_model.pkl", "rb"))

# Function to show stylish custom popup
def show_custom_popup(message, color):
    popup = tk.Toplevel(root)
    popup.title("Prediction Result")
    popup.geometry("300x150")
    popup.configure(bg="white")
    popup.resizable(False, False)

    # Center the popup
    popup.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - 150
    y = root.winfo_y() + (root.winfo_height() // 2) - 75
    popup.geometry(f"+{x}+{y}")

    tk.Label(popup, text="Prediction Result", font=("Helvetica", 14, "bold"), bg="white", fg="#333").pack(pady=(15, 5))
    tk.Label(popup, text=message, font=("Helvetica", 12), bg="white", fg=color).pack(pady=(0, 10))

    tk.Button(popup, text="Close", command=popup.destroy, font=("Helvetica", 10), bg="#007bff", fg="white", padx=10, pady=5).pack()

# Predict function
def predict():
    try:
        values = [float(entry.get()) for entry in entries]
        result = model.predict([values])
        if result[0] == 1:
            show_custom_popup("⚠️ Diabetic", "#dc3545")  # Red
        else:
            show_custom_popup("✅ Not Diabetic", "#28a745")  # Green
    except:
        show_custom_popup("Please enter all values correctly!", "#ff8800")  # Orange

# App Window
root = tk.Tk()
root.title("🩺 Diabetes Prediction System")
root.geometry("500x550")
root.configure(bg="#f0f4f7")

# Title
tk.Label(root, text="Diabetes Predictor", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=20)

# Frame for Inputs
form_frame = tk.LabelFrame(root, text="Enter Patient Details", font=("Helvetica", 12, "bold"), bg="#ffffff", padx=20, pady=20, fg="#333")
form_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Labels and Entries
labels = [
    "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness",
    "Insulin", "BMI", "Diabetes Pedigree Function", "Age"
]
entries = []

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label + ":", font=("Helvetica", 10), bg="#ffffff", anchor="w").grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, font=("Helvetica", 10), width=25)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

# Predict Button
tk.Button(root, text="🔍 Predict", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", width=20, command=predict).pack(pady=20)

root.mainloop()
