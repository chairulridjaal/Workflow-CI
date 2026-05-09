import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_data(filepath):
    df = pd.read_csv(filepath)
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    return X, y

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, 'titanic_preprocessing', 'titanic_preprocessed.csv')
    
    X, y = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    mlflow.sklearn.autolog()
    
    with mlflow.start_run(run_name="CI_Pipeline_Run"):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(f"[SUCCESS] CI Run Completed. Test Accuracy: {score:.4f}")
# Trigger action CI
# Trigger action CI again
