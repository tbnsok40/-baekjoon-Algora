str1 = "FRANCE"
str2 = 'french'

# str1 = "E=M*C^2"
# str2 = "e=m*c^2"

# str1 = "AA_bb_aa_AA"
# str2 = "BBB"

str1 = "ABDDD"
str2 = "DDEFGHH"

# str1 = "AACCC"
# str2 = "A A A A A C C C C"

import math
import re
def solution(str1, str2):

    # str3 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    # str4 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    # print(str3)
    # print(str4)

    str1 = str1.upper()
    str2 = str2.upper()
    temp1, temp2 = [], []

    # 문자 1차 가공
    temp1 = [(str1[i] + str1[i + 1]) for i in range(len(str1) - 1) if (str1[i] + str1[i + 1]).isalpha()]
    temp2 = [(str2[i] + str2[i + 1]) for i in range(len(str2) - 1) if (str2[i] + str2[i + 1]).isalpha()]
    print(temp1)
    print(temp2)

    gyo = set(temp2) & set(temp1)
    hap = set(temp1) | set(temp2)
    print(gyo)
    print(hap)

    # 여기가 이해 안돼
    gyo_sum = [min(str1.count(gg), str2.count(gg)) for gg in gyo]
    hap_sum = [max(str1.count(hh), str2.count(hh)) for hh in hap]
    print(gyo_sum)
    print(hap_sum)

    # uni_temp = []
    # for i in temp1:
    #     for j in temp2:
    #         if i == j:
    #             uni_temp.append(i)
    #             temp2.remove(j)
    #             break
    # all_temp = temp1 + temp2

    if len(gyo) != 0 and len(hap) != 0:
        return math.floor((len(gyo) / len(hap)) * 65536)
    else:
        return 65536

    # if len(uni_temp) != 0 and len(all_temp) != 0:
    #     return math.floor((len(uni_temp) / len(all_temp)) * 65536)
    # else:
    #     return 65536
# test 5, 13 error
print(solution(str1, str2))

