import librosa

file_path = "Christina Perri - A Thousand Years.m4a"

y, sr = librosa.load(file_path)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

if tempo < 90:
    speed = "slow"
elif tempo < 110:
    speed = "mid-tempo"
else:
    speed = "fast"

prompt = f"A {speed} retro citypop track with dreamy synths and mellow bassline."
print(f"\n🎧 SUNO 프롬프트:\n{prompt}")
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)