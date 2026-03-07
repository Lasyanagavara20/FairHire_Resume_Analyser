from skills_db import SKILLS

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume, jd):

    resume_skills = set(extract_skills(resume))
    jd_skills = set(extract_skills(jd))

    matched = list(resume_skills.intersection(jd_skills))
    missing = list(jd_skills - resume_skills)

    return matched, missing