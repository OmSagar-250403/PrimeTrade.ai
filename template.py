import os

def create_file_structure(project_name):
    # Base directories
    base_dirs = [
        f"{project_name}/data/raw",
        f"{project_name}/data/processed",
        f"{project_name}/data/examples",
        f"{project_name}/notebooks",
        f"{project_name}/src",
        f"{project_name}/tests",
        f"{project_name}/reports/figures"
    ]

    # Base files with content
    base_files = {
        f"{project_name}/.gitignore": "# Add files/directories to ignore\n__pycache__/\n*.pyc\n*.pyo\n*.csv\n*.h5\n*.db\n",
        f"{project_name}/README.md": f"# {project_name}\n\nProject overview and instructions.",
        f"{project_name}/LICENSE": "# Add your license information here.",
        f"{project_name}/requirements.txt": "# Add Python dependencies here.\npandas\nnumpy\nsklearn\nmatplotlib\n",
        f"{project_name}/environment.yml": "# Conda environment file\nname: {project_name}\ndependencies:\n  - python=3.9\n  - pandas\n  - numpy\n  - scikit-learn\n  - matplotlib\n",
        f"{project_name}/setup.py": "# Setup script for packaging\nfrom setuptools import setup, find_packages\n\nsetup(\n    name='{project_name}',\n    version='0.1.0',\n    packages=find_packages(),\n    install_requires=[\n        'pandas',\n        'numpy',\n        'scikit-learn',\n        'matplotlib'\n    ],\n)\n",
        f"{project_name}/Makefile": "# Makefile for automating tasks\ninstall:\n\tpip install -r requirements.txt\n",
        f"{project_name}/src/__init__.py": "# Initialize src module",
        f"{project_name}/tests/__init__.py": "# Initialize tests module",
        f"{project_name}/reports/model_results.md": "# Model Results\n\nAdd model evaluation results here.",
        f"{project_name}/reports/ranking_results.md": "# Ranking Results\n\nAdd ranking analysis here."
    }

    # Create directories
    for directory in base_dirs:
        os.makedirs(directory, exist_ok=True)

    # Create files with content
    for file_path, content in base_files.items():
        with open(file_path, "w") as file:
            file.write(content)

    print(f"Project structure for '{project_name}' created successfully.")

# Run the script
def main():
    project_name = input("Enter the project name: ").strip()
    create_file_structure(project_name)

if __name__ == "__main__":
    main()
