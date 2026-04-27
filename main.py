# 파일이름 :
# 작 성 자 :
import random
hiphop_f = ["Meteor", "Love Love Love","우산","죽일 놈","삐딱하게"]
hiphop_u = ["LOV3","Glendale","포커페이스","25","All Of The Lights"]
rnb_f = ["Square","비도 오고 그래서","Boat","눈,코,입","Beautiful"]
rnb_u = ["왜,왜,왜","텅 빈 밤","개인사","Self Control","White Ferrari"]
ballad_f = ["너의 결혼식","먼지가 되어","그대안의 블루","소주 한잔","심"]
ballad_u = ["그대 내 품에","가리워진 길","기억의 습작","사랑했지만","J에게"]
pop_f = ["save your tears","See you again","This Love","Golden","Stay"]
pop_u = ["Circles","Postman","Whatever","Out of Time","Best Friends"]
indie_f = ["사랑하게 될거야","나무","입춘","주저하는 연인들을 위해","0+0"]
indie_u = ["정면돌파","섬","거울","Huf","일인칭 관찰자 시점"]

genres = ["힙합","알앤비","발라드","팝","인디"]
preference = []
recommended = []

name = input("이름을 입력하세요 : ")
listen_time = float(input("하루 평균 음악 감상 시간을 실수형으로 입력하세요 :"))
print("힙합, 알앤비, 발라드, 팝, 인디 순으로 선호 점수를 1점~10점 사이로 입력하세요 : ")
for i in range(5) :
    score = int(input(f"{genres[i]} 선호 점수를 입력하세요."))
    if score < 1 or score > 10 :
        print("유효하지 않은 점수 입니다. 해당 점수는 0점 처리 됩니다.")
        preference.append(0)
        continue

    preference.append(score)

print(f"입력하신 점수는 {preference} 입니다.")

total = 0

for j in range(len(preference)) :
    total += preference[j]

avg = total/5
print(f"총점 : {total}, 평균 : {avg}")

highest_score = max(preference)
print(f"가장 높은 선호도 점수는 {highest_score} 입니다.")


if preference[0] <= avg :
    song = random.choice(hiphop_f)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)
else :
    song = random.choice(hiphop_u)
    print(f"유명하지 않은 힙합 추천 : {song}")
    recommended.append(song)

if preference[1] <= avg :
    song = random.choice(rnb_f)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)
else :
    song = random.choice(rnb_u)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)

if preference[2] <= avg :
    song = random.choice(ballad_f)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)
else :
    song = random.choice(ballad_u)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)

if preference[3] <= avg :
    song = random.choice(pop_f)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)
else :
    song = random.choice(pop_u)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)

if preference[4] <= avg :
    song = random.choice(indie_f)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)
else :
    song = random.choice(indie_u)
    print(f"유명한 힙합 추천 : {song}")
    recommended.append(song)

answer = input("추천된 다섯 곡을 모두 들어보셨나요? (네/아니오) : ")

if answer == "네" :
    print(f"축하합니다! {name}님에게 '장르올킬상' 을 수여합니다!")

elif answer == "아니오" :
    print("꼭 다 들어 보세요!")

else :
    print("유효하지 않은 답변입니다.")