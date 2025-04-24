import streamlit as st
from advisor.recommender import get_course_recommendations
import os
from dotenv import load_dotenv

load_dotenv()

st.title("🎓 AI Career & Course Advisor")
st.markdown("Let AI help you choose a career path based on your interests and academic background.")

name = st.text_input("Your Name")
interests = st.text_area("Describe your interests and career dreams (e.g., I love solving problems with tech, or I enjoy drawing and creativity)")
waec_subjects = st.text_input("WAEC Subjects (comma-separated)")
utme_score = st.number_input("Your UTME Score", min_value=100, max_value=400)

if st.button("Get AI-Powered Suggestions"):
    with st.spinner("Thinking..."):
        recommendations = get_course_recommendations(interests)
    st.success("Here are some recommendations based on your input:")
    for item in recommendations:
        st.markdown(f"- **{item[0]}** → _Possible Career: {item[1]}_")
