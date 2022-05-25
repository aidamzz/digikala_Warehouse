import numpy as np
n, m = map(int,input().split(' '))
l = []
for i in range(n):
    s = map(int, input().split(' '))
    s = list(s)
    l.append(s)

def maxsatr(m):
    p = []
    m_mat = np.matrix(m)
    m_t = m_mat.transpose()
    for i in range(len(m)):
        ma = max(m[i])
        if m[i].count(ma) > 1:
            a = indices(m[i], ma)
            m_tlist = m_t.tolist()
            k = a[0]
            for j in a:
                if max(m_tlist[j])== ma:
                    k = j
        else:
            k = m[i].index(ma)
        p.append(k)
    return p

        
            
def indices(lst, item):
   return [i for i, x in enumerate(lst) if x == item]


mat = np.matrix(l)
mat_t = mat.transpose()
mat_tlist = mat_t.tolist()
satr = mat.max(0)
satr_index = maxsatr(mat_tlist)

satr = satr.tolist()
satr = satr[0]

sotun = mat.max(1)

sotun = sotun.tolist()
sotun_index = maxsatr(l)

mat_list = list(mat)
r = 0
for i in range(n):
    for j in range(m):

        if l[i][j] != 1:
            if l[i][j] != 0:

                if j != sotun_index[i]:
                    if i != satr_index[j]:

                        r += l[i][j] -1
print(r)