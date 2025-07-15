import numpy as np
import librosa
from pathlib import Path
from music21 import converter, chord

# ==== 1. 파일 경로 ====
file_path = "audio/46bea759.wav"
lyrics_path = "lyrics/Christina_Perri_-_A_Thousand_Years.txt"

# ==== 2. 오디오 불러오기 ====
y, sr = librosa.load(file_path, sr=None, mono=True)

# ==== 3. 템포 추정 ====
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
tempo = float(tempo)

if tempo < 85:
    speed = "slow"
elif tempo < 115:
    speed = "mid-tempo"
else:
    speed = "fast"

print(f"🎵 추정 템포: {tempo:.2f} BPM • {speed}")

# ==== 4. 키(Key) 추출 ====
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
key_index = np.argmax(np.sum(chroma, axis=1))
keys_major = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
detected_key = keys_major[key_index]
print(f"🎼 추정 키: {detected_key} Major")

# ==== 5. 가사 불러오기 ====
lyrics_text = ""
lyrics_file = Path(lyrics_path)
if lyrics_file.exists():
    with open(lyrics_file, "r", encoding="utf-8") as f:
        lyrics_text = f.read().strip()

# ==== 6. 기본 프롬프트 요소 ====
emotion = "emotional, romantic, cinematic"
instruments = "soft piano, cinematic strings"
vocal = "female vocals"
lyrics_theme = "timeless love and waiting"
context = "inspired by romantic movie soundtracks, ideal for wedding scenes or dramatic emotional moments."
language = "English"

# ==== 7. 코드 진행 추정 ====
# wav 파일은 직접 코드 추정 어렵기 때문에 midi 변환 기반 추정 (임시 처리)
chord_progression = "C - G - Am - F"  # 예시. 추후 개선 시 music21.midi 변환 가능

# ==== 8. 프롬프트 생성 ====
short_prompt = (
    f"A {emotion} {speed} pop ballad in {detected_key} Major with {instruments}, "
    f"featuring {vocal}. "
    f"Lyrics about {lyrics_theme}.\n"
    f"Chord progression: {chord_progression}"
)

# ==== 9. 익스클루시브 스타일 강조 프롬프트 ====
exclusive_prompt = f"🎧 Exclusive style: {context}"

# ==== 10. 출력 ====
print("\n🎬 최종 프롬프트:\n", short_prompt)
print(exclusive_prompt)



