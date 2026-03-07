from flask import Flask, request, jsonify, render_template
from resume_parser import extract_text
from preprocess import clean_text
from similarity import calculate_similarity
from explainability import generate_explanation
from skills_matcher import compare_skills

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_resume():

    try:

        if 'resume' not in request.files:
            return jsonify({"error": "No resume uploaded"})

        file = request.files['resume']
        job_description = request.form.get("job_description")

        if file.filename == "":
            return jsonify({"error": "No file selected"})

        if not job_description:
            return jsonify({"error": "Job description missing"})

        # Extract resume text
        resume_text = extract_text(file)

        # Clean text
        processed_resume = clean_text(resume_text)
        processed_jd = clean_text(job_description)

        # Similarity score
        score = calculate_similarity(processed_resume, processed_jd)

        # Skill comparison
        matched_skills, missing_skills = compare_skills(processed_resume, processed_jd)

        # Explanation
        explanation = generate_explanation(processed_resume)

        return jsonify({
            "score": round(score * 100, 2),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "explanation": explanation
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)