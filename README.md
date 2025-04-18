# 오늘 뭐 먹노?
#### 경주 내 음식점 검색 및 추천 서비스 입니다.
![오늘 뭐 먹노? 배너](https://github.com/user-attachments/assets/9c7a4dcc-4666-4cac-bebc-71691a1f5bc5)

## 📚 기술 스택
|                |NAME                          |
|----------------|-------------------------------|
|Language         |`JavaScript`|
|Styling     |`CSS`|
|Framework     |`Express.js`|
|Template Engine     |`EJS`|
|Database     |`Microsoft SQL Server (Azure)`|
|Authentication     |`Passport.js`, `Bcrypt`|
|Session Management     |`Express-session`|
|Server     |`Node.js`|
|API     |`Kakao Map API`|
|IDE     |`VScode`|

## ✅ 사전 요구사항
이 프로젝트를 실행하기 위해서는 아래의 환경이 필요합니다:

### 사전 설치
- Node.js (v14 이상)
- npm 또는 yarn
- Microsoft SQL Server

### 외부 API
- 카카오 개발자 계정 및 API 키
- 공공데이터 포털에서 경상북도 경주시_경주문화관광_메뉴별음식점 검색후 활용 신청 및 API키 발급

### 발급받은 데이터를 json 파일로 만든후 MSSQL에 데이터 삽입
### 유저 더미 데이터 MSSQL에 데이터 삽입

## 🖥️  어플리케이션 실행 (로컬 환경)
### 1. 프로젝트 Clone
```
git clone https://github.com/JSH0905/Today-Restaurant.git
```

### 2. 프로젝트 이동
```
cd Today-Restaurant
```

### 3. 의존성 설치

```
npm install
```

### 4. .env 파일 생성 후 내용 작성

```
DB_SERVER=your_db_server
DB_USER=your_db_user
DB_PW=your_db_password
DB_NAME=your_db_name
DB_PORT=your_db_port
SESSION_SECRET=your_session_secret
```

## 🌟 서비스 기능
### 메인화면
메인화면에서 한식, 일식, 양식, 카페 총 4가지의 카테고리에 대해서 각각 5개의 음식점을 랜덤하게 보여줍니다.

<img width="1920" src="https://github.com/user-attachments/assets/95fbd25c-f895-47cb-bd39-912e0fa9ca7a" />
<img width="1920" src="https://github.com/user-attachments/assets/783ad9b0-2e9f-4ca4-a422-099f554b61f3" />

### 카테고리별 음식점 조회 
음식점 목록 페이지 우측 드롭다운 버튼을 통해서 선택한 카테고리의 음식점의 목록을 조회할 수 있습니다. 

<img width="1920" src="https://github.com/user-attachments/assets/be893c84-df8f-47af-a804-df06a37bd0ef" />  
<img width="1920" src="https://github.com/user-attachments/assets/540169d2-1856-4c07-b755-501761590c36" />

### 음식점 검색 기능
메인페이지 또는 목록페이지의 검색창에 찾고자하는 음식점 이름을 입력하여 검색어를 포함하는 음식점을 조회할 수 있습니다.
<img width="1920" src="https://github.com/user-attachments/assets/a63c76ce-5412-45d7-9f7f-23bfba4cf6fd" />


### 음식점 상세 정보 조회
음식점의 영업시간, 추가 사진 등의 상세 정보를 조회할 수 있습니다. 로그인을 완료한 유저라면 좋아요를 누르거나 취소할 수 있습니다.

<img width="1920" src="https://github.com/user-attachments/assets/a5fab8c9-7540-44a7-82b1-ed57b14dcf7c" />
<img width="1920" src="https://github.com/user-attachments/assets/10cbf265-3a39-4b95-98d6-b472f9532695" />


## 🎥 Demo
https://www.youtube.com/watch?v=rnBn79C03kM

## 🧑🏻‍💻 팀원 소개
| 정성훈 | 윤용현 | 이태우 |
| ------------ | ------------- | ------------- |
| <p align="center"> 팀장 </p> | <p align="center"> 팀원 </p> | <p align="center"> 팀원 </p> |
| <p align="center"> 프로젝트 매니저 <br/> 백엔드 개발 <br/> 프론트엔드 개발 </p> | <p align="center"> 백엔드 개발 </p> | <p align="center"> 프론트엔드 개발 </p> |
