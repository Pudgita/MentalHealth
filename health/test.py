# ml_service.py
import joblib
import os

# Загружаем модель через joblib (НЕ через pickle!)
model_path = os.path.join(os.path.dirname(__file__), 'mental_health_model.pkl')
model = joblib.load(model_path)

def predict(input_data):
    return model.predict(input_data)