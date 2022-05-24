from pandas import array
from utils import Task, Gant_chart, Ready_queue

def FCFS(tasks):
    """
    Args:
        tasks (list of Task)
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    for task in tasks:
        # 각 task 별로 waiting_time, response_time, turnaround_time 저장
        if current_time < task.arrival_time:
            none_time = task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = task.arrival_time

        task.waiting_time = current_time-task.arrival_time
        task.response_time = current_time-task.arrival_time
        current_time += task.burst_time
        task.turnaround_time = current_time-task.arrival_time

        # gant chart 기록
        gant.add(task.pid, task.burst_time)
            
    return gant

def SJF(tasks):
    """
    Args:
        tasks (list of Task)
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)

        current_task.waiting_time = current_time-current_task.arrival_time
        current_task.response_time = current_time-current_task.arrival_time
        current_time += current_task.burst_time
        current_task.turnaround_time = current_time-current_task.arrival_time
        gant.add(current_task.pid, current_task.burst_time)

        while tasks:
            if tasks[0].arrival_time <= current_time:
                task = tasks.pop(0)
                ready_queue.insert_process(task, key=lambda x: (x.burst_time))
            else:
                break

    return gant

def SRTF(tasks):
    """
    Args:
        tasks (list of Task)
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)
        
        if tasks and (tasks[0].arrival_time < current_time+current_task.burst_time):
            task = tasks.pop(0)
            used_time = task.arrival_time-current_time
            current_task.burst_time -= used_time
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= used_time
            current_time = task.arrival_time
            gant.add(current_task.pid, used_time)

            ready_queue.insert_process(current_task, key=lambda x: (x.burst_time))
            ready_queue.insert_process(task, key=lambda x: (x.burst_time))
        else:
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time += current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
    
    return gant

def RR(tasks, t_q):
    """
    Args:
        tasks (list of Task)
        t_q (float) : time_quantum
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)

        if current_task.burst_time <= t_q:
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time += current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
            current_task.burst_time = 0
        else:
            current_task.burst_time -= t_q
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= t_q
            current_time += t_q
            gant.add(current_task.pid, t_q)

        while tasks:
            # 우선은 먼저 새로 들어온 process 먼저 ready queue로
            if tasks[0].arrival_time <= current_time:
                task = tasks.pop(0)
                ready_queue.insert_process(task, key=None)
            else:
                break
        if current_task.burst_time != 0:
            ready_queue.insert_process(current_task, key=None)

    return gant

def priority(tasks):
    """
    Args:
        tasks (list of Task)
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)

        current_task.waiting_time = current_time-current_task.arrival_time
        current_task.response_time = current_time-current_task.arrival_time
        current_time += current_task.burst_time
        current_task.turnaround_time = current_time-current_task.arrival_time
        gant.add(current_task.pid, current_task.burst_time)

        while tasks:
            if tasks[0].arrival_time <= current_time:
                task = tasks.pop(0)
                ready_queue.insert_process(task, key=lambda x: (x.priority))
            else:
                break
    
    return gant 

def preemptive_priority(tasks):
    """
    Args:
        tasks (list of Task)
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)
        
        if tasks and (tasks[0].arrival_time < current_time+current_task.burst_time):
            task = tasks.pop(0)
            used_time = task.arrival_time-current_time
            current_task.burst_time -= used_time
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= used_time
            current_time = task.arrival_time
            gant.add(current_task.pid, used_time)

            ready_queue.insert_process(current_task, key=lambda x: (x.priority))
            ready_queue.insert_process(task, key=lambda x: (x.priority))
        else:
            current_task.waiting_time += current_time-current_task.arrival_time
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
    
    return gant

def priority_RR(tasks, t_q):
    """
    Args:
        tasks (list of Task)
        t_q (float) : time quantum
    """
    # arrival_time 기준으로 sorting.
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = 0

    # ready_queue 생성
    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
            none_time = current_task.arrival_time - current_time
            gant.add(None, none_time)
            current_time = current_task.arrival_time
        else:
            current_task = ready_queue.pop(0)
        
        if current_task.burst_time <= t_q:            
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time += current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
            current_task.burst_time = 0
        else:
            current_task.burst_time -= t_q
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= t_q
            current_time += t_q
            gant.add(current_task.pid, t_q)

        while tasks:
            # 우선은 먼저 새로 들어온 process 먼저 ready queue로
            if tasks[0].arrival_time <= current_time:
                task = tasks.pop(0)
                ready_queue.insert_process(task, key=lambda x: (x.priority))
            else:
                break

        if current_task.burst_time != 0:
            ready_queue.insert_process(current_task, key=lambda x: (x.priority))

    return gant

if __name__ == "__main__":
    from utils import get_AWT, get_ART, get_ATT
    processes_sample = []
    processes_sample.append(Task(0, 1, 3, 4))
    processes_sample.append(Task(1, 1, 2, 3))
    processes_sample.append(Task(2, 7, 2, 2))
    # processes_sample.append(Task(3, 5, 5, 2))
    # processes_sample.append(Task(0, 0, 7, 4))
    # processes_sample.append(Task(1, 2, 4, 3))
    # processes_sample.append(Task(2, 4, 1, 2))
    # processes_sample.append(Task(3, 5, 4, 2))
    
    # gant = FCFS(processes_sample)
    # gant = SJF(processes_sample)
    # gant = SRTF(processes_sample)
    # gant = RR(processes_sample,1)
    # gant = priority(processes_sample)
    gant = preemptive_priority(processes_sample)
    # gant = priority_RR(processes_sample,1)
    gant.draw()

    print("AWT: ", get_AWT(processes_sample))
    print("ART: ", get_ART(processes_sample))
    print("ATT: ", get_ATT(processes_sample))

    
    

    # print("mean_waiting_time\t", np.mean(mean_waiting_time),mean_waiting_time)
    # print("mean_turnaround_time\t", np.mean(mean_turnaround_time),mean_turnaround_time)
    # print("mean_response_time\t", np.mean(mean_response_time),mean_response_time)
    # print("gant", gant)

    # processes_sample = np.array([[0,0,11], [1,5,28], [2,12,2], [3,2,10], [4,9,16]])