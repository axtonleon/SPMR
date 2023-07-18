import streamlit as st
from collections import Counter

st.title("STUDENT SUCCESS PREDICTOR")
st.info("   :information_source: answer the below questions with 1 as poor and 5 as very good")
questions = {
    "What level are you?": ("100", "200", "300", "400", "500"),
    "How would you describe your study habits and time management skills?": ("1", "2", "3", "4", "5"),
    "Are you actively engaged in class discussions and participate in group activities?": ("1", "2", "3", "4", "5"),
    "How often do you seek clarification or ask questions when you don't understand a concept?": ("1", "2", "3", "4", "5"),
    "Do you set specific goals for yourself and track your progress towards achieving them?": ("yes", "no"),
    "Are you able to effectively manage your workload and meet deadlines?": ("yes", "no"),
    "Do you actively seek additional resources or study materials to enhance your understanding of the subject matter?": ("yes", "no"),
    "How often do you review and reflect on your previous work to identify areas for improvement?": ("1", "2", "3", "4", "5"),
    "Are you able to adapt and apply knowledge learned in one subject to other related subjects?": ("yes", "no"),
    "Do you actively participate in study groups or seek peer collaboration to enhance your learning experience?": ("yes", "no"),
    "Are you able to manage test anxiety and perform well under exam conditions?": ("yes", "no"),
    "Are you familiar with effective note-taking techniques and do you implement them regularly?": ("yes", "no"),
    "Are you proactive in seeking help from teachers or classmates when you encounter difficulties?": ("yes", "no"),
    "Are you able to effectively analyze and evaluate information to form well-rounded arguments in your assignments or essays?": ("yes", "no"),
    "Do you suffer from any health issues that could affect your academic?": ("yes", "no")
}

selected_values = {}
st.selectbox('Select the model:', ("Xgboost", "Logistic Regression", "Support vector Machine","Deep Neural Network"))
for question, options in questions.items():
    selected_values[question] = st.selectbox(question, options)

if st.button("Predict"):
    # Access selected values
    level = int(selected_values["What level are you?"])
    time_skills = int(selected_values["How would you describe your study habits and time management skills?"])
    class_active = int(selected_values["Are you actively engaged in class discussions and participate in group activities?"])
    seek_clarification = int(selected_values["How often do you seek clarification or ask questions when you don't understand a concept?"])
    set_goals = selected_values["Do you set specific goals for yourself and track your progress towards achieving them?"]
    manage_workload = selected_values["Are you able to effectively manage your workload and meet deadlines?"]
    seek_resources = selected_values["Do you actively seek additional resources or study materials to enhance your understanding of the subject matter?"]
    review_work = int(selected_values["How often do you review and reflect on your previous work to identify areas for improvement?"])
    apply_knowledge = selected_values["Are you able to adapt and apply knowledge learned in one subject to other related subjects?"]
    participate_groups = selected_values["Do you actively participate in study groups or seek peer collaboration to enhance your learning experience?"]
    test_anxiety = selected_values["Are you able to manage test anxiety and perform well under exam conditions?"]
    note_taking = selected_values["Are you familiar with effective note-taking techniques and do you implement them regularly?"]
    seek_help = selected_values["Are you proactive in seeking help from teachers or classmates when you encounter difficulties?"]
    analyze_info = selected_values["Are you able to effectively analyze and evaluate information to form well-rounded arguments in your assignments or essays?"]
    health_issues = selected_values["Do you suffer from any health issues that could affect your academic?"]

    # Store pass/fail results in a list
    results = []



    if time_skills < 3:
        results.append("Fail")
    else:
        results.append("Pass")

    if class_active < 3:
        results.append("Fail")
    else:
        results.append("Pass")

    if seek_clarification < 3:
        results.append("Fail")
    else:
        results.append("Pass")

    if set_goals == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if manage_workload == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if seek_resources == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if review_work < 3:
        results.append("Fail")
    else:
        results.append("Pass")

    if apply_knowledge == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if participate_groups == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if test_anxiety == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if note_taking == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if seek_help == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if analyze_info == "no":
        results.append("Fail")
    else:
        results.append("Pass")

    if health_issues == "yes":
        results.append("Fail")
    else:
        results.append("Pass")

    # Calculate pass/fail percentage
    result_counter = Counter(results)
    pass_percentage = (result_counter["Pass"] / len(results)) * 100
    fail_percentage = (result_counter["Fail"] / len(results)) * 100

    # Display pass/fail percentages
    st.write("Pass Percentage:", pass_percentage)
    st.write("Fail Percentage:", fail_percentage)
