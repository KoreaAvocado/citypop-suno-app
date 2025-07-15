import whisper

# Whisper 모델 불러오기
model = whisper.load_model("small")

# 분석할 M4A 파일
file_path = "Christina Perri - A Thousand Years.m4a"

# 자막 추출
result = model.transcribe(file_path)

# 결과 출력
print("\n🎤 추출된 가사 (앞부분):\n")
print(result["text"][:500])  # 앞부분 500자만 미리보기

