# library
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import pandas as pd
from pandas import *
import numpy as np

'''
# variable 
health_2020_02 ~ health_2020_05
health_2019_02 ~ health_2019_05
food_2020_02 ~ food_2020_05
food_2019_02 ~ food_2019_05
cul_2020_02 ~ cul_2020_05
cul_2019_02 ~ cul_2019_05
medi_2020_02 ~ medi_2020_05
medi_2019_02 ~ medi_2019_05
leisure_2020_02 ~ leisure_2020_05
leisure_2019_02 ~ leisure_2019_05
stay_2020_02 ~ stay_2020_05
stay_2019_02 ~ stay_2019_05
'''


# class word
class word():
    def __init__(self):
        self.word = []

    def input_word(self, arg):
        self.arg = arg
        self.word.append(self.arg)
        return self.word


if __name__ == "__main__":
    test = word()
    test1 = test.input_word("가")
    test1 = test.input_word("나")
    test1 = test.input_word("다")
    print(test1)
'''
#health 2020
result: health_2020_02  ~  health_2020_05
'''
# from health202002
embedding_mode = Word2Vec(health202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
# 유사도
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 건강 : 위협(-) /중대한(-)/ 헛걸음(-)/ 당혹스럽긴(-) / 범죄 (-) / 성급히(-) / 지키기 (+)

health = word()
health_20_02 = health.input_word("위협")
health_20_02 = health.input_word("중대한")
health_20_02 = health.input_word("헛걸음")
health_20_02 = health.input_word("당혹스럽긴")
health_20_02 = health.input_word("범죄")
health_20_02 = health.input_word("성급히")
health_20_02 = health.input_word("지키기")

health_2020_02 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_02))], 'target': health_20_02,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_02]})

health_2020_02['postivie'] = ['-', '-', '-', '-', '-', '-', '+']
print(health_2020_02)

# from health202003
embedding_mode = Word2Vec(health202003, size=100, window=2,
                          min_count=1, workers=4, iter=50,
                          sg=1)
# 유사도
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 염려(-)/ 회복(+)/ 위생(중립)/공중(중립)/ 밀봉(중립) /공중보건(중립) /분쟁(-)
# (주석참고) 염려(-)/ 회복(+)/ 위생(-)/공중(-)/ 밀봉(-) /공중보건(-) /분쟁(-)
health = word()
health_20_03 = health.input_word("염려")
health_20_03 = health.input_word("회복")
health_20_03 = health.input_word("위생")
health_20_03 = health.input_word("공중")
health_20_03 = health.input_word("밀봉")
health_20_03 = health.input_word("공중보건")
health_20_03 = health.input_word("분쟁")
health_2020_03 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_03))], 'target': health_20_03,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_03]})
health_2020_03['postivie'] = ['-', '+', '-', '-', '-', '-', '-']
print(health_2020_03)
'''
# 중립단어 : 위생, 공중, 밀봉, 공중보건
print(embedding_mode.wv.most_similar(positive=['위생'],topn=100)) # 책임지는(-), 염려(-), 회복(+)
print(embedding_mode.wv.most_similar(positive=['공중'],topn=100)) # 책임지는(-), 위생(중립)
print(embedding_mode.wv.most_similar(positive=['밀봉'],topn=100)) # 속였다(-), 구속(-), KF(-), 염려(-)
print(embedding_mode.wv.most_similar(positive=['공중보건'],topn=100)) #책임지는 (-), 통제(-)
#result : 중립단어 모두 -
'''

# from health202004
embedding_mode = Word2Vec(health202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 생명(+)/ 걱정(-)/ 스테이(-) / 과로(-) / 불편(-) / 힘들(-) / 줄일(-) / 대가(-) / 호소(-)
health = word()
health_20_04 = health.input_word("생명")
health_20_04 = health.input_word("걱정")
health_20_04 = health.input_word("스테이")
health_20_04 = health.input_word("과로")
health_20_04 = health.input_word("불편")
health_20_04 = health.input_word("힘들")
health_20_04 = health.input_word("줄일")
health_20_04 = health.input_word("대가")
health_20_04 = health.input_word("호소")
health_2020_04 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_04))], 'target': health_20_04,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_04]})

health_2020_04['postivie'] = ['+', '-', '-', '-', '-', '-', '-', '-', '-']
print(health_2020_04)

# from health202005
embedding_mode = Word2Vec(health202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 생명(+)/ 신선(+)/ 염려(-)/ 과로(-) /무리한(-)
health = word()
health_20_05 = health.input_word("생명")
health_20_05 = health.input_word("신선")
health_20_05 = health.input_word("염려")
health_20_05 = health.input_word("과로")
health_20_05 = health.input_word("무리한")
health_2020_05 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_05))], 'target': health_20_05,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_05]})
health_2020_05['postivie'] = ['+', '+', '-', '-', '-']
print(health_2020_05)

'''
#health 2019
result: health_2019_02  ~  health_2019_05
'''

# from health201902
embedding_mode = Word2Vec(health201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 조심해야(-)/위협(-)/즐기는(+)/주의(-)/해외여행(+)/다행히(+)/성실하게(+)
health = word()
health_19_02 = health.input_word("조심해야")
health_19_02 = health.input_word("위협")
health_19_02 = health.input_word("즐기는")
health_19_02 = health.input_word("주의")
health_19_02 = health.input_word("해외여행")
health_19_02 = health.input_word("다행히")
health_19_02 = health.input_word("성실하게")

health_2019_02 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_02))], 'target': health_19_02,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_02]})
health_2019_02['postivie'] = ['-', '-', '+', '-', '+', '+', '+']
print(health_2019_02)

