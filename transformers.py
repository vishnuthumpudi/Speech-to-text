from sentence_transformers import SentenceTransformer, util

# Load pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define question and response
question = "What is machine learning?"
response = "Machine learning is a field of artificial intelligence that enables computers to learn from data."

# Get embeddings
q_embedding = model.encode(question, convert_to_tensor=True)
r_embedding = model.encode(response, convert_to_tensor=True)

# Compute similarity
similarity_score = util.pytorch_cos_sim(q_embedding, r_embedding)

print(f"Relevance Score: {similarity_score.item():.2f}")  # Closer to 1 means more relevant
