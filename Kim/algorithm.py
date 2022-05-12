from utils import Task, Gant_chart, Ready_queue

def FCFS(tasks):
    """
    """
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    for task in tasks:
        task.waiting_time = current_time-task.arrival_time
        task.response_time = current_time-task.arrival_time
        current_time += task.burst_time
        task.turnaround_time = current_time-task.arrival_time
        gant.add(task.pid, task.burst_time)

    gant.rearrange()
    return gant

def SJF(tasks):
    """
    """
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
           current_task = tasks.pop(0)
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
    
    gant.rearrange()
    return gant

def SRTF(tasks):
    """
    """
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
           current_task = tasks.pop(0)
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
    
    gant.rearrange()
    return gant

def RR(tasks, t_q):
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    while tasks:
        current_task = tasks.pop(0)
        if current_task.burst_time <= t_q:
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time += current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
        else:
            current_task.burst_time -= t_q
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= t_q
            current_time += t_q
            gant.add(current_task.pid, t_q)

            tasks.append(current_task)

    gant.rearrange()
    return gant

def priority(tasks):
    """
    """
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
           current_task = tasks.pop(0)
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
    
    gant.rearrange()
    return gant 

def preemptive_priority(tasks):
    """
    """
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
           current_task = tasks.pop(0)
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
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
    
    gant.rearrange()
    return gant

def priority_RR(tasks, t_q):
    tasks = sorted(tasks, key = lambda x: (x.arrival_time))
    gant = Gant_chart()
    current_time = tasks[0].arrival_time
    gant.start(current_time)

    ready_queue = Ready_queue()
    while ready_queue or tasks:
        if not ready_queue:
            current_task = tasks.pop(0)
        else:
            current_task = ready_queue.pop(0)
        
        if current_task.burst_time <= t_q:            
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time += current_time-current_task.arrival_time
            current_time += current_task.burst_time
            current_task.turnaround_time = current_time-current_task.arrival_time
            gant.add(current_task.pid, current_task.burst_time)
            # current_task 종료
            current_task = None
        else:
            current_task.burst_time -= t_q
            if current_task.response_time is None:
                current_task.response_time = current_time-current_task.arrival_time
            current_task.waiting_time -= t_q
            current_time += t_q
            gant.add(current_task.pid, t_q)

        while tasks:
            if tasks[0].arrival_time <= current_time:
                task = tasks.pop(0)
                ready_queue.insert_process(task, key=lambda x: (x.priority))
        if current_task:
            ready_queue.insert_process(current_task, key=lambda x: (x.priority))

    gant.rearrange()
    return gant

if __name__ == "__main__":
    from utils import get_AWT, get_ART, get_ATT
    processes_sample = []
    processes_sample.append(Task(0, 0, 10, 4))
    processes_sample.append(Task(1, 2, 3, 3))
    processes_sample.append(Task(2, 3, 7, 2))
    processes_sample.append(Task(3, 5, 5, 2))
    # processes_sample.append(Task(0, 0, 7, 4))
    # processes_sample.append(Task(1, 2, 4, 3))
    # processes_sample.append(Task(2, 4, 1, 2))
    # processes_sample.append(Task(3, 5, 4, 2))
    
    gant = SRTF(processes_sample)
    gant.draw()

    print("AWT: ", get_AWT(processes_sample))
    print("ART: ", get_ART(processes_sample))
    print("ATT: ", get_ATT(processes_sample))

    
    

    # print("mean_waiting_time\t", np.mean(mean_waiting_time),mean_waiting_time)
    # print("mean_turnaround_time\t", np.mean(mean_turnaround_time),mean_turnaround_time)
    # print("mean_response_time\t", np.mean(mean_response_time),mean_response_time)
    # print("gant", gant)

    # processes_sample = np.array([[0,0,11], [1,5,28], [2,12,2], [3,2,10], [4,9,16]])