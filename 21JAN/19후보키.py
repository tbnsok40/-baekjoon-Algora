from itertools import combinations
def solution(relation):

    trans_rel = list(map(list, zip(*relation)))
    count = 0
    for a_list in trans_rel:
        if len(a_list) == len(set(a_list)):
            trans_rel.remove(a_list)
            count += 1
    # 유일성
    # print(trans_rel)
    N = len(trans_rel)
    for i in range(2, N):
        for j in combinations(trans_rel,i):
            temp_list = []
            for k in zip(*j):
                temp_list.append(k)
            if len(temp_list) == len(set(temp_list)):
                # print(temp_list)
                count += 1

    # 이제 최소성 만족시키러 ㄲ

    # print(count)
    return count


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))


#set은 중복 허용안하니까 리스트와 세트와 길이 비교했을 때 같은거 리턴
