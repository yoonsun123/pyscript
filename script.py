import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/ly._.sun/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#8EFFEC"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이윤선")
write("description", "대구 거주, 07년생")
write("button", "인스타그램 방문하기")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "mbti": "ENTP",
  "좋아하는 것": "보석, 늦은 오후 감성, 잘생긴 외국인",
  "취미": "그림 그리기, 팝송 듣기, 테니스, 유튜브로 영화 리뷰 정주행 하기, 망상하기",
  "버킷 리스트 Top 3": "서핑 배우기, 스카이 다이빙 하기, 100억 모으기"
}
information(informations)