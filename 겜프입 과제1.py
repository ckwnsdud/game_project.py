import time
import random
import os


#글자 한글자씩 출력해주는 함수
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.08)

#일정 돌아가는 개월
total_select_month = 0

#일주일
total_week = 1

#스탯
total_brain = 10
total_health = 50
total_stress = 0
total_code = 0
total_money = 50

#교수님 호감도
total_proheart1 = 0
total_proheart2 = 0

#스케쥴 리스트 생성
scheduleList = []

#일정 증감
def schedule_UpDown():
    global total_brain, total_code, total_health, total_money, total_stress, scheduleList, total_select_month
    os.system('cls')
    for i in range(0,3):
        if scheduleList[i] == '알바 가기':
            for week in range(1,5):
                m, h, s = week_UpDown1()
                print_slow(f"{week}주째...  알바를 하면서...  소지금이 {m}원 올랐다!  체력이{h} 올랐다!  스트레스가 {-s} 내렸다!  \n\n")

        elif scheduleList[i] == '운동 하기':
            for week in range(1,5):
                h, s = week_UpDown2()
                print_slow(f"{week}주째...  운동을 하면서...  체력이 {h} 올랐다!  스트레스가 {-s} 내렸다!  \n\n")

        elif scheduleList[i] == '일반 공부':
            for week in range(1,5):
                b, s, h = week_UpDown3()
                print_slow(f"{week}주째...  일반 공부를 하면서...  지능이 {b} 올랐다!  스트레스가 {s} 올랐다!  체력이 {-h} 내렸다!  \n\n")

        elif scheduleList[i] == '코딩 공부':
            for week in range(1,5):
                c, h, s = week_UpDown4()
                print_slow(f"{week}주째...  코딩 공부를 하면서...  코딩 실력이 {c} 올랐다!  체력이 {-h} 내렸다!  스트레스가 {s} 올랐다!\n\n")
            
        elif scheduleList[i] == '재밌게 놀기':
            for week in range(1,5):
                m, h, s = week_UpDown5()
                print_slow(f"{week}주째...  놀면서...  소지금이 {m}원 내렸다!  체력이 {h} 올랐다!  스트레스가 {-s} 내렸다!\n\n")


        #일정을 총 몇달 돌렸는지 확인하는 변수
        total_select_month += 1

    #메인 화면으로 돌아가기 
    main_menu()
    
    

#일주일단위로 한달 반복



#알바 가기의 일주일단위 능력치 증감
def week_UpDown1():
    plus1 = money_RandomUp()
    plus2 = health_RandomUp()
    plus3 = stress_RandomDown()
    return plus1, plus2, plus3 

#운동 하기의 일주일단위 능력치 증감 
def week_UpDown2():
    plus1 = health_RandomUp()
    plus2 = stress_RandomDown()
    return plus1, plus2

#일반 공부의 일주일단위 능력치 증감
def week_UpDown3():
    plus1 = brain_RandomUp()
    plus2 = stress_RandomUp()
    plus3 = health_RandomDown()
    return plus1, plus2, plus3

#코딩 공부의 일주일단위 능력치 증감
def week_UpDown4():
    plus1 = code_RandomUp()
    plus2 = health_RandomDown()
    plus3 = stress_RandomUp()
    return plus1, plus2, plus3

#재밌게 놀기의 일주일단위 능력치 증감
def week_UpDown5():
    plus1 = money_RandomDown()
    plus2 = health_RandomUp()
    plus3 = stress_RandomDown()
    return plus1, plus2, plus3

#스탯 랜덤 증가
def brain_RandomUp():
    global total_brain
    if 0 <= total_brain <=999:
        plus = random.randint(1,5)
        total_brain += plus
        return plus
    
def health_RandomUp():
    global total_health
    if total_health >0:
        plus = random.randint(1,5)
        total_health += plus
        return plus
    elif total_health <= 0:
        death()

def stress_RandomUp():
    global total_stress
    plus = random.randint(1,5)
    if total_stress < 0:
        fix_stress()
        total_stress += plus
        return plus
    elif total_stress + plus >= 100:
        death()
    else :
        total_stress += plus
        return plus