# from health201903
embedding_mode = Word2Vec(health201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 안전한지(-)/비싸지만(-)/힘들어져(-)/격차(-)/해롭다(-)/지킬(+)/Healthiest(+)
health = word()
health_19_03 = health.input_word("안전한지")
health_19_03 = health.input_word("비싸지만")
health_19_03 = health.input_word("힘들어져")
health_19_03 = health.input_word("격차")
health_19_03 = health.input_word("해롭다")
health_19_03 = health.input_word("지킬")
health_19_03 = health.input_word("Healthiest")

health_2019_03 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_03))], 'target': health_19_03,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_03]})
health_2019_03['postivie'] = ['-', '-', '-', '-', '-', '+', '+']
print(health_2019_03)

# from health201904
embedding_mode = Word2Vec(health201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 호흡기(-)/위협(-)/생명(+)/과로(-)/침투(-)/좋다(+)
health = word()
health_19_04 = health.input_word("호흡기")
health_19_04 = health.input_word("위협")
health_19_04 = health.input_word("생명")
health_19_04 = health.input_word("과로")
health_19_04 = health.input_word("침투")
health_19_04 = health.input_word("좋다")
health_2019_04 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_04))], 'target': health_19_04,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_04]})
health_2019_04['postivie'] = ['-', '-', '+', '-', '-', '+']
print(health_2019_04)

# from health201905
embedding_mode = Word2Vec(health201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 지켜(+)/복지(+)/웰빙(+)/위협(-)/좋지(+)/진흥(+)/따뜻한(+)/깨끗한(+)
health = word()
health_19_05 = health.input_word("지켜")
health_19_05 = health.input_word("복지")
health_19_05 = health.input_word("웰빙")
health_19_05 = health.input_word("위협")
health_19_05 = health.input_word("좋지")
health_19_05 = health.input_word("진흥")
health_19_05 = health.input_word("따뜻한")
health_19_05 = health.input_word("깨끗한")

health_2019_05 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_05))], 'target': health_19_05,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_05]})
health_2019_05['postivie'] = ['+', '+', '+', '-', '+', '+', '+', '+']
print(health_2019_05)

'''
#food 2020
result: food_2020_02  ~  food_2020_05
'''

# from food202002
embedding_mode = Word2Vec(food202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 까다로운(-)/좋다(+)/소형(-)/궁합(+)/정해진(-)/외부(-)/살아남은(+)/배달(-)/지킨(+)/성공한(+)
food = word()
food_20_02 = food.input_word("까다로운")
food_20_02 = food.input_word("좋다")
food_20_02 = food.input_word("소형")
food_20_02 = food.input_word("궁합")
food_20_02 = food.input_word("정해진")
food_20_02 = food.input_word("외부")
food_20_02 = food.input_word("살아남은")
food_20_02 = food.input_word("배달")
food_20_02 = food.input_word("지킨")
food_20_02 = food.input_word("성공한")
food_2020_02 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_02))], 'target': food_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_02]})
food_2020_02['positive'] = ['-', '+', '-', '+', '-', '-', '+', '-', '+', '+']
print(food_2020_02)

# from food202003
embedding_mode = Word2Vec(food202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 빠른(+)/잃었고(-)/닫은(-)/배달(-)/관광(중립)/대유행(중립)/불확실하다(-)
# 빠른(+)/잃었고(-)/닫은(-)/배달(-)/관광(-)/대유행(-)/불확실하다(-)
'''
#중립단어 : 관광, 대유행
print(embedding_mode.wv.most_similar(positive=['관광'],topn=100)) #마비(-)/떠나(-)/열악한(-)
print(embedding_mode.wv.most_similar(positive=['대유행'],topn=100)) #잃었고(-)/억제(-)/압도(-)
'''
food = word()
food_20_03 = food.input_word("빠른")
food_20_03 = food.input_word("잃었고")
food_20_03 = food.input_word("닫은")
food_20_03 = food.input_word("배달")
food_20_03 = food.input_word("관광")
food_20_03 = food.input_word("대유행")
food_20_03 = food.input_word("불확실하다")
food_2020_03 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_03))], 'target': food_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_03]})
food_2020_03['positive'] = ['+', '-', '-', '-', '-', '-', '-']

print(food_2020_03)

# from food202004
embedding_mode = Word2Vec(food202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 기름진(-)/피하(-)/맛있어야(+)/맛집(+)
print(embedding_mode.wv.most_similar(positive=['배달'], topn=100))
# 급증(+)/많습니다(+)/않습니다(-)/폴리프로필렌(-)/포장(-)

food = word()
food_20_04 = food.input_word("기름진")
food_20_04 = food.input_word("피하")
food_20_04 = food.input_word("맛있어야")
food_20_04 = food.input_word("맛집")
food_2020_04 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_04))], 'target': food_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_04]})
food = word()
food_20_04_1 = food.input_word("급증")
food_20_04_1 = food.input_word("많습니다")
food_20_04_1 = food.input_word("않습니다")
food_20_04_1 = food.input_word("폴리프로필렌")
food_20_04_1 = food.input_word("포장")

