skills = [
    "python",
    "machine learning",
    "nlp",
    "sql",
    "data analysis",
    "deep learning",
    "tensorflow",
    "pytorch"
]


def generate_explanation(resume_text):

    found_skills = []

    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)

    if len(found_skills) == 0:
        return "Few relevant skills found in resume."

    return f"Relevant skills detected: {', '.join(found_skills)}"