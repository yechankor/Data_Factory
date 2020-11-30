# 3-1) PN 변수 계산

# 19년 2월 숙박관련 정보
PN = stay_2019_02['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('{}'.format(PN[6]))
    
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average

# 19년 3월 숙박 PN 계산 ===============================================================================
PN = stay_2019_03['vector'] 
vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 숙박 PN 계산 ===============================================================================
PN = stay_2019_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 숙박 PN 계산 ===============================================================================
PN = stay_2019_05['vector']

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 숙박 PN 계산 ===============================================================================
PN = stay_2020_02['vector']

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 숙박 PN 계산 ===============================================================================

PN = stay_2020_03['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 숙박 PN 계산 ===============================================================================

PN = stay_2020_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 숙박 PN 계산 ===============================================================================
PN = stay_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 문화취미 PN 계산 ==========================================================================
PN = cul_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_03['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('+{}'.format(PN[10]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('+{}'.format(PN[10]))
    elif i == PN[11]:
        vec.append('-{}'.format(PN[11]))
    elif i == PN[12]:
        vec.append('+{}'.format(PN[12]))
    elif i == PN[13]:
        vec.append('+{}'.format(PN[13]))
    elif i == PN[14]:
        vec.append('+{}'.format(PN[14]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 푸드 PN 계산 ==========================================================================

PN = food_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 푸드 PN 계산 ==========================================================================
PN = food_2019_03['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 푸드 PN 계산 ==========================================================================
PN = food_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 푸드 PN 계산 ==========================================================================
PN = food_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average

#==========================================================================================
# 20년 2월 푸드관련 정보
PN = food_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 푸드 PN 계산 ==========================================================================
PN = food_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 푸드 PN 계산 ==========================================================================

PN = food_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 푸드 PN 계산 ==========================================================================


PN = food_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 의료기관 PN 계산 ==========================================================================
PN = medi_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 의료기관 PN 계산 ==========================================================================

PN = medi_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 의료기관 PN 계산 ==========================================================================
PN = medi_2019_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 의료기관 PN 계산 ==========================================================================

PN = medi_2019_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_02['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('-{}'.format(PN[10]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 보건위생 PN 계산 ==========================================================================

PN = health_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 보건위생 PN 계산 ==========================================================================
PN = health_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 보건위생 PN 계산 ==========================================================================
PN = health_2019_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 보건위생 PN 계산 ==========================================================================
PN = health_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 보건위생 PN 계산 ==========================================================================
PN = health_2020_02['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 보건위생 PN 계산 ==========================================================================
PN = health_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 보건위생 PN 계산 ==========================================================================
PN = health_2020_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 보건위생 PN 계산 ==========================================================================

PN = health_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 레저 PN 계산 ==========================================================================

PN = leisure_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 레저 PN 계산 ==========================================================================

PN = leisure_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 레저 PN 계산 ==========================================================================

PN = leisure_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 레저 PN 계산 ==========================================================================

PN = leisure_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 레저 PN 계산 ==========================================================================

PN = leisure_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 레저 PN 계산 ==========================================================================

PN = leisure_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 레저 PN 계산 ==========================================================================

PN = leisure_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 레저 PN 계산 ==========================================================================

PN = leisure_2020_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average