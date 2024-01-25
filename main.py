# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.
import sys
import assemblyai as aai
audio_file = sys.argv[1]
# Replace with your API key
aai.settings.api_key = "a2474478613f46259c907bc54ac97f6c"

# URL of the file to transcribe
FILE_URL = audio_file
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript.text)