def code_RandomUp():
    global total_code
    if 0 <= total_code <= 999:
        plus = random.randint(1,5)
        total_code += plus
        return plus
    
def money_RandomUp():
    global total_money
    if total_money >=0:
        plus = random.randint(1,5)
        total_money += plus
        return plus
        
#스탯 랜덤 감소
def brain_RandomDown():
    global total_brain
    if 0 <= total_brain <=999:
        minus = random.randint(-5,-1)
        total_brain += minus
        return minus
    
def health_RandomDown():
    global total_health
    minus = random.randint(-5,-1)
    if total_health + minus >0:
        total_health += minus
        return minus
    elif total_health + minus <= 0:
        death()

def stress_RandomDown():
    global total_stress
    minus = random.randint(-5,-1)
    if total_stress + minus < 0:
        fix_stress()
        total_stress += minus
        return minus
    elif total_stress + minus >= 100: 
        death()
    else :
        total_stress += minus
        return minus
    
def code_RandomDown():
    global total_code
    if 0 <= total_code <= 999:
        minus = random.randint(-5,-1)
        total_code += minus
        return minus
    
def money_RandomDown():
    global total_money
    minus = random.randint(-5,-1)
    if total_money + minus < 0:
        fix_money()
        total_money += minus
        return minus
    elif total_money + minus >= 0:
        total_money += minus
        return minus
    
    #소지금이 0원 이하로 내려가지 않게 하는 코드
def fix_money():
    global total_money
    total_money = 0

#스탯 증감들
def brain(amount):
    global total_brain
    if 0 <= total_brain <= 999:
        total_brain += amount

def health(amount):
    global total_health
    if total_health + amount >0:
        total_health += amount
    elif total_health + amount <= 0:
        death()

def stress(amount):
    global total_stress
    if total_stress + amount < 0:
        fix_stress()
    elif total_stress + amount >=0:
        total_stress += amount
        if total_stress >= 100: 
            death()
    #스트레스가 0이하로 내려가지 않게 하는 코드
def fix_stress():
    global total_stress
    total_stress = 0

    
def code(amount):
    global total_code
    if 0 <= total_code <= 999:
        total_code += amount
    

def money(amount):
    global total_money
    if total_money >=0:
        total_money += amount

    #교수님 호감도 증감

    #박교수님 호감도
def proheart1():
    global total_proheart1
    if total_proheart1 >= 0:
        plus1 = random.randint(1, 5)
        return plus1

    #김교수님 호감도
def proheart2():
    global total_proheart2
    if total_proheart2 >= 0:
        plus2 = random.randint(5, 10)
        return plus2

    #게임 진행하는 코드
def main():
    start_game()
    choice = input("< 시작하기(y)\n")

    if (choice == 'y' or 'Y'):
        start_intro()
        time.sleep(1)
        
        main_menu()
    else:
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
        print_slow(" 시작하기 싫으세요?\n")
        main()

    #스트레스 100이상일때 & 체력0 이하될때 게임오버
def death():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
    print_slow(
        "준영이는 스트레스로 병에 걸려 생을 마감했습니다...\n"+
        "\n"+
        "농담이고요. 당신이 준영이를 혹사시켜서 자퇴했습니다.\n"+
        "\n"+
        "하하 이것도 농담이에요. 준영이는 안좋은 선택을 했어요. 당신, 때문에.\n"+
        "\n"+
        "이거 다 거짓말인거 아시죠? 아무튼 준영이는 더 이상 무리 ㅠ3ㅠ\n"+
        "\n"+
        "다음에는 열심히 해보세요 ^_^. 당신의 이야기는 여기까지. 바이바이")
    exit()

  #게임시작프린트
