import os
import pickle
from colorama import Fore, Style

# Define the target for loading the model (local, docker, gcs, mlflow)
MODEL_TARGET = "local"  # Change this as needed

# Set model path based on environment (default to Docker's path for docker)


MODEL_PATH = os.getenv('MODEL_PATH', '/Users/SHAD/code/Parvxi/Peaklytics/peaklytics/ml_logic/final_lgbm_model_2')

def load_model():
    if MODEL_TARGET == "local":
        print(Fore.BLUE + f"\nLoading model from local file..." + Style.RESET_ALL)

        # Check if the model path exists
        if not os.path.exists(MODEL_PATH):
            print(f"\n❌ Model not found at {MODEL_PATH}")
            return None

        # Load the model from the .pkl file using pickle
        try:
            with open(MODEL_PATH, 'rb') as model_file:
                model = pickle.load(model_file)
            print("✅ Model successfully loaded from local disk (Pickle model)")
            return model
        except Exception as e:
            print(f"\n❌ Error loading model: {e}")
            return None

    elif MODEL_TARGET == "docker":
        print(Fore.GREEN + f"\nLoading model from Docker container at {MODEL_PATH}..." + Style.RESET_ALL)

        # Load the model from Docker path
        try:
            with open(MODEL_PATH, 'rb') as model_file:
                model = pickle.load(model_file)
            print("✅ Model successfully loaded from Docker container")
            return model
        except Exception as e:
            print(f"\n❌ Error loading model from Docker: {e}")
            return None

    elif MODEL_TARGET == "gcs":
        print(Fore.BLUE + f"\nLoad latest model from GCS..." + Style.RESET_ALL)

        # Uncomment and implement GCS functionality
        # client = storage.Client()
        # blobs = list(client.get_bucket(BUCKET_NAME).list_blobs(prefix="model"))
        #
        # try:
        #     latest_blob = max(blobs, key=lambda x: x.updated)
        #     latest_model_path_to_save = os.path.join(LOCAL_REGISTRY_PATH, latest_blob.name)
        #     latest_blob.download_to_filename(latest_model_path_to_save)
        #
        #     if latest_model_path_to_save.endswith(".pkl"):
        #         with open(latest_model_path_to_save, 'rb') as model_file:
        #             model = pickle.load(model_file)
        #     else:
        #         model = keras.models.load_model(latest_model_path_to_save)
        #
        #     print("✅ Latest model downloaded from GCS")
        #     return model
        # except Exception as e:
        #     print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}: {e}")
        #     return None
        pass  # Placeholder for GCS

    elif MODEL_TARGET == "mlflow":
        stage = "production"
        print(Fore.BLUE + f"\nLoad [{stage}] model from MLflow..." + Style.RESET_ALL)

        # Uncomment and implement MLflow functionality
        # mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        # client = MlflowClient()
        #
        # try:
        #     model_versions = client.get_latest_versions(name=MLFLOW_MODEL_NAME, stages=[stage])
        #     model_uri = model_versions[0].source
        #
        #     if model_uri.endswith(".pkl"):
        #         with open(model_uri, 'rb') as model_file:
        #             model = pickle.load(model_file)
        #     else:
        #         model = keras.models.load_model(model_uri)
        #
        #     print("✅ Model loaded from MLflow")
        #     return model
        # except Exception as e:
        #     print(f"\n❌ No model found with name {MLFLOW_MODEL_NAME} in stage {stage}: {e}")
        #     return None
        pass  # Placeholder for MLflow

    else:
        print(f"\n❌ MODEL_TARGET '{MODEL_TARGET}' not supported.")
        return None
