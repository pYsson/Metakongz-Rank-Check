# Metakongz-Rank-Check
## Description
- 디스코드 봇 명령어를 통해 메타콩즈 랭킹 확인
  - ranking.json 파일을 활용하여 메타콩즈 랭킹 및 스코어 측정
  - 해당 번호의 메타콩즈 이미지 표시

## Installation
1. 레포지토리 클론  
```https://github.com/pYsson/Metakongz-Rank-Check.git```
2. 필요한 라이브러리 설치  
```pip install -r requirements.txt```
3. 디스코드 봇 [TOKEN](https://discord.com/developers/docs/intro) 발급

## How to run your Bot
1. mkRanking.py 파일 실행  
```python3 mkRanking.py``` or ```python mkRanking.py```  

    1-1. mkRanking.py 파일 내 디스코드 봇 토큰 입력  
2. 봇 토큰 입력  
<img width="776" alt="스크린샷 2022-01-16 오전 12 42 16" src="https://user-images.githubusercontent.com/97378861/149627875-96bd2d58-2d9e-47b0-9bca-6d4c0f2e9299.png">  

- 서버 내 백그라운드 실행하고 싶은 경우 (봇 토큰 미리 입력 필수)  
```nohup python3 floorcheck.py &``` or ```nohup python floorcheck.py &```

## Command
- !rank 콩즈-번호  
ex) ```!rank 1```  
<img width="407" alt="스크린샷 2022-01-16 오전 12 44 50" src="https://user-images.githubusercontent.com/97378861/149627941-eeb4e91a-a888-4df1-be88-6af569c96df9.png">  
