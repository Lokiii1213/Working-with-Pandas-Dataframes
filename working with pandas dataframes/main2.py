import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("students.csv")


# ============================================================
# 2. PANDAS DATA PROCESSING
# ============================================================

# Calculate average marks
df["Average"] = (
    df["Maths"] +
    df["Python"] +
    df["Data_Science"]
) / 3

df["Average"] = df["Average"].round(2)


# Calculate grade
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"


df["Grade"] = df["Average"].apply(calculate_grade)


# ============================================================
# 3. MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Student Performance Analysis")
root.geometry("1250x780")
root.minsize(1100, 700)

root.configure(bg="#F4F7FB")


# ============================================================
# 4. COLORS
# ============================================================

NAVY = "#172554"
BLUE = "#2563EB"
CYAN = "#0891B2"
GREEN = "#16A34A"
PURPLE = "#7C3AED"
ORANGE = "#EA580C"
RED = "#DC2626"

WHITE = "#FFFFFF"
BLACK = "#111827"
GRAY = "#64748B"
LIGHT = "#F4F7FB"
BORDER = "#E2E8F0"


# ============================================================
# 5. HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=NAVY,
    height=95
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


title = tk.Label(
    header,
    text="🎓 Student Performance Analysis",
    font=("Segoe UI", 25, "bold"),
    bg=NAVY,
    fg=WHITE
)

title.pack(
    pady=(14, 0)
)


subtitle = tk.Label(
    header,
    text="Fundamentals of Data Science  •  Working with Pandas DataFrames",
    font=("Segoe UI", 11),
    bg=NAVY,
    fg="#BFDBFE"
)

subtitle.pack()


# ============================================================
# 6. DASHBOARD CARD AREA
# ============================================================

cards_frame = tk.Frame(
    root,
    bg=LIGHT
)

cards_frame.pack(
    fill="x",
    padx=25,
    pady=20
)


def create_card(parent, title_text, value_text, color):

    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    card.pack(
        side="left",
        expand=True,
        fill="both",
        padx=7
    )

    top_line = tk.Frame(
        card,
        bg=color,
        height=5
    )

    top_line.pack(
        fill="x"
    )

    value = tk.Label(
        card,
        text=value_text,
        font=("Segoe UI", 23, "bold"),
        bg=WHITE,
        fg=color
    )

    value.pack(
        pady=(13, 2)
    )

    label = tk.Label(
        card,
        text=title_text,
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=GRAY
    )

    label.pack(
        pady=(0, 13)
    )

    return value


total_card = create_card(
    cards_frame,
    "TOTAL STUDENTS",
    str(len(df)),
    BLUE
)


average_card = create_card(
    cards_frame,
    "OVERALL AVERAGE",
    f"{df['Average'].mean():.2f}",
    GREEN
)


top_student_card = create_card(
    cards_frame,
    "TOP PERFORMER",
    df.loc[df["Average"].idxmax(), "Name"],
    PURPLE
)


attendance_card = create_card(
    cards_frame,
    "AVG ATTENDANCE",
    f"{df['Attendance'].mean():.1f}%",
    ORANGE
)


# ============================================================
# 7. BUTTON AREA
# ============================================================

button_area = tk.Frame(
    root,
    bg=LIGHT
)

button_area.pack(
    fill="x",
    padx=25,
    pady=(0, 10)
)


def create_button(text, command, color):

    return tk.Button(
        button_area,
        text=text,
        command=command,
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=8
    )


# ============================================================
# 8. TABLE FRAME
# ============================================================

table_container = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

table_container.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=5
)


table_title = tk.Label(
    table_container,
    text="📋 Student DataFrame",
    font=("Segoe UI", 15, "bold"),
    bg=WHITE,
    fg=BLACK
)

table_title.pack(
    anchor="w",
    padx=15,
    pady=10
)


# ============================================================
# 9. TREEVIEW STYLE
# ============================================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    foreground=BLACK,
    rowheight=32,
    fieldbackground=WHITE,
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    background=NAVY,
    foreground=WHITE,
    font=("Segoe UI", 10, "bold"),
    padding=8
)

style.map(
    "Treeview",
    background=[
        ("selected", "#DBEAFE")
    ],
    foreground=[
        ("selected", BLACK)
    ]
)


# ============================================================
# 10. TABLE
# ============================================================

columns = (
    "Name",
    "Age",
    "Gender",
    "Maths",
    "Python",
    "Data Science",
    "Attendance",
    "Average",
    "Grade"
)


tree_frame = tk.Frame(
    table_container,
    bg=WHITE
)

tree_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)


tree = ttk.Treeview(
    tree_frame,
    columns=columns,
    show="headings"
)


for column in columns:

    tree.heading(
        column,
        text=column
    )

    tree.column(
        column,
        anchor="center",
        width=110
    )


tree.column(
    "Name",
    width=130
)

tree.column(
    "Data Science",
    width=130
)


vertical_scroll = ttk.Scrollbar(
    tree_frame,
    orient="vertical",
    command=tree.yview
)

horizontal_scroll = ttk.Scrollbar(
    tree_frame,
    orient="horizontal",
    command=tree.xview
)


