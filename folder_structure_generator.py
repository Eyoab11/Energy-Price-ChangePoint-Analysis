# folder_structure_generator.py
import os
import pathlib

# --- Configuration ---
# The root name of your project. The script will create a folder with this name.
PROJECT_NAME = "Brent-Event-Impact-Analysis"

# Define the folder structure as a dictionary.
# Keys are directory names, and values are lists of subdirectories or files.
# Use an empty list [] for an empty directory.
# Use a list of strings for subdirectories.
# Use None as a value to create a placeholder file (e.g., .gitkeep).
STRUCTURE = {
    "data": {
        "01_raw": [".gitkeep"],  # For the original, immutable data
        "02_processed": [".gitkeep"],  # For cleaned and preprocessed data
        "03_external": [".gitkeep"],  # For the researched events CSV
        "04_models": [".gitkeep"], # For saved model objects or traces
    },
    "notebooks": {
        "01_data_ingestion_and_eda.ipynb": None,
        "02_bayesian_modeling.ipynb": None,
        "03_results_interpretation.ipynb": None,
        "archive": [".gitkeep"], # For old or experimental notebooks
    },
    "src": {
        "__init__.py": None,
        "data": {
            "__init__.py": None,
            "make_dataset.py": "# Script to download or generate data",
        },
        "features": {
            "__init__.py": None,
            "build_features.py": "# Script to process data and create features (e.g., log returns)",
        },
        "models": {
            "__init__.py": None,
            "change_point_model.py": "# Main PyMC3 model definition",
            "predict_model.py": "# Script to make predictions or run analysis",
        },
        "visualization": {
            "__init__.py": None,
            "visualize.py": "# Scripts for creating static plots and charts",
        },
        "utils": {
            "__init__.py": None,
            "helpers.py": "# Utility functions used across the project"
        }
    },
    "dashboard": {
        "backend_flask": {
            "app.py": "# Main Flask application file",
            "requirements.txt": "Flask\n",
            "api": {
                "__init__.py": None,
                "routes.py": "# API routes for serving data"
            }
        },
        "frontend_react": {
            "README.md": "# Instructions to set up the React frontend",
            "package.json": "{\n  \"name\": \"dashboard-frontend\",\n  \"version\": \"0.1.0\"\n}",
            "src": [".gitkeep"],
            "public": [".gitkeep"]
        },
    },
    "reports": {
        "interim_report.md": "# Outline for the interim report",
        "final_report.md": "# Draft for the final blog post or PDF report",
        "figures": [".gitkeep"], # For exported plots, charts, and diagrams
    },
    "tests": {
        "__init__.py": None,
        "test_data.py": None,
        "test_features.py": None,
    },
    ".gitignore": "*.pyc\n__pycache__/\n.env\ndata/01_raw/\ndata/02_processed/\n*.csv\n*.pkl",
    "README.md": f"# {PROJECT_NAME}\n\nProject to analyze the impact of major events on Brent oil prices.",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\npymc\nflask\nscikit-learn\n",
    "config.yaml": "data:\n  raw_path: 'data/01_raw/brent_prices.csv'\n  events_path: 'data/03_external/key_events.csv'\n"
}

def generate_structure(base_path, structure_dict):
    """
    Recursively creates folders and files based on a dictionary.
    """
    for name, content in structure_dict.items():
        current_path = base_path / name
        if isinstance(content, dict):  # It's a directory with content
            current_path.mkdir(exist_ok=True)
            print(f"Created directory: {current_path}")
            generate_structure(current_path, content)
        elif isinstance(content, list): # It's a directory with sub-items
            current_path.mkdir(exist_ok=True)
            print(f"Created directory: {current_path}")
            for item in content:
                (current_path / item).touch()
                print(f"  - Created file: {current_path / item}")
        else:  # It's a file
            if not current_path.exists():
                with open(current_path, "w") as f:
                    if content is not None:
                        f.write(content)
                print(f"Created file: {current_path}")

if __name__ == "__main__":
    project_path = pathlib.Path(PROJECT_NAME)
    if project_path.exists():
        print(f"Project directory '{PROJECT_NAME}' already exists. Aborting.")
    else:
        project_path.mkdir()
        print(f"--- Creating project structure for '{PROJECT_NAME}' ---")
        generate_structure(project_path, STRUCTURE)
        print("\n--- Folder structure generated successfully! ---")
        print(f"Navigate to your project folder with: cd {PROJECT_NAME}")