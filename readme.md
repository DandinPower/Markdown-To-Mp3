# Text-to-Speech Slides Splitter

This Python script splits a Markdown file containing slides into separate MP3 files, one for each slide. The script uses the Microsoft Azure Text-to-Speech API to generate the audio files.

## Prerequisites

Before running the script, you need to have the following:

- Python 3 installed on your system
- A Microsoft Azure account with access to the Text-to-Speech API
- A .env file in the root directory of the project containing your subscription key and region for the Text-to-Speech API. The file should have the following format:

    ```env
    SPEECH_KEY= 
    SPEECH_REGION=
    ```

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Create a .env file in the root directory of the project with your subscription key and region for the Text-to-Speech API.
3. Install the required Python packages by running `pip install -r requirements.txt` in the root directory of the project.
4. Place your Markdown file containing the slides in the `md` directory.
5. Run the script by executing `python main.py` in the root directory of the project.
6. The script will generate a directory with the same name as your Markdown file (without the extension) in the `mp3` directory. Each slide will be saved as a separate MP3 file in this directory.

## Contributing

If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.