def start_game():
    os.system('cls')
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.15)
    print("    ■■■■■■■■      ■■■■■■■              ■■■■■■■■        ■■■■■■■  ")
    print("    ■                                ■              ■                                  ■  ")
    print("    ■                                ■              ■                                  ■  ")
    print("    ■                                ■              ■                                  ■  ")
    print("    ■■■■■■■■                  ■              ■■■■■■■■                    ■  ")
    print("                       ■■■■■■■■■■                                 ■■■■■■■■■")
    print("  ■■■■■■■■■■     ■                      ■■■■■■■■■■■      ■             ")
    print("          ■               ■                                ■                ■             ")
    print("          ■               ■                                ■                ■             ")
    print("          ■               ■■■■■■■                    ■                ■■■■■■■ ")
    print("\n")
    print("  ■■■■■■    ■      ■          ■                ■        ■                          ")               
    print("            ■    ■      ■          ■          ■■■■■■■  ■       ■■■■■■     ■")
    print("            ■    ■      ■          ■              ■■■      ■            ■          ■")
    print("            ■    ■      ■■■■■■■            ■      ■    ■■■■      ■    ■■■■")
    print("  ■■■■■■■■■      ■          ■            ■      ■    ■          ■■■        ■")
    print("  ■              ■      ■          ■              ■■■      ■      ■■      ■■    ■")
    print("  ■              ■      ■■■■■■■                          ■                        ■")
    print("  ■              ■                                  ■■■■■■            ■■■■■■■  ")
    print("  ■■■■■■    ■                                            ■            ■          ■  ")
    print("                  ■    ■■■■■■■■■                      ■            ■          ■  ")
    print("                                                                ■            ■■■■■■■  ")

    print("♡■■■■■■■■■♡♡■■■■■■■■■♡♡♡■■■■■■♡■♡♡■♡♡■■■■■■■■■♡")
    print("♡♡♡■♡♡♡■■♡♡♡♡♡♡♡♡♡♡■■♡♡♡♡♡♡■♡♡♡■♡♡■♡♡■■♡♡♡♡♡♡♡♡")
    print("♡♡♡■♡♡♡■■♡♡♡■■■■■■■■■♡♡♡♡♡♡■■■■■♡♡■♡♡■■■■■■■■■♡")
    print("♡♡♡■♡♡♡■■♡♡♡■■♡♡♡♡♡♡♡♡♡♡♡♡■■■♡♡■♡♡■♡♡■■♡♡♡♡♡♡♡♡")
    print("♡♡♡■♡♡♡■■♡♡♡■■♡♡♡♡♡♡♡♡♡♡♡■■♡■■■■♡♡■♡♡■■♡♡♡♡♡♡♡♡")
    print("♡■■■■■■■■■♡♡■■■■■■■■■♡♡♡■■♡♡♡■♡■♡♡■♡♡■■■■■■■■■♡")
    print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡■■♡♡♡♡♡♡♡♡♡■■■■■■■■♡♡♡♡♡♡♡♡♡♡♡♡")
    print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡■■♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡■♡♡♡♡♡♡♡♡♡♡♡♡")
    print("■■■■■■■■■■■■■■■■■■■■■■♡♡♡♡♡♡♡♡♡♡♡♡■♡■■■■■■■■■■■")
    print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡■♡♡♡♡♡♡♡♡♡♡♡♡")                                                                          
    print_slow("     ver. 교수님과의 러브러브 만남\n")
    
    #인트로
def start_intro():
    os.system('cls')
    print_slow( 
        "준영이 : 아 큰일났다 망했다 아 시험 어떡하지 \n"+
        "\n"+
        "*수뭉이요정* : 힘들어하는 준영이의 목소리를 듣고 요정 등장 ! \n"+
        "\n"+
        "준영이 : 아 깜짝아 아 뭐야 아 이게 뭐지 벌레인가 \n"+
        "\n"+
        "*수뭉이요정* : 준영아! 걱정마! 내가 첫날로 시간을 되돌려줄게 \n"+
        "\n"+
        "준영이 : 아 진짜 아 진짜 그러면 좋겠다 \n"+
        "\n"+
        "*수뭉이요정* : 웅 ! \n"+
        "\n"+
        "준영이 : 어어? 갑자기 머리가 (시야가 핑 돈다)\n"+
        "\n"+
        "준영이 : 아 안돼 시험 망치고 죽다니...(털석)\n"+
        "\n"+
        "*수뭉이요정* : 후후...이번엔 열심히해 준영아 ! \n"+
        "\n"+
        "이 때 들은 말을 끝으로 나는 정말로 입학 첫날로 돌아왔다... \n"+
        "\n"+
        "준영이 : 수뭉이는... 실존했구나. 사랑해요 상명대! \n\n")
    

    #인트로 후 메인메뉴
