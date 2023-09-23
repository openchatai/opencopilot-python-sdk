from setuptools import setup

setup(
    name="open-copilot",
    version="0.0.0",
    description="",
    long_description="",  # You can provide a long description here
    author="",  # Add your name
    author_email="",  # Add your email
    packages=["open_copilot"],  # Adjust the package name based on your project structure
    install_requires=[
        "httpx>=0.21.2",
        "pydantic>=1.9.2",
        "python>=3.7",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)