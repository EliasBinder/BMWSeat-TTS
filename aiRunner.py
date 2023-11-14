import torch
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import simpleaudio as sa

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

def say(text):
    # Create sound file
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    sf.write("./temp/speech.wav", speech['audio'], samplerate=16000)

    # Play sound file
    wave_obj = sa.WaveObject.from_wave_file('./temp/speech.wav')
    play_obj = wave_obj.play()
    play_obj.wait_done()
