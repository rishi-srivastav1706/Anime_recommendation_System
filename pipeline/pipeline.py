from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            logger.info("Initializing the Recommendation Pipeline.")

            vector_builder = VectorStoreBuilder(csv_path = "", persist_directory=persist_directory)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize the pipeline: {str(e)}")
            raise CustomException("Error during pipeline initialization",e)

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received a query: {query}")

            recommendation = self.recommender.get_recommendations(query)

            logger.info("Recommendation generated successfully for query..")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to generate recommendation: {str(e)}")
            raise CustomException("Error during recommendation generation", e)