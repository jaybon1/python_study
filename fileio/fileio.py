
# 파일 생성 및 데이터 입력

# mode w는 write 모드
file_editor = open(file="fileio/test.txt", mode="w", encoding="utf-8")

file_editor.write("안녕하세요.")

# 파일을 open 했으면 반드시 close 해주는 것이 좋다.
file_editor.close()

print("작업종료")
