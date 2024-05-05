from setuptools import find_packages, setup

setup(
    name="solution",
    version="0.1",
    description="Starter code.",
    author="Student",
    packages=find_packages(),
    install_requires=[
            "numpy",
            "pandas",
            "scikit-learn",
            "pytest",
            "requests",
            "fastapi==0.63.0",
            "uvicorn",
            "gunicorn",
            "flake8",
            "ruff",
            "mangum"
    ]

)
