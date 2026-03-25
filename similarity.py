from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume, jd):
    try:
        resume = resume[:2000]
        jd = jd[:2000]

        embeddings = model.encode([resume, jd])

        similarity_score = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        return float(similarity_score)

    except Exception as e:
        print("Similarity Error:", e)
        return 0.0