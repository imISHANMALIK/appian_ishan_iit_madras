# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data (simulated data)
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [5, 3, 4, 2],
    'History': [4, 5, 2, 3],
    'Science': [2, 4, 5, 3],
    'Programming': [5, 2, 3, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate similarity matrix
cosine_sim = cosine_similarity(df.iloc[:, 1:])

# Function to get course recommendations
def get_recommendations(student_name):
    student_index = df[df['Student'] == student_name].index[0]
    sim_scores = list(enumerate(cosine_sim[student_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Top 3 similar students
    student_indices = [i[0] for i in sim_scores]
    return df['Student'].iloc[student_indices].tolist()