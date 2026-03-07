from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume, jd):

    resume_embedding = model.encode(resume, convert_to_numpy=True)
    jd_embedding = model.encode(jd, convert_to_numpy=True)

    similarity_score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return float(similarity_score)