food_2020_04 = food_2020_04.append(
    pd.DataFrame({'keyword': ['배달' for i in range(0, len(food_20_04_1))], 'target': food_20_04_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_04_1]}))
food_2020_04 = food_2020_04.reset_index(drop=True)
food_2020_04['positive'] = ['-', '-', '+', '+', '+', '+', '-', '-', '-']
print(food_2020_04)

# from food202005
embedding_mode = Word2Vec(food202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 비해(-)/신선한(+)/Personal(-)/장벽(-)/즐기기(+)/일상생활(+)
food = word()
food_20_05 = food.input_word("비해")
food_20_05 = food.input_word("신선한")
food_20_05 = food.input_word("Personal")
food_20_05 = food.input_word("장벽")
food_20_05 = food.input_word("즐기기")
food_20_05 = food.input_word("일상생활")
food_2020_05 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_05))], 'target': food_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_05]})
food_2020_05['positive'] = ['-', '+', '-', '-', '+', '+']

'''
#food 2019
result: food_2019_02  ~  food_2019_05
'''

# from food201902
embedding_mode = Word2Vec(food201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 기회(+)/배려하되(+)/전세계(+)/편하게(+)/깔끔한(+)/좋고(+)
food = word()
food_19_02 = food.input_word("기회")
food_19_02 = food.input_word("배려하되")
food_19_02 = food.input_word("전세계")
food_19_02 = food.input_word("편하게")
food_19_02 = food.input_word("깔끔한")
food_19_02 = food.input_word("좋고")
food_2019_02 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_02))], 'target': food_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_02]})
food_2019_02['positive'] = ['+', '+', '+', '+', '+', '+']
print(food_2019_02)

# from food201903
embedding_mode = Word2Vec(food201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 재미있고(+)/흥(+)/가볍게(+)/좋아한다면(+)/춤(+)/힐링(+)
food = word()
food_19_03 = food.input_word("재미있고")
food_19_03 = food.input_word("흥")
food_19_03 = food.input_word("가볍게")
food_19_03 = food.input_word("좋아한다면")
food_19_03 = food.input_word("흥")
food_19_03 = food.input_word("힐링")
food_2019_03 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_03))], 'target': food_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_03]})
food_2019_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(food_2019_03)

# from food201904
embedding_mode = Word2Vec(food201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 세련되게(+)/나눠주고(+)/업그레이드(+)/맛있는(+)/특별하게(+)/야무진(+)/밝은(+)
food = word()
food_19_04 = food.input_word("세련되게")
food_19_04 = food.input_word("나눠주고")
food_19_04 = food.input_word("업그레이드")
food_19_04 = food.input_word("맛있는")
food_19_04 = food.input_word("특별하게")
food_19_04 = food.input_word("야무진")
food_19_04 = food.input_word("밝은")

food_2019_04 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_04))], 'target': food_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_04]})
food_2019_04['positive'] = ['+' for i in range(0, 7)]

# from food201905
embedding_mode = Word2Vec(food201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 아니라(-)/레저(+)/않으려(-)/버텨(-)/휴식(+)/가능해지게(+)/거친(-)/제재(-)/맛있을(+)
food = word()
food_19_05 = food.input_word("아니라")
food_19_05 = food.input_word("레저")
food_19_05 = food.input_word("않으려")
food_19_05 = food.input_word("버텨")
food_19_05 = food.input_word("휴식")
food_19_05 = food.input_word("가능해지게")
food_19_05 = food.input_word("거친")
food_19_05 = food.input_word("제재")
food_19_05 = food.input_word("맛있을")
food_2019_05 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_05))], 'target': food_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_05]})
food_2019_05['positive'] = ['-', '+', '-', '-', '+', '+', '-', '-', '+']
print(food_2019_05)

'''
#culture 2020
result: cul_2020_02  ~  cul_2020_05
'''
# from cul202002
embedding_mode = Word2Vec(cul202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 줄어들고(-)/불가능(-)/돌이켜(-)/즐기기(+)/없다고(-)/장점(+)/즐기자(+)
cul = word()
cul_20_02 = cul.input_word("줄어들고")
cul_20_02 = cul.input_word("불가능")
cul_20_02 = cul.input_word("돌이켜")
cul_20_02 = cul.input_word("즐기기")
cul_20_02 = cul.input_word("없다고")
cul_20_02 = cul.input_word("장점")
cul_20_02 = cul.input_word("즐기자")

cul_2020_02 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_02))], 'target': cul_20_02,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_02]})
cul_2020_02['positive'] = ['-', '-', '-', '+', '-', '+', '+']
print(cul_2020_02)

# from cul202003
embedding_mode = Word2Vec(cul202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 가능해진(+)/웃는(+)/미비한(-)/활성화(+)/힘들죠(-)
cul = word()
cul_20_03 = cul.input_word("가능해진")
cul_20_03 = cul.input_word("웃는")
cul_20_03 = cul.input_word("미비한")
cul_20_03 = cul.input_word("활성화")
cul_20_03 = cul.input_word("힘들죠")
cul_2020_03 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_03))], 'target': cul_20_03,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_03]})
print(embedding_mode.wv.most_similar(positive=['취미'], topn=100))

