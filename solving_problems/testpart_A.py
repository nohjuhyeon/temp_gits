# # 문제 만들기 _ juuuuuu

def question():    #질문지 function 설정
    question_list = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)",        #질문 리스트 설정
                    "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)",
                    "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)",
                    "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                    ]
    answer_list = ["1) var name, 2) name = value, 3) set name, 4) name == value",       #답변 리스트 설정
                "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다",
                "1) if-else, 2) for-in, 3) while, 4) def",
                "1) class, 2) def, 3) import, 4) return"
    ]

    user_answer = []  #유저가 입력한 답변 리스트

    for a in range(len(question_list)): 
        print(question_list[a])         #질문 출력
        print(answer_list[a])           #답항 출력
        input_answer = int(input("- 정답:"))    #유저 답변 출력
        user_answer.append(input_answer)    #답변 리스트에 추가
        pass
    pass
    return user_answer