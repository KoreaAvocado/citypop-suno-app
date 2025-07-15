from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_path, wav_path):
    if not os.path.exists(wav_path):
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print("✅ 변환 완료:", wav_path)
    else:
        print("ℹ️ 이미 존재:", wav_path)

