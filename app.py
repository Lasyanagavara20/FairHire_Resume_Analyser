from flask import Flask, request, jsonify, render_template
from resume_parser import extract_text
from preprocess import clean_text
from similarity import calculate_similarity
from explainability import generate_explanation
from skills_matcher import compare_skills
from common_jds import common_jds

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_resume():

    try:
        # 🔍 Validate input
        if 'resume' not in request.files:
            return jsonify({"error": "No resume uploaded"})

        file = request.files['resume']
        job_description = request.form.get("job_description")
        selected_role = request.form.get("role")

        if file.filename == "":
            return jsonify({"error": "No file selected"})

        # 🔥 Use predefined JD if role selected
        if selected_role and selected_role in common_jds:
            job_description = common_jds[selected_role]

        if not job_description:
            return jsonify({"error": "Job description missing"})

        # 📄 Extract + preprocess
        resume_text = extract_text(file)
        processed_resume = clean_text(resume_text)
        processed_jd = clean_text(job_description)

        # 🧠 Semantic similarity
        semantic_score = calculate_similarity(processed_resume, processed_jd)

        # 🎯 Skill comparison
        matched_skills, missing_skills = compare_skills(processed_resume, processed_jd)

        # 📊 Skill score
        total_skills = len(matched_skills) + len(missing_skills)
        skill_score = (len(matched_skills) / total_skills) if total_skills > 0 else 0

        # 🔥 Final hybrid score
        final_score = (0.7 * semantic_score) + (0.3 * skill_score)
        final_score_percent = round(final_score * 100, 2)

        # 🧠 Smart explanation (UPDATED CALL)
        explanation = generate_explanation(
            processed_resume,
            matched_skills,
            missing_skills,
            final_score_percent
        )

        # 💡 Smart suggestions
        suggestions = []

        if len(missing_skills) == 0 and final_score > 0.6:
            suggestions.append("Excellent! Your resume strongly matches this role.")

        elif len(missing_skills) == 0:
            suggestions.append("You have the required skills, but improve project descriptions and experience relevance.")

        elif final_score < 0.5:
            suggestions.append("Your resume is not well aligned with this role. Consider adding relevant skills and experience.")

        else:
            suggestions.append("You have a decent profile. Improving missing skills can boost your chances.")

        # 🔹 Add missing skills suggestion
        if missing_skills:
            suggestions.append("Consider learning: " + ", ".join(missing_skills[:5]))

        return jsonify({
            "score": final_score_percent,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "explanation": explanation,
            "suggestions": suggestions,
            "selected_role": selected_role if selected_role else "Custom JD"
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)