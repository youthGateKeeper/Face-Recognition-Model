# 팀명 : 집가고싶다
## 팀원 소개
|   | 이름 | 역할 | GitHub Profile |   | 이름 | 역할 | GitHub Profile |
|:------:|------|------|---------|:------:|------|------|---------|
| <img width="86" alt="image" src="https://github.com/user-attachments/assets/721b6caf-ff8a-41be-880e-aa6b68b32dfb" />| 김민준 | 팀장 | [@KIMsongeul](https://github.com/KIMsongeul)|<img width="86" alt="image" src="https://github.com/user-attachments/assets/90010f5b-b83a-465e-bffb-3f7354442304" />| 최도은 | 부팀장 | [@doeun07](https://github.com/doeun07) |
| <img width="86" alt="image" src="https://github.com/user-attachments/assets/0b40ee99-a53d-490c-aa66-71d13fed6d44"/>| 구건모 | 프로그래머 | [@rra30](https://github.com/rra30) |<img width="78" height="76" alt="image" src="https://github.com/user-attachments/assets/f5935e93-7d70-4728-b6b7-bfaad00222c4" />| 정혜양 | 엔지니어 | [@xom1p](https://github.com/xom1p) |

---

# 프로젝트 개요
## 프로젝트 이름 : 감정친구
### 프로젝트 명 선정 이유 
청소년들이 ai에게 감정을 자유롭게 나눌 수 있는 친구처럼 다가가는 챗봇이자 감정을 인식해주기 때문이다. 
## 문제인식
![image](https://github.com/user-attachments/assets/83b7a6c2-fa96-468d-9998-49dc455620da)<br>
기존 심리상담은 전문가가 부족한 지역에서는 접근이 어려워 상담을 받지 못하는 문제가 있습니다. 또한, 대기 시간이 길어 즉각적인 도움이 필요한 상황에서는 적시에 지원을 받기 어려운 점이 있습니다. 상담사와의 심리적 거리감도 큰 장애물로 작용하여, 일부 사람들은 자신의 감정을 진지하게 털어놓는 데 어려움을 겪습니다. 이러한 문제로 상담의 효과가 저조할 수 있으며, 상담을 계속할 동기가 부족해질 수 있습니다. 결과적으로, 상담 서비스의 접근성과 실효성에 한계가 있는 상황이 발생합니다.<br>

K-SDGs 목표 3: 모두를 위한 건강한 삶 보장 및 웰빙 증진<br>
K-SDGs 목표 4: 포용적이고 공평한 양질의 교육 보장<br>
K-SDGs 목표 11: 포용적이고 안전하며 지속 가능한 도시 조성이 지켜지지 않고 있다고 생각합니다.<br>

위와 같은 문제를 해결하기 위해서 상담센터를 직접 방문하지 않아도 쉽고 편하게 접근할 수 있는 사이트를 만들게 되었습니다.
## 프로젝트 개발 이유
표정을 통해 무의식적으로 드러난 감정을 인식하면 현재 기분을 객관적으로 파악할 수 있습니다. AI 챗봇은 자연어 처리와 감정 인식 기술을 활용해 슬픔, 분노, 불안 등 청소년의 감정 상태를 분석합니다. 이에 맞는 조언이나 위로를 제공하며, 비판 없는 환경을 조성해 편안하게 감정을 표현하도록 돕습니다. 이러한 접근은 청소년들에게 정서적 안전감을 주고, 진솔한 대화를 가능하게 합니다. 결과적으로, 감정 이해와 문제 해결 능력을 키우는 데 기여합니다.

## 주요 기능 :
### - 웹캠을 통해 표정으로 사용자 감정 인식 가능. <br>
![image](https://github.com/user-attachments/assets/b0ad008d-226e-4e0c-be4b-72cd39f8a119) <br>
### - Gemini-Bot을 활용하여 사이트에서 대화가 가능한 채팅 시스템
<img width="730" alt="image" src="https://github.com/user-attachments/assets/7655037b-2d37-4fb3-8817-daecc0dbfe9c"/><br>

## 기술스택
- 프론트엔드: php , JavaScript
- AI백엔드: Python

---
  
# 프로젝트 실행 방법
## 가상환경 및 필요한 패키지 설치[VSC Terminal]
```
conda create --name Locals python==3.12.0 anaconda 
conda activate Locals
pip install --upgrade --user pip
pip install openvino==2024.1.0
pip install openvino-dev==2024.1.0
pip install opencv-python==4.9.0.80
pip install ipywidgets==8.1.2
pip install tensorflow==2.16.1
pip install streamlit 
pip install google-generativeai #gemini AI 사용을 위한 패키지
```
## 파일 구조
```
AI/
├── model/
│   └──age-gender-recognition-retail-0013.bin 
│   └──age-gender-recognition-retail-0013.xml # 나이,성별 인식
│   └──emotions-recognition-retail-0003.bin
│   └──emotions-recognition-retail-0003.xml # 감정 인식 
│   └──face-detection-adas-0001.bin
│   └──face-detection-adas-0001.xml # 사람얼굴 인식
├── app.py
├── utils.py
└── Collection.py
```

## 코드 참조 
https://github.com/youthGateKeeper/Face-Recognition-Model/blob/main/AI/app.py <br>
https://github.com/youthGateKeeper/Face-Recognition-Model/blob/main/AI/utils.py <br>
https://github.com/youthGateKeeper/Face-Recognition-Model/blob/main/AI/Collection.py <br>

## 실행영상
[![testvideo](http://img.youtube.com/vi/CuBg78KK1QM/0.jpg)](https://youtu.be/CuBg78KK1QM=0s) 

---

## 추후개발 사항
- Web AI연동
- 프롬포트 자동작성
- 스스로 작성 가능 일기 기록페이지
- 에러 수정 및 최적화
