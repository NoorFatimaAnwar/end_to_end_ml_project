import os

project_name = "ml_project"
# List of folders and files you want in your ML project
project_structure = [
    "src/",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluater.py",
    "src/utils/",
    "src/pipeline/",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/predicting_pipeline.py",
    
 
    
    "loggers",
    
    
    "requirements.txt",
    "setup.py",
    ".gitignore",
    "README.md"
]


def create_structure(base_path="."):
    for path in project_structure:
        full_path = os.path.join(base_path, path)

        # If it's a file (has extension)
        if os.path.splitext(path)[1]:
            folder = os.path.dirname(full_path)

            # Create folder if not exists
            if folder and not os.path.exists(folder):
                os.makedirs(folder)
                print(f"📁 Created folder: {folder}")

            # Create file only if it doesn't exist
            if not os.path.exists(full_path):
                with open(full_path, "w") as f:
                    pass  # create empty file
                print(f"📄 Created file: {full_path}")
            else:
                print(f"⏭️ File already exists: {full_path}")

        # If it's a folder
        else:
            if not os.path.exists(full_path):
                os.makedirs(full_path)
                print(f"📁 Created folder: {full_path}")
            else:
                print(f"⏭️ Folder already exists: {full_path}")


if __name__ == "__main__":
    create_structure()