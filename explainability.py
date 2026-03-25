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

def generate_explanation(resume_text, matched_skills, missing_skills, score):

    explanation = []

    # 🔹 Overall match quality
    if score > 75:
        explanation.append("Your resume is highly relevant to the job description.")
    elif score > 50:
        explanation.append("Your resume partially matches the job requirements.")
    else:
        explanation.append("Your resume has low alignment with the job description.")

    # 🔹 Skills detected from your original logic
    found_skills = []
    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)

    if found_skills:
        explanation.append("Relevant skills detected: " + ", ".join(found_skills[:5]))

    # 🔹 Matched skills (from JD comparison)
    if matched_skills:
        explanation.append("Strong match in: " + ", ".join(matched_skills[:5]))

    # 🔹 Missing skills
    if missing_skills:
        explanation.append("Missing important skills like: " + ", ".join(missing_skills[:5]))

    # 🔹 Final guidance
    explanation.append("Improve project descriptions and align your experience with the job role for better results.")

    return " ".join(explanation)