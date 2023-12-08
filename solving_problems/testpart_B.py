# 답을 받아서 산출하기...sky


# 입력 리스트 [] 정답리스트 [] 점수 리스트[]
# if문으로 비교해서 점수 넣기(function쓰기 가능)
# 최종 점수 계산식

# 계산하는 함수 정의
def result_cal(user_answer) :
    pass
    correct_answer = [2,1,1,2]  # 정확한 답안 리스트
    score_list=[10,15,10,5]     # 각 답에 따른 점수 리스트
    score=[]
    for i in range(len(user_answer)):  #question으로부터 받은 user_answer를 변수로 사용
       if user_answer[i] == correct_answer[i] : # 둘의 답이 같을 경우 
            score.append(int(score_list[i]))    # score 리스트에 점수 리스트에 해당되는 요소 추가
            user_sum = sum(score)               # 전체 점수 합산
    # if문을 사용해 점수에 따른 학점 계산
    if user_sum >=30 :
        user_score = "A"
    elif user_sum >=20 :
        user_score = "B"
    else:
        user_score = "C"
    # print 해야 하는 결과값들 넣기
    print ("--------결과---------")
    print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(user_answer[0], user_answer[1],user_answer[2], user_answer[3]))
    print("당신 응답 합계 : {}점".format(user_sum))
    print("학점은 {}입니다.".format(user_score))
 
result_cal(question()) #A에서 제작된 question 함수를 대입하여 최종 print 도출하기