

"""
process = [] 

res = []

"""



process=[
    ['P1', 0, 5],
    ['P2', 1, 9],
    ['P3', 2, 3],
    ['P4', 3, 4],
    ['P5', 4, 5]
]
res = []



def avg_wt_tat(data):
    for dct in data:
        dct['tat'] = dct['ct'] - dct['at']
        dct['wt'] = dct['tat'] - dct['bt']
    tot_wt = tot_tat = 0
    for dct in data:
        tot_wt += dct['wt']
        tot_tat += dct['tat']
    ln = len(data)
    return {'avg_tat': tot_tat/ln, 'avg_wt': tot_wt/ln}

def priority_non_preemptive(data):
    def has_arrived(lst, curr_time, index):
        for i in lst:
            if i[-1] == index:
                if i[1] <= curr_time:
                    return True
        return False
    prior = []
    indx = 0
    curr_time = 0
    for i in data:
        prior.append([i['pr'], i['at'], i['bt'], indx])
        indx += 1
    prior.sort(reverse=True)
    while prior:
        for val in prior:
            if has_arrived(prior, curr_time, val[-1]):
                curr_time += val[2]
                data[val[-1]]['ct'] = curr_time
                prior.remove(val)
    return data

  
  
  def priority_preemptive(data):
    def find_max_prior_arrived(curr_time, lst):
        lst.sort(reverse=True)
        for i in lst:
            if curr_time >= i[1]:
                return i[-1], True

    def all_done(lst):
        for i in lst:
            if i[2] != 0:
                return False
        return True

    def reduce_bt(indx, lst):
        for i in range(len(lst)):
            if lst[i][-1] == indx:
                lst[i][2] -= 1
                if lst[i][2] == 0:
                    del lst[i]
                    return lst, True
        return lst, False
    prior = []
    indx = 0
    curr_time = 0
    for i in data:
        prior.append([i['pr'], i['at'], i['bt'], indx])
        indx += 1
    prior.sort(reverse=True)
    while not all_done(prior):
        index, has_arrived = find_max_prior_arrived(curr_time, prior)
        if has_arrived:
            curr_time += 1
            prior, is_done = reduce_bt(index, prior)
            if is_done:
                data[index]['ct'] = curr_time
    return data






prirun = 0
run = 0


for a in range(0, len(process)) :
    res.append([])
    res[0].append(process[a][0])
    run += prirun
    arrive = process[a][1]
    waittime=run-arrive
    res.append([])
    res[1].append(waittime)
    returntime = waittime + process[a][2]
    res.append([])
    res[2].append(returntime)
    prirun = process[a][2]


for p in range(0, len(process)) :
    print(res[0][p], "  //  waiting time : ", res[1][p] ,"\t", "return time : ", res[2][p])




def shortest_job_first(data):
    sjf = []
    indx = 0
    curr_time = 0
    for dct in data:
        sjf.append([dct['bt'], dct['at'], indx])
        indx += 1
    sjf.sort()
    while sjf:
        for val in sjf:
            if val[1] <= curr_time:
                curr_time += data[val[2]]['bt']
                data[val[2]]['ct'] = curr_time
                sjf.remove(val)
    return data
  
  def round_robin(data, tq):
    rr = []
    indx = 0
    curr_time = 0
    flag = True
    for dct in data:
        rr.append([dct['at'], dct['bt'], indx])
        indx += 1
    while flag:
        for i in range(len(rr)):
            bt = rr[i][1]
            if bt != 0 and rr[i][0] < curr_time or curr_time == 0:
                if bt > tq:
                    rr[i][1] -= tq
                    curr_time += tq
                else:
                    rr[i][1] = 0
                    curr_time += bt
                    data[rr[i][2]]['ct'] = curr_time
        flg = True
        for i in rr:
            if not i[1] == 0:
                flg = False
        if flg:
            flag = False
    return data
  
  
  def shortest_remaining_time(data):
    def find_min_rt_arrived(curr_time, lst):
        lst.sort(key=lambda x: x[1])
        for i in lst:
            if curr_time >= i[0]:
                return i[2], True

    def all_done(lst):
        for i in lst:
            if i[1] != 0:
                return False
        return True

    def reduce_bt(indx, lst):
        for i in range(len(lst)):
            if lst[i][-1] == indx:
                lst[i][1] -= 1
                if lst[i][1] == 0:
                    del lst[i]
                    return lst, True
        return lst, False
    srtf = []
    indx = 0
    curr_time = 0
    for dct in data:
        srtf.append([dct['at'], dct['bt'], indx])
        indx += 1
    srtf.sort()
    while not all_done(srtf):
        index, has_arrived = find_min_rt_arrived(curr_time, srtf)
        if has_arrived:
            curr_time += 1
            srtf, is_done = reduce_bt(index, srtf)
            if is_done:
                data[index]['ct'] = curr_time
    return data

  

