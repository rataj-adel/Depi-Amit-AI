import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class SalaryApp:
    def __init__(self, root):  
        """
        Initialize the SalaryApp GUI, set up window, buttons, labels, 
        and prepare the matplotlib canvas for plotting.
        """
        self.root = root
        self.root.title("Simple Salary Prediction")
        self.root.geometry("800x600")

        self.data = None
        self.model = None

        self.load_btn = tk.Button(root, text="Load Salary_Data.csv", command=self.load_data, bg="#2980b9", fg="white", font=("Arial", 12))
        self.load_btn.pack(pady=10)

        self.train_btn = tk.Button(root, text="Train Linear Regression", command=self.train_model, bg="#27ae60", fg="white", font=("Arial", 12))
        self.train_btn.pack(pady=10)
        self.train_btn.config(state=tk.DISABLED)

        self.metrics_label = tk.Label(root, text="", font=("Arial", 12))
        self.metrics_label.pack(pady=10)

        self.figure = Figure(figsize=(7,4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

    def load_data(self):
        """
        Load the Salary_Data.csv file, validate required columns, 
        enable training button, and plot the initial data.
        """
        try:
            self.data = pd.read_csv('Salary_Data.csv')
            if 'YearsExperience' not in self.data.columns or 'Salary' not in self.data.columns:
                raise ValueError("CSV must have 'YearsExperience' and 'Salary' columns.")
            self.metrics_label.config(text=f"Loaded {len(self.data)} records.")
            self.train_btn.config(state=tk.NORMAL)
            self.plot_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.train_btn.config(state=tk.DISABLED)

    def plot_data(self):
        """
        Plot the scatter plot of Years of Experience vs Salary 
        before training the regression model.
        """
        self.ax.clear()
        self.ax.scatter(self.data['YearsExperience'], self.data['Salary'], color='blue')
        self.ax.set_title("Salary vs Years of Experience")
        self.ax.set_xlabel("Years of Experience")
        self.ax.set_ylabel("Salary")
        self.canvas.draw()

    def train_model(self):
        """
        Train a linear regression model using the loaded data, 
        calculate metrics (MSE, RMSE, R²), and plot the regression line 
        along with training and test datasets.
        """
        X = self.data[['YearsExperience']].values
        y = self.data['Salary'].values

        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        self.model = LinearRegression()
        self.model.fit(x_train, y_train)

        y_pred = self.model.predict(x_test)

        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        self.metrics_label.config(text=f"MSE: {mse:.2f} | RMSE: {rmse:.2f} | R²: {r2:.4f}")

        self.ax.clear()
        self.ax.scatter(x_train, y_train, color='red', label='Training data')
        self.ax.scatter(x_test, y_test, color='green', label='Test data')

        x_range = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
        y_range_pred = self.model.predict(x_range)
        self.ax.plot(x_range, y_range_pred, color='blue', label='Regression line')

        self.ax.set_title("Salary vs Years of Experience")
        self.ax.set_xlabel("Years of Experience")
        self.ax.set_ylabel("Salary")
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":   
    """
    Entry point of the program. Creates the main Tkinter window 
    and launches the SalaryApp.
    """
    root = tk.Tk()
    app = SalaryApp(root)
    root.mainloop()