# 그립습니다(-)/편의(+)/소중한(+)/힘든(-)/좋습니다(+)/좋다(+)
cul = word()
cul_20_03_1 = cul.input_word("그립습니다")
cul_20_03_1 = cul.input_word("편의")
cul_20_03_1 = cul.input_word("소중한")
cul_20_03_1 = cul.input_word("힘든")
cul_20_03_1 = cul.input_word("좋습니다")
cul_20_03_1 = cul.input_word("좋다")
cul_2020_03 = cul_2020_03.append(
    pd.DataFrame({'keyword': ['취미' for i in range(0, len(cul_20_03_1))], 'target': cul_20_03_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='취미', w2=i)) for i in cul_20_03_1]}))
cul_2020_03['positive'] = ['+', '+', '-', '+', '-', '-', '+', '+', '-', '+', '+']
cul_2020_03 = cul_2020_03.reset_index(drop=True)
print(cul_2020_03)

# from cul202004
embedding_mode = Word2Vec(cul202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 편의(+)/풍부하다(+)/건전한(+)/다양한(+)/좋다며(+)/우수하다(+)/훈훈함을(+)/편리하게(+)/어렵고(-)
cul = word()
cul_20_04 = cul.input_word("편의")
cul_20_04 = cul.input_word("풍부하다")
cul_20_04 = cul.input_word("건전한")
cul_20_04 = cul.input_word("다양한")
cul_20_04 = cul.input_word("좋다며")
cul_20_04 = cul.input_word("우수하다")
cul_20_04 = cul.input_word("훈훈함을")
cul_20_04 = cul.input_word("편리하게")
cul_20_04 = cul.input_word("어렵고")
cul_2020_04 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_04))], 'target': cul_20_04,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_04]})

print(embedding_mode.wv.most_similar(positive=['취미'], topn=100))
# 극복(+)/슬기로운(+)/씁쓸한(-)/즐기고(+)/즐거움(+)/재치(+)
cul = word()
cul_20_04_1 = cul.input_word("극복")
cul_20_04_1 = cul.input_word("슬기로운")
cul_20_04_1 = cul.input_word("씁쓸한")
cul_20_04_1 = cul.input_word("즐기고")
cul_20_04_1 = cul.input_word("즐거움")
cul_20_04_1 = cul.input_word("재치")
cul_2020_04 = cul_2020_04.append(
    pd.DataFrame({'keyword': ['취미' for i in range(0, len(cul_20_04_1))], 'target': cul_20_04_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='취미', w2=i)) for i in cul_20_04_1]}))
cul_2020_04['positive'] = ['+', '+', '+', '+', '+', '+', '+', '+', '-', '+', '+', '-', '+', '+', '+']
cul_2020_04 = cul_2020_04.reset_index(drop=True)
print(cul_2020_04)

# from cul202005
embedding_mode = Word2Vec(cul202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 확산(-)/다양한(+)/배낭여행(+)/좋아했다(+)/유치했다(-)
cul = word()
cul_20_05 = cul.input_word("확산")
cul_20_05 = cul.input_word("다양한")
cul_20_05 = cul.input_word("배낭여행")
cul_20_05 = cul.input_word("좋아했다")
cul_20_05 = cul.input_word("유치했다")
cul_2020_05 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_05))], 'target': cul_20_05,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_05]})
cul_2020_05['positive'] = ['-', '+', '+', '+', '-']
print(cul_2020_05)

'''
#culture 2019
result: cul_2019_02  ~  cul_2019_05
'''
# from cul201902
embedding_mode= Word2Vec(cul201902, size=100,window=2,
                         min_count=1, workers=4, iter=100,
                         sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'],topn=100))
#성숙한(+)/안전하답니다(+)/열린(+)/역량(+)/활성화(+)
cul=word()
cul_19_02=cul.input_word("성숙한")
cul_19_02=cul.input_word("안전하답니다")
cul_19_02=cul.input_word("열린")
cul_19_02=cul.input_word("역량")
cul_19_02=cul.input_word("활성화")
cul_2019_02=pd.DataFrame({'keyword':['문화' for i in range(0,len(cul_19_02))],'target':cul_19_02,
              'vector':[float(embedding_mode.wv.similarity(w1='문화',w2=i)) for i in cul_19_02]})

print(embedding_mode.wv.most_similar(positive=['취미'],topn=100))
#좋아하는(+)/중요한(+)/기대할(+)/성숙한(+)
cul=word()
cul_19_02_1=cul.input_word("좋아하는")
cul_19_02_1=cul.input_word("중요한")
cul_19_02_1=cul.input_word("기대할")
cul_19_02_1=cul.input_word("성숙한")
cul_2019_02=cul_2019_02.append(pd.DataFrame({'keyword':['취미' for i in range(0,len(cul_19_02_1))],'target':cul_19_02_1,
              'vector':[float(embedding_mode.wv.similarity(w1='취미',w2=i)) for i in cul_19_02_1]}))
cul_2019_02['positive']=['+','+','+','+','+','+','+','+','+']
cul_2019_02=cul_2019_02.reset_index(drop=True)
print(cul_2019_02)

# from cul201903
embedding_mode = Word2Vec(cul201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 줄면서(-)/다지는(+)/없는(-)/뜨거웠다(+)/짜릿함과(+)/강했지만(+)
cul = word()
cul_19_03 = cul.input_word("줄면서")
cul_19_03 = cul.input_word("다지는")
cul_19_03 = cul.input_word("없는")
cul_19_03 = cul.input_word("뜨거웠다")
cul_19_03 = cul.input_word("짜릿함과")
cul_19_03 = cul.input_word("강했지만")
cul_2019_03 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_03))], 'target': cul_19_03,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_03]})
cul_2019_03['positive'] = ['-', '+', '-', '+', '+', '+']
print(cul_2019_03)