def main_menu():
    os.system('cls')
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)
    print("\n")
    print(" _______________메인 메뉴________________\n")
    print(" |                                      |\n")
    print(" |         > 스케쥴 표 (a)              |\n")
    print(" |                                      |\n")
    print(" |         > 교수님 만나기 (s)          |\n")
    print(" |                                      |\n")
    print(" |         > 자판기 (d)                 |\n")
    print(" |                                      |\n")
    print(" |         > 스탯 확인 (f)              |\n")
    print(" |______________________________________|\n")
    print("\n")
    choice = input("무엇을 하시겠습니까? : \n")
    if choice == 'a':
        schedule()
    elif choice == 's':
        professor()
    elif choice == 'd':
        store()
    elif choice == 'f':
        status()
    else:
        print_slow("제대로 선택 하세요.\n")
        main_menu()
        

    #스케쥴 메뉴
def schedule():
    os.system('cls')
    global total_brain, total_code, total_health, total_money, total_stress, scheduleList
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
    print_slow(" 준영이의 세 달을 정해주세요 !\n\n")
    print(" ____________________일 정_______________________\n")
    print(" |                                               |\n")
    print(" |             > 1. 알바 가기                    |\n")
    print(" |        [소지금 up, 체력 up, 스트레스 down]    |\n")
    print(" |                                               |\n")
    print(" |             > 2. 운동 하기                    |\n")
    print(" |        [체력 up, 스트레스 down]               |\n")
    print(" |                                               |\n")
    print(" |             > 3. 일반 공부                    |\n")
    print(" |        [지능 up, 스트레스 up, 체력 down]      |\n")
    print(" |                                               |\n")
    print(" |             > 4. 코딩 공부                    |\n")
    print(" |        [코딩실력 up, 체력 dowm, 스트레스 up]  |\n")
    print(" |                                               |\n")
    print(" |             > 5. 재밌게 놀기                  |\n")
    print(" |        [소지금 down, 체력 up, 스트레스 down]  |\n")
    print(" |                                               |\n")
    print(" |_______________________________________________|\n")

    
    #리스트 비우기
    empty_scheduleList()

    while True:
        choice = input("메뉴로 돌아가기(6): \n")
        if choice == '6':
            
            main_menu()

        elif choice == '1':
            print("알바 가기를 선택하셨습니다.\n")
            scheduleList.append('알바 가기')
        
        elif choice == '2':
            print("운동 하기를 선택하셨습니다.\n")
            scheduleList.append('운동 하기')
        
        elif choice == '3':
            print("일반 공부를 선택하셨습니다.\n")
            scheduleList.append('일반 공부')

        elif choice == '4':
            print("코딩 공부를 선택하셨습니다.\n")
            scheduleList.append('코딩 공부')

        elif choice == '5':
            print("재밌게 놀기를 선택하셨습니다.\n")
            scheduleList.append('재밌게 놀기')

        else:
            def print_slow(text):
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.08)
            print_slow("제대로 입력하시라고요.\n")

        #세 달 정했으면 일정 증감 함수로 GO
        if len(scheduleList) == 3:
            schedule_UpDown()

# 스케쥴 표 선택 시 리스트 비우기
def empty_scheduleList():
    global scheduleList
    scheduleList = []

    
    #교수만나기메뉴
def professor():
    os.system('cls')
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.09)
    print("------연구실 앞------")
    print("> 박교수님 만나러 가기 (1)\n")
    print("> 김교수님 만나러 가기 (2)\n")
    print("메뉴로 돌아가기 (3)")
    print("--------------------")
    choice = input("무엇을 하시겠습니까? : \n")

    #교수님 선택
    if choice == '1':
        professor1()

    elif choice == '2':
        professor2()
    elif choice == '3':
        main_menu()
    else:
        print_slow("다시 입력하세요. 제발.\n")
        professor()

    #박교수님 선택
