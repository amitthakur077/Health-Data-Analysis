import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ----------------------------------------
# APP TITLE
# ----------------------------------------
st.set_page_config(page_title="Health Data Analysis Dashboard", layout="wide")

st.title("🏥 Health Data Analysis Dashboard")
st.markdown("""
Analyze and visualize patient health records using **NumPy**, **Pandas**, and **Matplotlib**.  
You can view individual patient data and explore trends across the dataset.
""")

# ----------------------------------------
# FILE UPLOAD SECTION
# ----------------------------------------
uploaded_file = st.file_uploader("📂 Upload your health data CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    
     # ✅ Validation for required columns
    required_columns = ["Patient_ID", "Age", "Gender", "Blood_Pressure", "Cholesterol", "Heart_Rate", "BMI"]
    if not all(col in df.columns for col in required_columns):
        st.error("❌ Invalid file format! Please upload a CSV file containing these columns exactly:\n"
                 "`Patient_ID`, `Age`, `Gender`, `Blood_Pressure`, `Cholesterol`, `Heart_Rate`, `BMI`")
        st.stop()
    
    
    
    df.dropna(inplace=True)
    df["BMI"] = df["BMI"].astype(float)

    st.success("✅ File uploaded successfully!")

    # ----------------------------------------
    # PATIENT SELECTION
    # ----------------------------------------
    patient_ids = df["Patient_ID"].unique()
    selected_id = st.selectbox("🔎 Select a Patient ID", patient_ids)

    patient_data = df[df["Patient_ID"] == selected_id].iloc[0]

    st.subheader(f"👤 Patient Details — ID: {selected_id}")

    # ----------------------------------------
    # PATIENT CARD LAYOUT
    # ----------------------------------------
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", f"{patient_data['Age']} years")
    col2.metric("Gender", f"{patient_data['Gender']}")
    col3.metric("BMI", f"{patient_data['BMI']}")

    col4, col5, col6 = st.columns(3)
    col4.metric("Blood Pressure", f"{patient_data['Blood_Pressure']} mmHg")
    col5.metric("Cholesterol", f"{patient_data['Cholesterol']} mg/dL")
    col6.metric("Heart Rate", f"{patient_data['Heart_Rate']} bpm")

    st.divider()

    # ----------------------------------------
    # DATASET-WIDE VISUALIZATIONS
    # ----------------------------------------
    st.subheader("📊 Data Visualizations")

    col1, col2, col3 = st.columns(3)

    # Histogram — Age Distribution
    with col1:
        fig1, ax1 = plt.subplots()
        ax1.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
        ax1.set_title("Age Distribution")
        ax1.set_xlabel("Age")
        ax1.set_ylabel("Number of Patients")
        st.pyplot(fig1)

    # Bar Chart — Gender Distribution
    with col2:
        fig2, ax2 = plt.subplots()
        df["Gender"].value_counts().plot(kind="bar", color=["lightcoral", "lightgreen"], ax=ax2)
        ax2.set_title("Gender Distribution")
        ax2.set_xlabel("Gender")
        ax2.set_ylabel("Count")
        st.pyplot(fig2)

    # Scatter Plot — Age vs Blood Pressure (Colored by Cholesterol)
    with col3:
        fig3, ax3 = plt.subplots()
        scatter = ax3.scatter(df["Age"], df["Blood_Pressure"],
                              c=df["Cholesterol"], cmap="viridis", s=80)
        ax3.set_title("Age vs Blood Pressure (Color = Cholesterol)")
        ax3.set_xlabel("Age")
        ax3.set_ylabel("Blood Pressure")
        cbar = plt.colorbar(scatter)
        cbar.set_label("Cholesterol Level")
        st.pyplot(fig3)

    # ----------------------------------------
    # NUMPY ANALYSIS SECTION
    # ----------------------------------------
    st.divider()
    st.subheader("📈 NumPy Data Insights")

    avg_bp = np.mean(df["Blood_Pressure"])
    avg_chol = np.mean(df["Cholesterol"])
    avg_bmi = np.mean(df["BMI"])

    st.write(f"**Average Blood Pressure:** {avg_bp:.2f} mmHg")
    st.write(f"**Average Cholesterol Level:** {avg_chol:.2f} mg/dL")
    st.write(f"**Average BMI:** {avg_bmi:.2f}")

else:
    st.info("⬆ Please upload your `health_data.csv` file to begin analysis.")













































































































































































































































































































































































































# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# # ----------------------------------------
# # MAIN APP WINDOW
# # ----------------------------------------
# root = tk.Tk()
# root.title("🏥 Health Data Analysis Dashboard")
# root.geometry("1200x700")
# root.configure(bg="#f0f4f7")

# # ----------------------------------------
# # GLOBAL VARIABLE
# # ----------------------------------------
# df = None

# # ----------------------------------------
# # FUNCTIONS
# # ----------------------------------------
# def load_csv():
#     global df
#     file_path = filedialog.askopenfilename(
#         title="Select Health Data CSV File",
#         filetypes=[("CSV Files", "*.csv")]
#     )
#     if file_path:
#         try:
#             df = pd.read_csv(file_path)
#             df.dropna(inplace=True)
#             df["BMI"] = df["BMI"].astype(float)
#             messagebox.showinfo("Success", "CSV loaded successfully!")

#             patient_ids = df["Patient_ID"].unique()
#             patient_menu["values"] = patient_ids
#             patient_menu.current(0)
#             show_patient_data()
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to load file: {e}")

# def show_patient_data(*args):
#     if df is None:
#         return
#     selected_id = patient_var.get()
#     patient_data = df[df["Patient_ID"] == selected_id].iloc[0]

#     # Update labels
#     age_label.config(text=f"Age: {patient_data['Age']} years")
#     gender_label.config(text=f"Gender: {patient_data['Gender']}")
#     bmi_label.config(text=f"BMI: {patient_data['BMI']}")

#     bp_label.config(text=f"Blood Pressure: {patient_data['Blood_Pressure']} mmHg")
#     chol_label.config(text=f"Cholesterol: {patient_data['Cholesterol']} mg/dL")
#     hr_label.config(text=f"Heart Rate: {patient_data['Heart_Rate']} bpm")

# def plot_charts():
#     if df is None:
#         messagebox.showwarning("Warning", "Please upload a CSV file first.")
#         return

#     # --- Chart 1: Histogram (Age Distribution)
#     fig, axs = plt.subplots(1, 3, figsize=(12, 4))

#     axs[0].hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
#     axs[0].set_title("Age Distribution")
#     axs[0].set_xlabel("Age")
#     axs[0].set_ylabel("Number of Patients")

#     # --- Chart 2: Bar chart (Gender Distribution)
#     df["Gender"].value_counts().plot(kind="bar", color=["lightcoral", "lightgreen"], ax=axs[1])
#     axs[1].set_title("Gender Distribution")
#     axs[1].set_xlabel("Gender")
#     axs[1].set_ylabel("Count")

#     # --- Chart 3: Scatter Plot (Age vs Blood Pressure)
#     scatter = axs[2].scatter(df["Age"], df["Blood_Pressure"], c=df["Cholesterol"], cmap="viridis", s=80)
#     axs[2].set_title("Age vs Blood Pressure (Color = Cholesterol)")
#     axs[2].set_xlabel("Age")
#     axs[2].set_ylabel("Blood Pressure")

#     plt.colorbar(scatter, ax=axs[2], label="Cholesterol Level")

#     # Embed chart in Tkinter
#     for widget in chart_frame.winfo_children():
#         widget.destroy()

#     canvas = FigureCanvasTkAgg(fig, master=chart_frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill="both", expand=True)

# def show_insights():
#     if df is None:
#         return
#     avg_bp = np.mean(df["Blood_Pressure"])
#     avg_chol = np.mean(df["Cholesterol"])
#     avg_bmi = np.mean(df["BMI"])

#     insights_label.config(
#         text=f"Average Blood Pressure: {avg_bp:.2f} mmHg\n"
#              f"Average Cholesterol: {avg_chol:.2f} mg/dL\n"
#              f"Average BMI: {avg_bmi:.2f}"
#     )

# # ----------------------------------------
# # UI LAYOUT
# # ----------------------------------------
# frame_top = tk.Frame(root, bg="#d9e6f2", pady=10)
# frame_top.pack(fill="x")

# tk.Label(frame_top, text="🏥 Health Data Analysis Dashboard", font=("Arial", 20, "bold"), bg="#d9e6f2").pack()

# upload_btn = tk.Button(frame_top, text="📂 Upload CSV", command=load_csv, bg="#4CAF50", fg="white", font=("Arial", 12))
# upload_btn.pack(pady=5)

# # Patient Selection
# patient_var = tk.StringVar()
# tk.Label(frame_top, text="Select Patient ID:", bg="#d9e6f2", font=("Arial", 12)).pack()
# patient_menu = ttk.Combobox(frame_top, textvariable=patient_var, state="readonly")
# patient_menu.pack()
# patient_menu.bind("<<ComboboxSelected>>", show_patient_data)

# # Patient Data Display
# info_frame = tk.Frame(root, bg="#f8fbfd", pady=10)
# info_frame.pack(fill="x")

# age_label = tk.Label(info_frame, text="Age: --", bg="#f8fbfd", font=("Arial", 12))
# gender_label = tk.Label(info_frame, text="Gender: --", bg="#f8fbfd", font=("Arial", 12))
# bmi_label = tk.Label(info_frame, text="BMI: --", bg="#f8fbfd", font=("Arial", 12))
# bp_label = tk.Label(info_frame, text="Blood Pressure: --", bg="#f8fbfd", font=("Arial", 12))
# chol_label = tk.Label(info_frame, text="Cholesterol: --", bg="#f8fbfd", font=("Arial", 12))
# hr_label = tk.Label(info_frame, text="Heart Rate: --", bg="#f8fbfd", font=("Arial", 12))

# age_label.pack(side="left", padx=15)
# gender_label.pack(side="left", padx=15)
# bmi_label.pack(side="left", padx=15)
# bp_label.pack(side="left", padx=15)
# chol_label.pack(side="left", padx=15)
# hr_label.pack(side="left", padx=15)

# # Chart Section
# chart_frame = tk.Frame(root, bg="#f0f4f7")
# chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

# plot_btn = tk.Button(root, text="📊 Show Charts", command=plot_charts, bg="#2196F3", fg="white", font=("Arial", 12))
# plot_btn.pack(pady=5)

# # NumPy Insights
# insights_label = tk.Label(root, text="", bg="#f0f4f7", font=("Arial", 12))
# insights_label.pack(pady=10)

# insights_btn = tk.Button(root, text="📈 Show Insights", command=show_insights, bg="#FF9800", fg="white", font=("Arial", 12))
# insights_btn.pack(pady=5)

# # ----------------------------------------
# # RUN APP
# # ----------------------------------------
# root.mainloop()
