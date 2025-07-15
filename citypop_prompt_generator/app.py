import streamlit as st
from pathlib import Path
import librosa
import numpy as np
from music21 import converter, chord

import streamlit as st
from pathlib import Path

# 제목
st.title("🎧 Suno AI 프롬프트 자동 생성기")

# 파일 업로드
uploaded_file = st.file_uploader("🎵 WAV 오디오 파일 업로드", type=["wav"])
lyrics_text = st.text_area("📝 가사 입력", "")

if uploaded_file and lyrics_text:
    with st.spinner("분석 중..."):
        # 파일 저장
        file_path = Path("temp_audio.wav")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # 오디오 로드 및 분석
        y, sr = librosa.load(file_path, sr=None, mono=True)
        tempo = float(librosa.beat.tempo(y=y, sr=sr)[0])
        speed = "slow" if tempo < 85 else "mid-tempo" if tempo < 115 else "fast"

        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = np.argmax(np.sum(chroma, axis=1))
        keys_major = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        detected_key = keys_major[key_index]

        # 코드 진행 추출
        score = converter.parse(file_path)
        chords = score.chordify()
        progression = []
        for c in chords.recurse().getElementsByClass('Chord'):
            progression.append(c.pitchedCommonName)
        chord_progression = " - ".join(progression[:4])  # 앞 4개만

        # 프롬프트 출력
        st.subheader("🎬 프롬프트 결과")
        st.write(f"""
**A emotional, romantic, cinematic {speed} pop ballad in {detected_key} Major**  
with soft piano, cinematic strings, featuring female vocals.  
Lyrics about **{lyrics_text.strip()}**  
**Chord progression**: {chord_progression}  
🎧 *Exclusive style: inspired by romantic movie soundtracks, ideal for wedding scenes or dramatic emotional moments.*
        """)

