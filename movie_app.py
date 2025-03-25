import streamlit as st
import pickle
import base64
import time

# Load movie data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    if movie not in movies['title'].values:
        return ["❌ Movie not found. Please try another title."]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommendations

# Function to encode the image in Base64
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    return encoded_img

# Apply background image
def set_background(image_path):
    encoded_img = get_base64_encoded_image(image_path)
    bg_css = f"""
    <style>
        .stApp {{
            background: url("data:image/jpeg;base64,{encoded_img}") no-repeat center center fixed;
            background-size: cover;
        }}
        .movie-title {{
            font-size: 40px;
            font-weight: bold;
            color: #32CD32;
            text-align: center;
            text-shadow: 4px 4px 10px black;
            margin-bottom: 20px;
        }}
        .input-label {{
            font-size: 22px;
            font-weight: bold;
            color: #00ffff;
            margin-bottom: 10px;
        }}
        .stTextInput {{
            font-size: 18px;
            color: black;
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #4CAF50;
            background-color: #f0fff0;
        }}
        .recommend-btn {{
            background: linear-gradient(45deg, #1E90FF, #4CAF50, #32CD32);
            color: white;
            border-radius: 12px;
            font-size: 22px;
            padding: 14px 28px;
            border: none;
            box-shadow: 0px 4px 15px rgba(50, 205, 50, 0.7);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .recommend-btn:hover {{
            transform: scale(1.15);
            background: linear-gradient(45deg, #32CD32, #4CAF50, #1E90FF);
            box-shadow: 0px 6px 20px rgba(50, 205, 50, 0.9);
        }}
        .recommendation-list {{
            font-size: 22px;
            color: #ADD8E6;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }}
        .recommendation-list li {{
            margin-bottom: 10px;
            text-shadow: 2px 2px 5px black;
        }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set the background image
set_background(r"C:/Users/asimk/movies_pic.jpeg")

# Streamlit UI
st.markdown("<h1 class='movie-title'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Input field
st.markdown("<label class='input-label'>Enter a movie name:</label>", unsafe_allow_html=True)
movie_name = st.text_input("", key="movie_input", placeholder="Type a movie name here")

# Recommend button
if st.button("Recommend", key="recommend_btn", help="Click to get movie recommendations"):
    with st.spinner("Finding the best movies for you... 🎥✨"):
        time.sleep(2)  # Simulate loading effect
    
    recommendations = recommend(movie_name)
    st.markdown("<h3 style='color:yellow; text-align: center;'>Recommended Movies:</h3>", unsafe_allow_html=True)
    
    st.markdown("<ul class='recommendation-list'>", unsafe_allow_html=True)
    for rec in recommendations:
        st.markdown(f"<li>✅ {rec}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)