# from cul201904
embedding_mode = Word2Vec(cul201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 불과했다(-)/기대해(+)/않아(-)/적합하다는(+)/당황(-)/신선했다(+)
cul = word()
cul_19_04 = cul.input_word("불과했다")
cul_19_04 = cul.input_word("기대해")
cul_19_04 = cul.input_word("않아")
cul_19_04 = cul.input_word("적합하다는")
cul_19_04 = cul.input_word("당황")
cul_19_04 = cul.input_word("신선했다")
cul_2019_04 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_04))], 'target': cul_19_04,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_04]})
cul_2019_04['positive'] = ['-', '+', '-', '+', '-', '+']
print(cul_2019_04)

# from cul201905
embedding_mode = Word2Vec(cul201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 놀이(+)/선물(+)/유행(+)/교류(+)/힐링(+)/광범위하게(+)/않는다(-)/생명력(+)/효행(+)/맑은(+)
cul = word()
cul_19_05 = cul.input_word("놀이")
cul_19_05 = cul.input_word("선물")
cul_19_05 = cul.input_word("유행")
cul_19_05 = cul.input_word("교류")
cul_19_05 = cul.input_word("힐링")
cul_19_05 = cul.input_word("광범위하게")
cul_19_05 = cul.input_word("않는다")
cul_19_05 = cul.input_word("생명력")
cul_19_05 = cul.input_word("효행")
cul_19_05 = cul.input_word("맑은")
cul_2019_05 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_05))], 'target': cul_19_05,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_05]})
cul_2019_05['positive'] = ['+', '+', '+', '+', '+', '+', '-', '+', '+', '+']
print(cul_2019_05)

'''
#medi 2020
result: medi_2020_02  ~  medi_2020_05
'''

# from medi202002
embedding_mode = Word2Vec(medi202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 떨어진다(-)/ 싸우는(-)/ 피로(-)/폐쇄입니(-)/열악하다(-)/마비(-)/폐쇄(-)/회복(+)
medi = word()
medi_20_02 = medi.input_word("떨어진다")
medi_20_02 = medi.input_word("싸우는")
medi_20_02 = medi.input_word("피로")
medi_20_02 = medi.input_word("폐쇄입니")
medi_20_02 = medi.input_word("열악하다")
medi_20_02 = medi.input_word("마비")
medi_20_02 = medi.input_word("폐쇄")
medi_20_02 = medi.input_word("회복")
medi_2020_02 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_02))], 'target': medi_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_02]})
medi_2020_02['positive'] = ['-', '-', '-', '-', '-', '-', '-', '+']
medi_2020_02.at[3, 'target'] = '폐쇄'
print(medi_2020_02)

# from medi202003
embedding_mode = Word2Vec(medi202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 협업(+)/감염증(-)/확진(-)/찔려(-)/노력(+)/다양한(+)/이뤄졌다(+)/불안감(-)/책임(-)
medi = word()
medi_20_03 = medi.input_word("협업")
medi_20_03 = medi.input_word("감염증")
medi_20_03 = medi.input_word("확진")
medi_20_03 = medi.input_word("찔려")
medi_20_03 = medi.input_word("노력")
medi_20_03 = medi.input_word("다양한")
medi_20_03 = medi.input_word("이뤄졌다")
medi_20_03 = medi.input_word("불안감")
medi_20_03 = medi.input_word("책임")
medi_2020_03 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_03))], 'target': medi_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_03]})
medi_2020_03['positive'] = ['+', '-', '-', '-', '+', '+', '+', '-', '-']
print(medi_2020_03)

# from medi202004
embedding_mode = Word2Vec(medi202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 위반(-)/압박(-)/연장(-)/악화(-)/윤리(+)/않기로(-)/화해(+)/면역(+)/협업(+)/비판(-)/죄송하다(-)
medi = word()
medi_20_04 = medi.input_word("위반")
medi_20_04 = medi.input_word("압박")
medi_20_04 = medi.input_word("연장")
medi_20_04 = medi.input_word("악화")
medi_20_04 = medi.input_word("윤리")
medi_20_04 = medi.input_word("않기로")
medi_20_04 = medi.input_word("화해")
medi_20_04 = medi.input_word("면역")
medi_20_04 = medi.input_word("협업")
medi_20_04 = medi.input_word("비판")
medi_20_04 = medi.input_word("죄송하다")
medi_2020_04 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_04))], 'target': medi_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_04]})

medi_2020_04['positive'] = ['-', '-', '-', '-', '+', '-', '+', '+', '+', '-', '-']
print(medi_2020_04)

