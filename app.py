import streamlit as st

# Title
st.title("🎓 GPA & CGPA Calculator")

# Get number of subjects
num_subjects = st.number_input("📚 Enter number of subjects this semester", min_value=1, step=1)

subjects = []

grade_data = []

# Function to convert marks to grade point and letter grade
def get_grade_info(marks):
    if marks >= 90:
        return 10, "O"
    elif marks >= 80:
        return 9, "A+"
    elif marks >= 70:
        return 8, "A"
    elif marks >= 60:
        return 7, "B+"
    elif marks >= 50:
        return 6, "B"
    elif marks >= 40:
        return 5, "C"
    else:
        return 0, "F"

# Enter subject names and marks
st.header("📝 Enter Subject Details")

for i in range(1, int(num_subjects) + 1):
    st.subheader(f"Subject {i}")
    subject_name = st.text_input(f"Enter name for subject {i}", key=f"name_{i}")
    marks = st.number_input(f"Enter marks for {subject_name or f'Subject {i}'}", min_value=0.0, max_value=100.0, key=f"marks_{i}")
    
    if subject_name:
        grade_point, letter_grade = get_grade_info(marks)
        grade_data.append({
            "subject": subject_name,
            "marks": marks,
            "grade_point": grade_point,
            "letter_grade": letter_grade
        })

# Show table after all subjects entered
if len(grade_data) == num_subjects:
    st.subheader("📊 Grade Summary")
    st.table(grade_data)

    total_gp = sum([entry["grade_point"] for entry in grade_data])
    gpa = total_gp / num_subjects
    st.success(f"✅ Your GPA for this semester is: **{gpa:.2f}**")

    # CGPA input
    st.header("📈 Calculate CGPA (if you have previous semesters)")

    num_prev_sem = st.number_input("How many previous semesters do you have?", min_value=0, step=1)

    total_gpa = gpa  # Start with current semester GPA
    total_sem = 1    # Start with current semester

    for j in range(1, int(num_prev_sem) + 1):
        prev_gpa = st.number_input(f"Enter GPA for semester {j}", min_value=0.0, max_value=10.0, key=f"prev_gpa_{j}")
        total_gpa += prev_gpa
        total_sem += 1

    if total_sem > 1:
        final_cgpa = total_gpa / total_sem
        st.success(f"🎉 Your CGPA across {total_sem} semesters is: **{final_cgpa:.2f}**")


