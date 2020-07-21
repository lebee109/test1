#커맨드라인에서 인수 입력받기
# 015.py
import sys

#print(dir(sys))

#print(sys.argv)

print(f"hello {sys.argv[1]}")

"""
python 015.py bio 하면 {}에 bio 출력
input은 사용자가 입력할때까지 기다려야되는데
이거는 자동으로 됨 -> 사용하면 좋음(출력값 바로 주는거)
"""
