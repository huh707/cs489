import csv
import random
#note1
#globalvariable
q_1st = []
q_2nd = []
adder = 0


#note2
#1st_function
#�� ����� 1��°�� ��� ���� �������� �Ѽ�Ʈ (3��), 2��°�� ��� ���� �������� �� ��Ʈ (3��) list�� ����� �Լ�, 1��°�� ��հ� ����, 2��°�� �츮�� ����ġ ���� ����

def ran_qlist():
    
    #for������   
    for i in range(3):    
        if i == 0:
            numb = 0
            adder = 7
        elif i == 1:
            numb = 8
            adder = 7
        else:
            numb = 16
            adder = 9
            
        ran_num = random.randint(numb,numb+adder)
        q_1st.append(ran_num) 
    
        for j in range(1):
            while ran_num in q_1st:
                ran_num = random.randint(numb,numb+adder)
            q_2nd.append(ran_num)
    #for����    
    return q_1st,q_2nd


#note3
#globalvariable
dil = []



#dilema csv �о�ͼ� dilema �κи� ����
#dil �� dilema�� ��� list

with open('./cs489/dilema.csv','r') as f: 
    reader = csv.reader(f)
    for row in reader:
        dil.append(row[2])


#note4
#2nd_function
#���� ������ ��ȣ�� ���� ������ return   
def q_out(z):
    return dil[z]

#note5
#����,���̴�,�������� ���� ������ �׷� �������� �� �׷캰�� list�� ��������.
#db�� ��� ���÷� ���� �κ�
M2S = []
with open('./cs489/20_male_student.csv','r') as f: 
    read = csv.reader(f)
    for row in read:
        M2S.append([row[0],row[1],row[2]])
print(M2S)



#note6
#3rd_function
#��������ȣ, ��� ����(list�̸�����) input���� ������ �� ������ �ش� ������ ���� ��� return
#x�� ������ȣ, L�� ��� ������ list
def qavg(x,L):
    M = []
    for i in range(len(L)):
        if int(L[i][0]) == x:
            M.append(int(L[i][1]))
    if len(M) != 0:
        AVG = (sum(M,0.0)/len(M))
        RAVG = round(AVG,2)
    else:
        return "�ش� ������ ���� �����Ͱ� ����, ����� ���� �� �����ϴ�."
    return RAVG




#note7
#globalvariable
peo_ans = dict()


#4th function
#� ������ ������ ���� �� ����� ����� ����, �� ������ ��� ������ ������ �����ִ� �Լ�.
#idd�� �׻�� id, x�� ������ȣ, L�� �� ����� ���� list
#��� �� �� ���� ������ csv�� �����ϰ�, �Ʒ��� diff �Լ� �����������. 

def diff(x,L,idd):
    N = []
    dif = 0.0
    if idd in peo_ans:
        N = peo_ans[idd]
    else:
        peo_ans[idd] = N
    
    avgg = qavg(x,L)
    
    for i in range(len(M2S)):
        if int(M2S[i][0]) == x:
            if str(M2S[i][2]) == str(idd):
                dif = float(M2S[i][1]) - avgg
                N.append(dif)
    return N






#note8
#5th function
#4th function���� ���� list�� �������� �ش� ������ ���� ���� �亯 ����

def pred(x,L,idd):
    avgg = qavg(x,L)
    cate = 0
    
    if x < 8:
        cate = 0
    elif 8 <= x and x < 16 :
        cate = 1
    else:
        cate = 2
    
    P = peo_ans[idd]
    differ = P[cate] + avgg
    pre = round(differ)
    if 0 < pre and pre < 6:
        return pre
    elif pre < 1:
        return 1
    else:
        return 5
    