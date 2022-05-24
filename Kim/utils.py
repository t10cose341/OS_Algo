class Task:    
    """ 
    Args:
        pid (int or str): process ID
        arrival_time (float): arrival_time
        burst_time (float): burst_time
        priority (None Or int): priority
    """
    def __init__(self, pid, arrival_time, burst_time, priority=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        if priority:
            self.priority = priority
        
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = None
    
    def __str__(self):
        return str(self.pid)

class Gant_chart:
    def __init__(self):
        self.pids = []
        self.used_times = []
        self.start_time = 0
    
    def start(self, start_time):
        """processor 사용 시작 시점 기록.
        Args:
            start_time (float): 시작 시점
        """
        if start_time:
            raise
        else:
            self.start_time = start_time

    def add(self, pid, used_time):
        """ 현재 사용한 pid와 burst_time 저장
        Args:
            pid (int or str): process ID
            used_time (float): used_time
        """
        if used_time == 0:
            pass
        else:
            if len(self.pids) == 0:
                self.pids.append(pid)
                self.used_times.append(used_time)
            elif self.pids[-1] == pid:
                self.used_times[-1] += used_time
            else:
                self.pids.append(pid)
                self.used_times.append(used_time)

    def draw(self):
        """ (임시)gant chart 출력
        """
        print("|", end='')
        for time in self.used_times:
            print("-"*time, end='|')
        print()
        for pid, time in zip(self.pids, self.used_times):
            print(pid, end='')
            print(" "*time, end='')
        print()

class Ready_queue(list):
    """
    process를 정해진 우선순위에 따라 정렬하면서 사용하기 위한 ready_queue.
    """
    def insert_process(self, process, key):
        # 늦게 들어온 process를 더 뒤로 배치
        insert_check = 0
        for i in reversed(range(len(self))):
            if key(self[i]) > key(process):
                continue
            else:
                self.insert(i+1, process)
                insert_check = 1
                break
        if insert_check==0:
            self.insert(0, process)

# 각종 average time 계산 함수

def get_AWT(tasks):
    return sum([task.waiting_time for task in tasks])/len(tasks)

def get_ART(tasks):
    return sum([task.response_time for task in tasks])/len(tasks)

def get_ATT(tasks):
    return sum([task.turnaround_time for task in tasks])/len(tasks)