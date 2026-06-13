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

famous_lists = [hiphop_f, rnb_f, ballad_f, pop_f, indie_f]
unfamous_lists = [hiphop_u, rnb_u, ballad_u, pop_u, indie_u]

preference = []
recommended = []

all_users_data = []

def calculate_average(scores) :
    total = sum(scores)
    avg = total / len(scores)
    return avg


def get_preferences() :
    global name
    name = input("이름을 입력하세요 : ")
    while True :
        try :
            listen_time = float(input("하루 평균 음악 감상 시간을 실수형으로 입력하세요 :"))
            break
        except ValueError :
            print("실수형으로 입력하세요.")

    print("힙합, 알앤비, 발라드, 팝, 인디 순으로 선호 점수를 1점~10점 사이로 입력하세요 : ")
    for i in range(5) :
        while True :
            try :        
                score = int(input(f"{genres[i]} 선호 점수를 입력하세요."))
                if score < 1 or score > 10 :
                    print("유효하지 않은 점수 입니다. 1~10 사이로 다시 입력하세요.")
                    continue
                else :
                    preference.append(score)
                    break    
            except ValueError :
                print("숫자만 입력하세요. 해당 점수는 0점 처리합니다.")
                preference.append(0)
                break
    print(f"입력하신 점수는 {preference} 입니다.")

def recommend_songs(avg) :
    global recommended

    for i in range(5) :
        if preference[i] <= avg :
            song = random.choice(famous_lists[i])
            print(f"유명한 {genres[i]} 추천 : {song}")
        else :
            song = random.choice(unfamous_lists[i])
            print(f"유명하지 않은 {genres[i]} 추천 : {song}")

        recommended.append(song)

print("=== 음악 추천 프로그램 시작 ===")
try :
    with open("playlist_data.txt", "r", encoding = "utf-8") as file :
        print("가존에 저장된 플레이리스트 데이터를 확인했습니다.")
except FileNotFoundError :
    print("저장된 데이터 파일이 없습니다. 새로 기록을 시작합니다.")

while True :
    print("\n1. 음악 추천 받기")
    print("2. 프로그램 종료/저장")
    print("3. 전체 사용자 기록 보기")

    choice = input("원하시는 메뉴의 번호를 입력하세요 :")

    if choice == "1" :
        preference.clear()
        recommended.clear()

        get_preferences()
        avg = calculate_average(preference)
        print(f"총점 : {sum(preference)}, 평균 : {avg}")
        print(f"가장 높은 선호도 점수는 {max(preference)} 입니다.")

        recommend_songs(avg)
        while True :
            print(f"현재 추천된 플레이리스트 : {recommended}")
            answer = input("추천된 다섯 곡을 모두 들어보셨나요? (네/아니오) :")

            if answer == "네" :
                print(f"축하합니다! {name} 님에게 '장르올킬상' 을 수여합니다!")
                custom_song = input("장르올킬상 혜택! 추가하고 싶은 곡 제목을 입력하세요 : ")
                recommended.append(custom_song)

                print(f"{name} 님의 최종 플레이리스트는 {recommended} 입니다.")

                user_record = [name, avg, recommended.copy()]
                all_users_data.append(user_record)
                break

            elif answer == "아니오" :
                print("\n들어보지 않은 장르의 노래를 다시 추천합니다.")
                unheard_genre = input(f"어떤 장르를 안 들어 보셨나요? ({', '.join(genres)})) : ").strip()

                if unheard_genre in genres :
                    idx = genres.index(unheard_genre)
                    current_song = recommended[idx]

                    if preference[idx] <= avg: 
                        song_pool = famous_lists[idx]
                    else :
                        song_pool = unfamous_lists[idx]

                    available_songs = [song for song in song_pool if song!= current_song]
                    
                    if available_songs :
                        new_song = random.choice(available_songs)
                        recommended[idx] = new_song
                        print(f"\n [{unheard_genre}] 장르의 곡이 '{current_song}'에서 '{new_song}' (으)로 변경되었습니다.")              
                    else :
                        print(f"\n {unheard_genre} 장르에는 더 이상 변경할 수 있는 다른 곡이 없습니다.")
                else :
                    print("\n 올바른 장르 이름을 입력하세요. 처음으로 돌아갑니다.")        
            else :
                print("유효하지 않은 답변입니다.")

    elif choice == "2" :
        print("데이터를 텍스트 파일로 저장합니다.......")
        with open("playlist_data.txt", "w", encoding = "utf-8") as file :
            for user in all_users_data :
                songs_str = ", ".join(user[2])
                file.write(f"이름 : {user[0]}, 평균점수 : {user[1]:.2f}, 플레이리스트 {songs_str}\n")
        print("저장이 완료되었습니다. 프로그램을 종료합니다.")
        break
    
    elif choice == "3" :
        print("\n---전체 사용자 추천 기록---")
        if not all_users_data :
            print("아직 기록된 사용자가 없습니다.")
        else :
            for user_id in range(len(all_users_data)) :
                user_info = all_users_data[user_id]
                print(f"[{user_id + 1}번 사용자] {user_info[0]}님의 평균 점수 : {user_info[1]:.2f}")
                print("추천된 곡 목록 :")

                user_playlist = user_info[2]
                for song in user_playlist :
                    print(f"   -{song}")
        print("-"*20)
    else :
        print("잘못된 메뉴 번호입니다. 다시 입력하세요.")