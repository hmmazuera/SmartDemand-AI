from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / 'models' / 'best_model.pkl'

APP_TITLE = 'SmartDemand-AI'

APP_SUBTITLE = 'Predict hourly bike rental demand using machine learning models'