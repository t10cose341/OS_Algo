class Task:
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
        self.start_time = start_time

    def add(self, pid, used_time):
        self.pids.append(pid)
        self.used_times.append(used_time)

    def rearrange(self):
        new_pids = []
        new_times = []
        pre_pid = None
        for pid, time in zip(self.pids, self.used_times):
            if time==0 or pre_pid==pid:
                pass
            else:
                new_pids.append(pid)
                new_times.append(time)

            pre_pid = pid

        self.pids = new_pids
        self.used_times = new_times

    def draw(self):
        print("|", end='')
        for time in self.used_times:
            print("-"*time, end='|')
        print()
        for pid, time in zip(self.pids, self.used_times):
            print(pid, end='')
            print(" "*time, end='')
        print()

class Ready_queue(list):
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


def get_AWT(tasks):
    return sum([task.waiting_time for task in tasks])/len(tasks)

def get_ART(tasks):
    return sum([task.response_time for task in tasks])/len(tasks)

def get_ATT(tasks):
    return sum([task.turnaround_time for task in tasks])/len(tasks)