def professor1():
    os.system('cls')
    global total_proheart1, total_brain
    print_slow("준영이 : 박교수님 계세요?\n")
    if total_brain > 10:
        if total_brain >= 10:
            print_slow("아 준영이 안녕~\n")
            print_slow("1. 그냥요\n")
            print_slow("2. 상담하고 싶은게 있어서 왔어요\n")

            choice = input("어떤 대답을 할까? :\n")
            if choice == '1':
                print_slow("\"그러니. 내가 좀 바빠서 미안해 (•_•).\"\n")
                print_slow("쫓겨났다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print(f"김교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                main_menu()
            elif choice == '2':
                print_slow("\"아이고 그렇구나 잠시만, 여기 앉으면 돼\"\n")
                print_slow("준영이와 박교수님은 재밌게 대화를 나눴다\n")
                like1 = proheart1()
                total_proheart1 += like1
                print(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 !")
                main_menu()
            else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
        
    elif total_brain <= 10:
        print_slow("박소영 교수님은 자리에 안계시는 것 같다.\n")
        professor()


    #김교수님 선택
def professor2():
    os.system('cls')
    global total_proheart2, total_brain, total_code
    print_slow("준영이 : 김교수님 계세요?\n")
    if total_brain >= 20 and total_code >= 20:
        if total_brain >= 20 and total_code >= 20:
            print_slow("\"그래 어떤일로 왔니\"\n")
            print_slow("1. 그냥요\n")
            print_slow("2. 상담하고 싶은게 있어서 왔어요\n")

            choice = input("어떤 대답을 할까? :\n")
            if choice == '1':
                print_slow("\"그래? 할 말 없으면 이만 가자. 바쁘다 바뻐.\"\n")
                print_slow("쫓겨났다...\n")
                like2 = proheart2()
                total_proheart2 -= like2
                print(f"김교수님의 호감도가 {like2} 내려가서 {total_proheart2}가 되었다\n")
                main_menu()
            elif choice == '2':
                print_slow("\"그래? 여기 앉아봐, 뭐 상담 하려고\"\n")
                print_slow("준영이와 김교수님은 재밌게 대화를 나눴다\n")
                like2 = proheart2()
                total_proheart2 += like2
                print(f"김교수님의 호감도가 {like2} 올라서 {total_proheart2}가 되었다\n")
                main_menu()
            else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
    
    elif total_brain < 20 or total_code < 20:
        print_slow("김석규 교수님은 자리에 안계시는 것 같다.")
        main_menu()
        
    #자판기 메뉴
def store():
    os.system('cls')
    global total_money, total_brain, total_code, total_health, total_stress
    
    if total_money >= 5:
        print("\n")
        print_slow(" 무엇을 마시던 상상이상!! 구매하지 않으면 불행이 옵니다.\n")
        print("\n")
        print("____________________________자 판 기__________________________")
        print("\n")
        print("> 1. 맛이 좋은 초록 이슬 (5원) \n")
        print("       [스트레스 -20, 지능 -5]\n")
        print_slow("      -마시면 기분이 좋아집니다-\n")
        print("\n")
        print("> 2. 스x피 커피우유 (10원) \n")
        print("       [스트레스 +5, 지능 +10]\n")
        print_slow("      -저런...잠을 잘자야 키가 커 준영아-\n")
        print("\n")
        print("> 3. 맛이 좋지 않은 사약 한 접시 (15원) \n")
        print("       [스트레스 +10, 체력 +20]\n")
        print_slow("      -사약은 몸에 좋은 재료로 이루어져 있다는 사실-\n")
        print("\n")
        print("> 4. 딸기 맛이 나는 해열제 (10원)\n")
        print("      [스트레스 -20]\n")
        print_slow("      -준영아 힘내! 아프지마 유유.-\n")
        print("\n")
        print("> 5. 색이알록달록한버섯을우린물 (25원) \n")
        print("       [스트레스 -10, 코딩실력 +10, 지능 +10, 체력 -20]\n")
        print_slow("      -히히...이거 마시면 나도 코딩을...-\n")
        print("\n")
        print("------------------------------------------------------")

    elif total_money <= 4:
        print_slow(" 돈도 없으면서 뭘 사시려고요 ? 가서 돈벌어와\n")
        main_menu()

    #자판기 메뉴선택
    choice = input(" 무엇을 드시겠어요? 설마 아무것도 마시지 않는건 아니시죠? (y/n) \n")
    if choice == '1':
        if total_money >= 5:
            print(" < 스트레스가 해소되고 지능이 떨어졌다 !>\n")
            print_slow(" - 이슬은 아이셔가 맛있는데-\n")
            total_stress -= 20
            total_brain -= 20
            total_money -= 5
            main_menu()
        elif total_money < 5:
            print_slow(" < 소지금이 부족합니다...[거-지]>\n")
            store()

    elif choice == '2': 
        if total_money >= 9:
            print(" < 스트레스를 받고 지능이 올라갔다 !>\n")
            print_slow(" - 공부 화이팅... 카페인은 조금만-\n")
            total_stress += 5
            total_brain += 10
            total_money -= 10
            main_menu()
        elif total_money <= 9:
            print_slow(" < 소지금이 부족합니다...[거-지]>\n")
            store()

    elif choice == '3':
        if total_money >= 15:
            print(" < 스트레스를 받고 체력이 올라갔다 !>")
            print_slow(" - 우웩 너무 맛없어!! 하지만 먹는건 준영이다 화이팅! >o< - \n\n")
            total_stress += 10
            total_brain -= 20
            total_money -= 15
            main_menu()
        elif total_money <= 14:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            store()
        
    elif choice == '4':
        if total_money >=10:
            print(" < 스트레스가 해소되었다 ! >")
            print_slow("- 아플때까지 공부하지는 말기로 ㅜㅅㅜ - \n\n")
            total_stress -= 20
            total_money -= 10
            main_menu()
        elif total_money <= 9:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            store()
    elif choice == '5':
        if total_money >= 25:
            print(" < 스트레스가 해소되고 체력이 떨어지고 코딩실력과 지능이 올라갔다 ! >\n")
            print_slow(" - 코딩 능력자가 되기 위해서는 뭐든 할 수 있어... -\n\n")
            total_stress -= 10
            total_brain = 10
            total_code += 10
            total_health -= 20
            total_money -= 25
            main_menu()
        elif total_money <= 24:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            store()
        
    elif choice == 'y':
            print_slow(" 아무것도 사지 않으시겠다고요? \n")
            print_slow(" 그렇다면... <버섯> 을 강제로 먹이겠습니다.\n")
            print_slow(" 스트레스를 1 받았다. 우웩 \n")
            stress(1)
            main_menu()
    elif choice == 'n':
            print_slow(" 감사합니다! 자판기 숫자를 선택해서 구매하시면 됩니다! \n")
            store()    
    else:
        print_slow(" 뭐하세요? 뭐든 하세요.\n")
        store()

    #스탯 메뉴 
def status():
    os.system('cls')
    global total_money, total_brain, total_code, total_health, total_proheart1, total_proheart2, total_stress



    print("\n")
    print(" ________________스 탯_________________\n")
    print("|                                     |\n")
    print("|    지능:{:<27} |".format(total_brain))
    print("|                                     |\n")
    print("|    체력:{:<27} |".format(total_health))
    print("|                                     |\n")
    print("|    스트레스:{:<23} |".format(total_stress))
    print("|                                     |\n")
    print("|    코딩실력:{:<23} |".format(total_code))
    print("|                                     |\n")
    print("|    소지금:{:<25} |".format(total_money))
    print("|                                     |\n")
    print("|    박교수님 호감도:{:<16} |".format(total_proheart1))
    print("|                                     |\n")
    print("|    김교수님 호감도:{:<16} |".format(total_proheart2))
    print("|                                     |\n")
    print("|_____________________________________|\n")
    print("\n")

    while True:
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
        choice = input("  > 메뉴로 돌아가기 (1): \n")
        if choice == '1':
            main_menu()
            break
        else:
            print_slow(" 제대로 입력하시라고요.\n")



    


    #main 코드만 실행되게하는 코드(name은 현재 진행중인 코드를 뜻함)
if __name__ == "__main__":
        main()