tree.configure(
    yscrollcommand=vertical_scroll.set,
    xscrollcommand=horizontal_scroll.set
)


tree.pack(
    side="left",
    fill="both",
    expand=True
)

vertical_scroll.pack(
    side="right",
    fill="y"
)

horizontal_scroll.pack(
    side="bottom",
    fill="x"
)


# ============================================================
# 11. DISPLAY DATAFRAME
# ============================================================

def display_data(data):

    for item in tree.get_children():

        tree.delete(item)

    for _, row in data.iterrows():

        tree.insert(
            "",
            "end",
            values=(
                row["Name"],
                row["Age"],
                row["Gender"],
                row["Maths"],
                row["Python"],
                row["Data_Science"],
                row["Attendance"],
                row["Average"],
                row["Grade"]
            )
        )


display_data(df)


# ============================================================
# 12. UPDATE DASHBOARD
# ============================================================

def update_dashboard():

    total_card.config(
        text=str(len(df))
    )

    average_card.config(
        text=f"{df['Average'].mean():.2f}"
    )

    top_student_card.config(
        text=df.loc[
            df["Average"].idxmax(),
            "Name"
        ]
    )

    attendance_card.config(
        text=f"{df['Attendance'].mean():.1f}%"
    )


# ============================================================
# 13. STATISTICS
# ============================================================

def show_statistics():

    maths_avg = df["Maths"].mean()

    python_avg = df["Python"].mean()

    ds_avg = df["Data_Science"].mean()

    highest = df.loc[
        df["Average"].idxmax()
    ]

    lowest = df.loc[
        df["Average"].idxmin()
    ]

    statistics = f"""
📊 DATASET STATISTICS

━━━━━━━━━━━━━━━━━━━━━━━━

Total Students     : {len(df)}

Overall Average    : {df["Average"].mean():.2f}

Average Attendance : {df["Attendance"].mean():.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━

📚 SUBJECT AVERAGES

Maths              : {maths_avg:.2f}

Python             : {python_avg:.2f}

Data Science       : {ds_avg:.2f}

━━━━━━━━━━━━━━━━━━━━━━━━

🏆 TOP PERFORMER

Name               : {highest["Name"]}

Average            : {highest["Average"]}

Grade              : {highest["Grade"]}

━━━━━━━━━━━━━━━━━━━━━━━━

📉 LOWEST PERFORMER

Name               : {lowest["Name"]}

Average            : {lowest["Average"]}

Grade              : {lowest["Grade"]}
"""

    messagebox.showinfo(
        "Statistics",
        statistics
    )


# ============================================================
# 14. TOP STUDENTS
# ============================================================

def show_top_students():

    top_students = df.sort_values(
        "Average",
        ascending=False
    ).head(5)

    result = "🏆 TOP 5 STUDENTS\n\n"

    for position, (_, row) in enumerate(
        top_students.iterrows(),
        start=1
    ):

        result += (
            f"{position}. "
            f"{row['Name']}   |   "
            f"Average: {row['Average']}   |   "
            f"Grade: {row['Grade']}\n\n"
        )

    messagebox.showinfo(
        "Top Performers",
        result
    )


# ============================================================
# 15. SEARCH STUDENT
# ============================================================

def search_student():

    window = tk.Toplevel(root)

    window.title(
        "Search Student"
    )

    window.geometry(
        "430x280"
    )

    window.configure(
        bg=WHITE
    )

    window.resizable(
        False,
        False
    )


    tk.Label(
        window,
        text="🔍 Search Student",
        font=("Segoe UI", 20, "bold"),
        bg=WHITE,
        fg=NAVY
    ).pack(
        pady=(25, 15)
    )


    entry = tk.Entry(
        window,
        font=("Segoe UI", 13),
        width=28,
        relief="solid",
        bd=1
    )

    entry.pack(
        pady=5
    )

    entry.focus()


    def search():

        name = entry.get().strip()

        result = df[
            df["Name"].str.lower()
            == name.lower()
        ]


        if result.empty:

            messagebox.showwarning(
                "Student Not Found",
                "No student found with that name.",
                parent=window
            )

            return


        student = result.iloc[0]


        details = f"""
👨‍🎓 STUDENT DETAILS

Name       : {student["Name"]}

Age        : {student["Age"]}

Gender     : {student["Gender"]}

Maths      : {student["Maths"]}

Python     : {student["Python"]}

Data Science : {student["Data_Science"]}

Attendance : {student["Attendance"]}%

Average    : {student["Average"]}

Grade      : {student["Grade"]}
"""


        messagebox.showinfo(
            "Student Information",
            details,
            parent=window
        )


    tk.Button(
        window,
        text="Search",
        command=search,
        bg=BLUE,
        fg=WHITE,
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=25,
        pady=8,
        cursor="hand2"
    ).pack(
        pady=20
    )


# ============================================================
# 16. SUBJECT CHART
# ============================================================

