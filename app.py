import streamlit as st

st.title("🎓 GPA & CGPA Calculator")

# Choose what to calculate
option = st.radio("What do you want to calculate?", ("GPA", "CGPA"))

# GPA Calculation
if option == "GPA":
    st.header("📘 GPA Calculator")

    num_subjects = st.number_input("Enter number of subjects", min_value=1, step=1)

    total_grade_points = 0

    for i in range(1, int(num_subjects) + 1):
        marks = st.number_input(f"Enter marks for subject {i}", min_value=0.0, max_value=100.0)
        
        # Simple grade point calculation
        if marks >= 90:
            grade_point = 10
        elif marks >= 80:
            grade_point = 9
        elif marks >= 70:
            grade_point = 8
        elif marks >= 60:
            grade_point = 7
        elif marks >= 50:
            grade_point = 6
        elif marks >= 40:
            grade_point = 5
        else:
            grade_point = 0

        total_grade_points += grade_point

    if num_subjects:
        gpa = total_grade_points / num_subjects
        st.success(f"✅ Your GPA is: {gpa:.2f}")

# CGPA Calculation
elif option == "CGPA":
    st.header("📗 CGPA Calculator")

    num_semesters = st.number_input("Enter number of semesters", min_value=1, step=1)

    total_gpa = 0

    for i in range(1, int(num_semesters) + 1):
        semester_gpa = st.number_input(f"Enter GPA for semester {i}", min_value=0.0, max_value=10.0)
        total_gpa += semester_gpa

    if num_semesters:
        cgpa = total_gpa / num_semesters
        st.success(f"🎉 Your CGPA is: {cgpa:.2f}")

