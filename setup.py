# setup.py 
import subprocess

# Install Python packages from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Download spaCy model
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

# Download NLTK resources
subprocess.run(["python", "-m", "nltk.downloader", "words"])
subprocess.run(["python", "-m", "nltk.downloader", "punkt"])
subprocess.run(["python", "-m", "nltk.downloader", "averaged_perceptron_tagger"])
subprocess.run(["python", "-m", "nltk.downloader", "universal_tagset"])
subprocess.run(["python", "-m", "nltk.downloader", "wordnet"])
subprocess.run(["python", "-m", "nltk.downloader", "brown"])
subprocess.run(["python", "-m", "nltk.downloader", "maxent_ne_chunker"])
