from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline.")

        data_loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv" )
        processed_csv = data_loader.load_and_process()

        logger.info("Data loaded and processed successfully.")

        vector_builder = VectorStoreBuilder(processed_csv, persist_directory="chroma_db")
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built successfully.")

        logger.info("Pipeline build built successfully.")
    
    except Exception as e:
                    logger.error(f"Failed to execute recommendation: {str(e)}")
                    raise CustomException("Error during recommendation generation", e)

if __name__ == "__main__":
    main()