def subject_chart():

    subjects = [
        "Maths",
        "Python",
        "Data Science"
    ]

    averages = [
        df["Maths"].mean(),
        df["Python"].mean(),
        df["Data_Science"].mean()
    ]


    plt.figure(
        figsize=(9, 5)
    )


    bars = plt.bar(
        subjects,
        averages
    )


    plt.title(
        "Average Marks by Subject",
        fontsize=17,
        fontweight="bold"
    )

    plt.xlabel(
        "Subjects"
    )

    plt.ylabel(
        "Average Marks"
    )


    plt.ylim(
        0,
        100
    )


    for bar in bars:

        value = bar.get_height()

        plt.text(
            bar.get_x()
            + bar.get_width() / 2,
            value + 1,
            f"{value:.1f}",
            ha="center",
            fontweight="bold"
        )


    plt.grid(
        axis="y",
        alpha=0.2
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 17. STUDENT PERFORMANCE CHART
# ============================================================

def student_chart():

    data = df.sort_values(
        "Average",
        ascending=False
    )


    plt.figure(
        figsize=(11, 5)
    )


    bars = plt.bar(
        data["Name"],
        data["Average"]
    )


    plt.title(
        "Student Average Performance",
        fontsize=17,
        fontweight="bold"
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Average Marks"
    )


    plt.ylim(
        0,
        100
    )


    plt.xticks(
        rotation=45
    )


    for bar in bars:

        value = bar.get_height()

        plt.text(
            bar.get_x()
            + bar.get_width() / 2,
            value + 1,
            f"{value:.1f}",
            ha="center",
            fontsize=8
        )


    plt.grid(
        axis="y",
        alpha=0.2
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 18. ATTENDANCE CHART
# ============================================================

def attendance_chart():

    data = df.sort_values(
        "Attendance",
        ascending=False
    )


    plt.figure(
        figsize=(11, 5)
    )


    bars = plt.bar(
        data["Name"],
        data["Attendance"]
    )


    plt.title(
        "Student Attendance Analysis",
        fontsize=17,
        fontweight="bold"
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Attendance (%)"
    )


    plt.ylim(
        0,
        100
    )


    plt.xticks(
        rotation=45
    )


    for bar in bars:

        value = bar.get_height()

        plt.text(
            bar.get_x()
            + bar.get_width() / 2,
            value + 1,
            f"{value:.0f}%",
            ha="center",
            fontsize=8
        )


    plt.grid(
        axis="y",
        alpha=0.2
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 19. SORT BY AVERAGE
# ============================================================

def sort_by_average():

    sorted_df = df.sort_values(
        "Average",
        ascending=False
    )

    display_data(
        sorted_df
    )


# ============================================================
# 20. FILTER HIGH PERFORMERS
# ============================================================

def high_performers():

    filtered = df[
        df["Average"] >= 80
    ]

    display_data(
        filtered
    )

    messagebox.showinfo(
        "Filter Applied",
        f"{len(filtered)} students have an average of 80 or above."
    )


# ============================================================
# 21. SHOW ALL STUDENTS
# ============================================================

def show_all():

    display_data(
        df
    )


# ============================================================
# 22. REFRESH
# ============================================================

def refresh_data():

    global df

    df = pd.read_csv(
        "students.csv"
    )


    df["Average"] = (
        df["Maths"]
        + df["Python"]
        + df["Data_Science"]
    ) / 3


    df["Average"] = df[
        "Average"
    ].round(2)


    df["Grade"] = df[
        "Average"
    ].apply(
        calculate_grade
    )


    display_data(
        df
    )


    update_dashboard()


    messagebox.showinfo(
        "Refresh",
        "Dataset refreshed successfully!"
    )


# ============================================================
# 23. BUTTONS
# ============================================================

create_button(
    "📊 Statistics",
    show_statistics,
    BLUE
).pack(
    side="left",
    padx=3
)


create_button(
    "🏆 Top 5",
    show_top_students,
    PURPLE
).pack(
    side="left",
    padx=3
)


create_button(
    "📚 Subject Chart",
    subject_chart,
    GREEN
).pack(
    side="left",
    padx=3
)


create_button(
    "👨‍🎓 Student Chart",
    student_chart,
    CYAN
).pack(
    side="left",
    padx=3
)


create_button(
    "📅 Attendance",
    attendance_chart,
    ORANGE
).pack(
    side="left",
    padx=3
)


create_button(
    "🔍 Search",
    search_student,
    NAVY
).pack(
    side="left",
    padx=3
)


create_button(
    "↕ Sort",
    sort_by_average,
    RED
).pack(
    side="left",
    padx=3
)


create_button(
    "⭐ 80+ Students",
    high_performers,
    GREEN
).pack(
    side="left",
    padx=3
)


create_button(
    "👥 All Students",
    show_all,
    GRAY
).pack(
    side="left",
    padx=3
)


create_button(
    "🔄 Refresh",
    refresh_data,
    "#475569"
).pack(
    side="left",
    padx=3
)


# ============================================================
# 24. FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="Python  •  Pandas  •  Tkinter  •  Matplotlib",
    font=("Segoe UI", 9),
    bg=LIGHT,
    fg=GRAY
)

footer.pack(
    pady=8
)


# ============================================================
# 25. START APPLICATION
# ============================================================

root.mainloop()