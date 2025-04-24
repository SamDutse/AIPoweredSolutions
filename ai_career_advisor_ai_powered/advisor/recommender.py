import os
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli",
                      use_auth_token=hf_token)

# Sample list of Nigerian-relevant courses and careers
course_career_map = {
    "Computer Science": "Software Developer",
    "Mechanical Engineering": "Automobile Engineer",
    "Medicine": "Doctor",
    "Law": "Lawyer",
    "Mass Communication": "Journalist",
    "Nursing": "Nurse",
    "Architecture": "Architect",
    "Accounting": "Auditor",
    "Agriculture": "Agricultural Extension Officer",
    "Public Health": "Health Policy Specialist",
    "Education": "Teacher",
    "Fine Art": "Graphic Designer",
    "Business Administration": "Business Consultant"
}

def get_course_recommendations(user_input):
    labels = list(course_career_map.keys())
    result = classifier(user_input, labels)
    ranked_courses = list(zip(result["labels"], result["scores"]))
    top_recommendations = ranked_courses[:5]
    return [(course, course_career_map[course]) for course, score in top_recommendations]