# from medi202005
embedding_mode = Word2Vec(medi202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 대란(-)/active(+)/일어날지도(암시,-)/방호복(-)/종교시설(-)/모른다(-)/집착(-)/참여(+)/Care(+)/않습니다(-)/
medi = word()
medi_20_05 = medi.input_word("대란")
medi_20_05 = medi.input_word("active")
medi_20_05 = medi.input_word("일어날지도")
medi_20_05 = medi.input_word("방호복")
medi_20_05 = medi.input_word("종교시설")
medi_20_05 = medi.input_word("모른다")
medi_20_05 = medi.input_word("집착")
medi_20_05 = medi.input_word("참여")
medi_20_05 = medi.input_word("Care")
medi_20_05 = medi.input_word("않습니다")
medi_2020_05 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_05))], 'target': medi_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_05]})
medi_2020_05['positive'] = ['-', '+', '-', '-', '-', '-', '-', '+', '+', '-']
print(medi_2020_05)

'''
#medi 2019
result: medi_2019_02  ~  medi_2019_05
'''
# from medi201902
embedding_mode = Word2Vec(medi201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# care(+)/잘(+)/못(-)/하지만(-)/Healthiest(+)/새로운(+)/않겠다는(-)/사망자(-)
medi = word()
medi_19_02 = medi.input_word("care")
medi_19_02 = medi.input_word("잘")
medi_19_02 = medi.input_word("못")
medi_19_02 = medi.input_word("하지만")
medi_19_02 = medi.input_word("Healthiest")
medi_19_02 = medi.input_word("새로운")
medi_19_02 = medi.input_word("않겠다는")
medi_19_02 = medi.input_word("사망자")

medi_2019_02 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_02))], 'target': medi_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_02]})
medi_2019_02['positive'] = ['+', '+', '-', '-', '+', '+', '-', '-']
print(medi_2019_02)

# from medi201903
embedding_mode = Word2Vec(medi201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 중단(-)/늘리고(+)/말기(-)/폭력(-)/객관성(+)/안전(+)/예방(+)/않는다(-)
medi = word()
medi_19_03 = medi.input_word("중단")
medi_19_03 = medi.input_word("늘리고")
medi_19_03 = medi.input_word("말기")
medi_19_03 = medi.input_word("폭력")
medi_19_03 = medi.input_word("객관성")
medi_19_03 = medi.input_word("안전")
medi_19_03 = medi.input_word("예방")
medi_19_03 = medi.input_word("않는다")
medi_2019_03 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_03))], 'target': medi_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_03]})
medi_2019_03['positive'] = ['-', '+', '-', '-', '+', '+', '+', '-']
print(medi_2019_03)

# from medi201904
embedding_mode = Word2Vec(medi201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 지식(+)/필요한(+)/부담(-)/좋다(+)/유예(-)
medi = word()
medi_19_04 = medi.input_word("지식")
medi_19_04 = medi.input_word("필요한")
medi_19_04 = medi.input_word("부담")
medi_19_04 = medi.input_word("좋다")
medi_19_04 = medi.input_word("유예")
medi_2019_04 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_04))], 'target': medi_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_04]})
medi_2019_04['positive'] = ['+', '+', '-', '+', '-']
print(medi_2019_04)

# from medi201905
embedding_mode = Word2Vec(medi201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 피부관리(+)/방해(-)/완전히(+)/다양한(+)/않는다(-)/
medi = word()
medi_19_05 = medi.input_word("피부관리")
medi_19_05 = medi.input_word("방해")
medi_19_05 = medi.input_word("완전히")
medi_19_05 = medi.input_word("다양한")
medi_19_05 = medi.input_word("않는다")
medi_2019_05 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_05))], 'target': medi_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_05]})
medi_2019_05['positive'] = ['+', '-', '+', '+', '-']
print(medi_2019_05)

'''
#leisure 2020
result: leisure_2020_02  ~  leisure_2020_05
'''
# from leisure202002
embedding_mode = Word2Vec(leisure202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 찾는(+)/보트(+)/함께(+)/해변(+)/새롭게(+)/명소(+)/색다른(+)
leisure = word()
leisure_20_02 = leisure.input_word("찾는")
leisure_20_02 = leisure.input_word("보트")
leisure_20_02 = leisure.input_word("함께")
leisure_20_02 = leisure.input_word("해변")
leisure_20_02 = leisure.input_word("새롭게")
leisure_20_02 = leisure.input_word("명소")
leisure_20_02 = leisure.input_word("색다른")
leisure_2020_02 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_02))], 'target': leisure_20_02,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_02]})
leisure_2020_02['positive'] = ['+', '+', '+', '+', '+', '+', '+']
print(leisure_2020_02)

# from leisure202003
embedding_mode = Word2Vec(leisure202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 축제(+)/휴양(+)/기대하고(+)/친근한(+)/대단한(+)/편안한(+)
leisure = word()
leisure_20_03 = leisure.input_word("축제")
leisure_20_03 = leisure.input_word("휴양")
leisure_20_03 = leisure.input_word("기대하고")
leisure_20_03 = leisure.input_word("친근한")
leisure_20_03 = leisure.input_word("대단한")
leisure_20_03 = leisure.input_word("편안한")
leisure_2020_03 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_03))], 'target': leisure_20_03,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_03]})
leisure_2020_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(leisure_2020_03)

