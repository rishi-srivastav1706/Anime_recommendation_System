import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anime Recommendation System", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommendation System")

query = st.text_input("Enter your anime preferences: (e.g., 'I like action and adventure with a touch of romance')")

if query:
    with st.spinner("Fetching recommendations for you..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommended Anime:")
        st.write(response) 