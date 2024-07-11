# Neural Style Transfer (NST)

This project implements image style transfer using pre-trained neural network models. The application allows users to select a style and apply it to an uploaded image through a web interface built with Streamlit.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Project Structure](#project-structure)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RAT1onaloNe/NST_MIPT.git
    cd NST_MIPT
    ```
    Python 3.8 or higher required

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501`.

3. Select a style and upload an image for processing.

## Streamlit share

[Demo](https://nstmipt-nsd9rqtkqtmaknavnb9ymq.streamlit.app/)

## Project Structure

NST_MIPT/
│



├── checkpoints/ # Directory with pre-trained models
│ ├── blue.pth
│ ├── green.pth
│ └── yellow.pth
│
├── styles/ # Directory with style images
│ ├── blue.jpg
│ ├── green.jpg
│ └── yellow.jpg
│
├── app.py # Main Streamlit application file
├── models.py # Model architecture definitions
├── utils.py # Utility functions
├── requirements.txt # Project dependencies
└── README.md # Project description
