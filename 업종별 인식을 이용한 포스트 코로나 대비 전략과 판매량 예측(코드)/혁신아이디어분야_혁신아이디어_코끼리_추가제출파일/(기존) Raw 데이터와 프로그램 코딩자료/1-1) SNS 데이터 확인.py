# 1-1) SNS 데이터 확인 ================================================================================

import csv
import pandas as pd

data = pd.read_csv("C:/data/2020 bigcontest data_wisenut.csv", delimiter='')
display(data)
type(data)

# 구+행정동에 대한 화제어
# 서울 중구
s_j = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][0:13]
# 서울 노원구
s_n = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][13:18]
# 대구 수성구
d_s = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][18:29]
# 대구 중구
d_j = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][29:35]


# 2019년 월별 업종1에 대한 긍정게시량
for i in range(2,6):
  x='UP1_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종2에 대한 긍정게시량
for i in range(2,6):
  x='UP2_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종3에 대한 긍정게시량
for i in range(2,6):
  x='UP3_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종4에 대한 긍정게시량
for i in range(2,6):
  x='UP4_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종5에 대한 긍정게시량
for i in range(2,6):
  x='UP5_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종6에 대한 긍정게시량
for i in range(2,6):
  x='UP6_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종1에 대한 긍정게시량
for i in range(2,6):
  x='UP1_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종2에 대한 긍정게시량
for i in range(2,6):
  x='UP2_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종3에 대한 긍정게시량
for i in range(2,6):
  x='UP3_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종4에 대한 긍정게시량
for i in range(2,6):
  x='UP4_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종5에 대한 긍정게시량
for i in range(2,6):
  x='UP5_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종6에 대한 긍정게시량
for i in range(2,6):
  x='UP6_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])


# 2019년 월별 업종1에 대한 부정게시량
for i in range(2,6):
  x='UP1_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종2에 대한 부정게시량
for i in range(2,6):
  x='UP2_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종3에 대한 부정게시량
for i in range(2,6):
  x='UP3_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종4에 대한 부정게시량
for i in range(2,6):
  x='UP4_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종5에 대한 부정게시량
for i in range(2,6):
  x='UP5_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종6에 대한 부정게시량
for i in range(2,6):
  x='UP6_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종1에 대한 부정게시량
for i in range(2,6):
  x='UP1_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종2에 대한 부정게시량
for i in range(2,6):
  x='UP2_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종3에 대한 부정게시량
for i in range(2,6):
  x='UP3_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종4에 대한 부정게시량
for i in range(2,6):
  x='UP4_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종5에 대한 부정게시량
for i in range(2,6):
  x='UP5_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종6에 대한 부정게시량
for i in range(2,6):
  x='UP6_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])
