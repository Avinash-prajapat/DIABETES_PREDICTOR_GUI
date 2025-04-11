
# 🩺 Diabetes Prediction GUI Application

## 🎯 Aim
To develop a user-friendly desktop application using Machine Learning and GUI (Tkinter) to predict whether a person is diabetic based on various health parameters.

---

## 📝 Introduction
Diabetes is one of the most common chronic diseases affecting millions worldwide. Early detection can help in effective management. This project utilizes a Machine Learning model trained on the Pima Indians Diabetes Dataset to predict the likelihood of diabetes based on inputs like glucose level, BMI, age, etc. The application features an interactive graphical interface to make predictions easy for end-users.

---

## 💻 Technologies Used

| Category                     | Tools/Libraries                        |
|------------------------------|----------------------------------------|
| Programming Language         | Python                                 |
| ML Framework                 | Scikit-learn                           |
| GUI Toolkit                  | Tkinter                                |
| Data Analysis                | Pandas, NumPy                          |
| Visualization (for training) | Matplotlib, Seaborn (optional)         |
| IDE Used                     | Visual Studio Code                     |

---

## 🧠 Machine Learning Model

- **Algorithm**: Logistic Regression
- **Dataset**: Pima Indians Diabetes Dataset (`diabetes.csv`)
- **Trained Model File**: `diabetes_model.pkl`
- **Accuracy**: ~77% (can vary depending on preprocessing)

---

## 🧩 Design and Implementation

1. **Data Preprocessing**: Handled missing values and normalized data.
2. **Model Training**: Logistic Regression used to build a classifier.
3. **GUI Design**:
   - Built using Tkinter with modern design.
   - User inputs 8 medical parameters.
   - On clicking **Predict**, it displays result using popup.
4. **Prediction Popup**:
   - ✅ Green = Not Diabetic
   - ⚠️ Red = Diabetic
   - 🟠 Orange = Error in input

---

## 🖼️ Application Screenshot

Here is a preview of the GUI: (output)

[GUI Screenshot Of Deabetic](images./Prediction_Diabetic.png)
[GUI Screenshot of Not Deabetic](images./Prediction_Not_Diabetic.png)

---

## 🗂️ Project Structure

```
DIABETES_PREDICTOR_GUI/
├── diabetes_model.pkl           # Trained ML model
├── diabetes.csv                 # Dataset
├── gui_diabetes_predictor.py    # GUI Application
├── train_model.ipynb            # Jupyter notebook for training
├── requirements.txt             # Project dependencies
├── image.png                    # GUI Screenshot
└── README.md                    # This documentation
```

---

## ✅ How to Run

1. Clone or download the project.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the GUI:
   ```bash
   python gui_diabetes_predictor.py
   ```

---

## ✅ Conclusion

This project showcases how Machine Learning models can be integrated with GUI interfaces to provide easy-to-use healthcare tools. It is beginner-friendly and can be extended further to include other algorithms, better designs, or even web-based deployment.

---

## 🙌 Contributions & Credits

- Created by: **Avinash Kumar**
- Dataset source: [Kaggle - Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