# from leisure202004
embedding_mode = Word2Vec(leisure202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 휴식(+)/즐기려는(+)/건강한(+)/즐길(+)/다양한(+)/불안해진다(-)/불가능하다(-)
leisure = word()
leisure_20_04 = leisure.input_word("휴식")
leisure_20_04 = leisure.input_word("즐기려는")
leisure_20_04 = leisure.input_word("건강한")
leisure_20_04 = leisure.input_word("즐길")
leisure_20_04 = leisure.input_word("다양한")
leisure_20_04 = leisure.input_word("불안해진다")
leisure_20_04 = leisure.input_word("불가능하다")
leisure_2020_04 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_04))], 'target': leisure_20_04,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_04]})
leisure_2020_04['positive'] = ['+', '+', '+', '+', '+', '-', '-']
print(leisure_2020_04)

# from leisure202005
embedding_mode = Word2Vec(leisure202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 없고(-)/해양(+)/쏘다니는(+)/담긴(+)
# print(embedding_mode.wv.most_similar(positive=['관광'],topn=100)) : 다를게 없음
leisure = word()
leisure_20_05 = leisure.input_word("없고")
leisure_20_05 = leisure.input_word("해양")
leisure_20_05 = leisure.input_word("쏘다니는")
leisure_20_05 = leisure.input_word("담긴")
leisure_2020_05 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_05))], 'target': leisure_20_05,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_05]})
leisure_2020_05['positive'] = ['-', '+', '+', '+']
print(leisure_2020_05)

'''
#leisure 2019
result: leisure_2019_02  ~  leisure_2019_05
'''
# from leisure201902
embedding_mode = Word2Vec(leisure201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 않아(-)/결합(+)/가까워(+)/함께(+)/밤하늘(+)/앓았던(-)/단순한(+)
leisure = word()
leisure_19_02 = leisure.input_word("않아")
leisure_19_02 = leisure.input_word("결합")
leisure_19_02 = leisure.input_word("가까워")
leisure_19_02 = leisure.input_word("함께")
leisure_19_02 = leisure.input_word("밤하늘")
leisure_19_02 = leisure.input_word("앓았던")
leisure_19_02 = leisure.input_word("단순한")
leisure_2019_02 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_02))], 'target': leisure_19_02,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_02]})
leisure_2019_02['positive'] = ['-', '+', '+', '+', '+', '-', '+']
print(leisure_2019_02)

# from leisure201903
embedding_mode = Word2Vec(leisure201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 허세(-)/통증(-)/프리미엄(+)/필수(+)/좋다며(+)/해롭습니다(-)
leisure = word()
leisure_19_03 = leisure.input_word("허세")
leisure_19_03 = leisure.input_word("통증")
leisure_19_03 = leisure.input_word("프리미엄")
leisure_19_03 = leisure.input_word("필수")
leisure_19_03 = leisure.input_word("좋다며")
leisure_19_03 = leisure.input_word("해롭습니다")
leisure_2019_03 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_03))], 'target': leisure_19_03,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_03]})
leisure_2019_03['positive'] = ['-', '-', '+', '+', '+', '-']
print(leisure_2019_03)

# from leisure201904
embedding_mode = Word2Vec(leisure201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 해양(+)/받는(+)/참여(+)/재난(-)/색다른(+)/늘었다(+)/불황(-)
leisure = word()
leisure_19_04 = leisure.input_word("해양")
leisure_19_04 = leisure.input_word("받는")
leisure_19_04 = leisure.input_word("참여")
leisure_19_04 = leisure.input_word("재난")
leisure_19_04 = leisure.input_word("색다른")
leisure_19_04 = leisure.input_word("늘었다")
leisure_19_04 = leisure.input_word("불황")
leisure_2019_04 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_04))], 'target': leisure_19_04,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_04]})
leisure_2019_04['positive'] = ['+', '+', '+', '-', '+', '+', '-']
print(leisure_2019_04)

# from leisure201905
embedding_mode = Word2Vec(leisure201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 캠핑장(+)/휴식(+)/수상(+)/외식(+)/꿀맛(+)/꿀잠(+)/꿀잼(+)
leisure = word()
leisure_19_05 = leisure.input_word("캠핑장")
leisure_19_05 = leisure.input_word("휴식")
leisure_19_05 = leisure.input_word("수상")
leisure_19_05 = leisure.input_word("외식")
leisure_19_05 = leisure.input_word("꿀맛")
leisure_19_05 = leisure.input_word("꿀잠")
leisure_19_05 = leisure.input_word("꿀잼")
leisure_2019_05 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_05))], 'target': leisure_19_05,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_05]})
leisure_2019_05['positive'] = ['+', '+', '+', '+', '+', '+', '+']
print(leisure_2019_05)

'''
#stay 2020
result: stay_2020_02  ~  stay_2020_05
'''
# from stay202002
embedding_mode = Word2Vec(stay202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 함께(+)/한산한(-)/않을(-)/새로운(+)/썰렁한(-)
stay = word()
stay_20_02 = stay.input_word("함께")
stay_20_02 = stay.input_word("한산한")
stay_20_02 = stay.input_word("않을")
stay_20_02 = stay.input_word("새로운")
stay_20_02 = stay.input_word("썰렁한")
stay_2020_02 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_02))], 'target': stay_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_02]})
stay_2020_02['positive'] = ['+', '-', '-', '+', '-']
print(stay_2020_02)

