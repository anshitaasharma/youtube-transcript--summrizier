# youtube-transcript--summrizier

# YouTube Video Summarizer

A web application built with Flask that summarizes the transcript of a YouTube video.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)

## Description

The YouTube Video Summarizer is a web application that allows users to input the URL of a YouTube video. The application then fetches the transcript of the video, summarizes it using a pre-trained model, and presents the summarized text to the user.

## Features

- Input a YouTube video URL.
- Retrieve the video transcript using the YouTube Transcript API.
- Summarize the transcript using a pre-trained transformer model.
- Display the summarized text to the user.
- Responsive and user-friendly web interface.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Amogha-k/youtube-transcript-summarizer.git
   
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python main.py
   ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Enter the YouTube video URL in the provided form and click "Submit."

4. The summarized text of the video transcript will be displayed on the page.

## Technologies

- Flask
- YouTube Transcript API
- Transformers library

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the original repository.

