#!/usr/bin/env python
# 실행하고 싶으면 python말고 sh test.sh 로 실행
#echo "hello"

for i in 1 2 3 4 5
do
    echo "sample_${i}"
    python 015.py ${i}
done