# from stay202003
embedding_mode = Word2Vec(stay202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 원하는(+)/협력(+)/다양한(+)/좋다(+)/가까운(+)/최신(+)
stay = word()
stay_20_03 = stay.input_word("원하는")
stay_20_03 = stay.input_word("협력")
stay_20_03 = stay.input_word("다양한")
stay_20_03 = stay.input_word("좋다")
stay_20_03 = stay.input_word("가까운")
stay_20_03 = stay.input_word("최신")
stay_2020_03 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_03))], 'target': stay_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_03]})
stay_2020_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(stay_2020_03)

# from stay202004
embedding_mode = Word2Vec(stay202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 용이(+)/여파(-)/떨어지면서(-)/직격탄(-)/아니었다(-)/없었는데(-)/헐값(-)/많던(-)/긴장감(-)/곤란하다고(-)
stay = word()
stay_20_04 = stay.input_word("용이")
stay_20_04 = stay.input_word("여파")
stay_20_04 = stay.input_word("떨어지면서")
stay_20_04 = stay.input_word("직격탄")
stay_20_04 = stay.input_word("아니었다")
stay_20_04 = stay.input_word("없었는데")
stay_20_04 = stay.input_word("헐값")
stay_20_04 = stay.input_word("많던")
stay_20_04 = stay.input_word("긴장감")
stay_20_04 = stay.input_word("곤란하다고")
stay_2020_04 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_04))], 'target': stay_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_04]})
stay_2020_04['positive'] = ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-']
print(stay_2020_04)

# from stay202005
embedding_mode = Word2Vec(stay202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 완성(+)/외식(+)/맛집(+)/고문(-)/손실(-)/했지만(-)/적발(-)/불법(-)/사기(-)
stay = word()
stay_20_05 = stay.input_word("완성")
stay_20_05 = stay.input_word("외식")
stay_20_05 = stay.input_word("맛집")
stay_20_05 = stay.input_word("고문")
stay_20_05 = stay.input_word("손실")
stay_20_05 = stay.input_word("했지만")
stay_20_05 = stay.input_word("적발")
stay_20_05 = stay.input_word("불법")
stay_20_05 = stay.input_word("사기")
stay_2020_05 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_05))], 'target': stay_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_05]})
stay_2020_05['positive'] = ['+', '+', '+', '-', '-', '-', '-', '-', '-']
print(stay_2020_05)

'''
#stay 2019
result: stay_2019_02  ~  stay_2019_05
'''
# from stay201902
embedding_mode = Word2Vec(stay201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 편의(+)/복합(+)/최대(+)/부당(-)/어려움(-)/편리하게(+)/자유(+)
stay = word()
stay_19_02 = stay.input_word("편의")
stay_19_02 = stay.input_word("복합")
stay_19_02 = stay.input_word("최대")
stay_19_02 = stay.input_word("부당")
stay_19_02 = stay.input_word("어려움")
stay_19_02 = stay.input_word("편리하게")
stay_19_02 = stay.input_word("자유")
stay_2019_02 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_02))], 'target': stay_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_02]})
stay_2019_02['positive'] = ['-', '-', '-', '+', '-', '+', '+']
print(stay_2019_02)

# from stay201903
embedding_mode = Word2Vec(stay201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 징계(-)/슬픔(-)/모든(+)/함께(+)/사고(-)/절반(-)/어렵게(-)/
stay = word()
stay_19_03 = stay.input_word("징계")
stay_19_03 = stay.input_word("슬픔")
stay_19_03 = stay.input_word("모든")
stay_19_03 = stay.input_word("함께")
stay_19_03 = stay.input_word("사고")
stay_19_03 = stay.input_word("절반")
stay_19_03 = stay.input_word("어렵게")
stay_2019_03 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_03))], 'target': stay_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_03]})
stay_2019_03['positive'] = ['-', '-', '+', '+', '-', '-', '-']
print(stay_2019_03)

# from stay201904
embedding_mode = Word2Vec(stay201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 했지만(-)/그런데(-)/부담(-)/거절(-)/쟁점(-)/다양한(+)/최저(-)
stay = word()
stay_19_04 = stay.input_word("했지만")
stay_19_04 = stay.input_word("그런데")
stay_19_04 = stay.input_word("부담")
stay_19_04 = stay.input_word("거절")
stay_19_04 = stay.input_word("쟁점")
stay_19_04 = stay.input_word("다양한")
stay_19_04 = stay.input_word("최저")
stay_2019_04 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_04))], 'target': stay_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_04]})
stay_2019_04['positive'] = ['-', '-', '-', '-', '-', '+', '-']
print(stay_2019_04)

# from stay201905
embedding_mode = Word2Vec(stay201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 편의(+)/비용(-)/하기에는(-)/건너갔다(-)/부적절하다는(-)/폭언(-)/실종(-)/욕설(-)
stay = word()
stay_19_05 = stay.input_word("편의")
stay_19_05 = stay.input_word("비용")
stay_19_05 = stay.input_word("하기에는")
stay_19_05 = stay.input_word("건너갔다")
stay_19_05 = stay.input_word("부적절하다는")
stay_19_05 = stay.input_word("폭언")
stay_19_05 = stay.input_word("실종")
stay_19_05 = stay.input_word("욕설")
stay_2019_05 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_05))], 'target': stay_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_05]})
stay_2019_05['positive'] = ['+', '-', '-', '-', '-', '-', '-', '-']
print(stay_2019_05)