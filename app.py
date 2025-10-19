import streamlit as st

# Title
st.title("🎓 GPA & CGPA Calculator (4.00 Scale)")

# Grade scale conversion (out of 100 ➝ GPA out of 4.00)
def get_grade_info(marks):
    if marks >= 90:
        return 4.00, "A+"
    elif marks >= 85:
        return 3.75, "A"
    elif marks >= 80:
        return 3.50, "A-"
    elif marks >= 75:
        return 3.25, "B+"
    elif marks >= 70:
        return 3.00, "B"
    elif marks >= 65:
        return 2.75, "B-"
    elif marks >= 60:
        return 2.50, "C+"
    elif marks >= 50:
        return 2.00, "C"
    else:
        return 0.00, "F"

# Input: number of subjects
num_subjects = st.number_input("📘 Enter number of subjects this semester:", min_value=1, step=1)

grade_data = []

st.header("📝 Subject Marks Entry")

# Input: Subject names and marks
for i in range(1, int(num_subjects) + 1):
    subject_name = st.text_input(f"Subject {i} Name", key=f"sub_{i}")
    marks = st.number_input(f"Enter marks for {subject_name or f'Subject {i}'}", min_value=0.0, max_value=100.0, key=f"marks_{i}")
    
    if subject_name:
        grade_point, letter_grade = get_grade_info(marks)
        grade_data.append({
            "Subject": subject_name,
            "Marks": marks,
            "Grade Point": grade_point,
            "Letter Grade": letter_grade
        })

# GPA calculation
if len(grade_data) == num_subjects:
    st.subheader("📊 Semester Grade Summary")
    st.table(grade_data)

    total_grade_points = sum([entry["Grade Point"] for entry in grade_data])
    gpa = total_grade_points / num_subjects
    st.success(f"✅ Your GPA for this semester is: **{gpa:.2f} / 4.00**")

    # CGPA input
    st.header("📈 Calculate CGPA (with previous semesters)")

    num_prev_sem = st.number_input("Enter number of previous semesters:", min_value=0, step=1)
    
    total_gpa = gpa
    total_sem = 1

    for j in range(1, int(num_prev_sem) + 1):
        prev_gpa = st.number_input(f"Enter GPA for semester {j}", min_value=0.0, max_value=4.0, key=f"prev_gpa_{j}")
        total_gpa += prev_gpa
        total_sem += 1

    if total_sem > 1:
        cgpa = total_gpa / total_sem
        st.success(f"🎓 Your CGPA across {total_sem} semesters is: **{cgpa:.2f} / 4.00**")



