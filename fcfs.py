# python Coding .. program of FCFS process

def banner():
    print("""
\t /$$$$$$$$ /$$$$$$ /$$$$$$$$ /$$$$$$ 
\t| $$_____/|_  $$_/| $$_____//$$__  $$
\t| $$        | $$  | $$     | $$  \ $$
\t| $$$$$     | $$  | $$$$$  | $$  | $$
\t| $$__/     | $$  | $$__/  | $$  | $$
\t| $$        | $$  | $$     | $$  | $$
\t| $$       /$$$$$$| $$     |  $$$$$$/
\t|__/      |______/|__/      \______/ 
                                                                          
 \t __         __           __         __            
\t|_. _ _|_  /   _  _  _  |_. _ _|_  (_  _ _   _ _| 
\t| || _)|_  \__(_)|||(-  | || _)|_  __)(-| \/(-(_| 
                                                  

""")
# banner text    
def main():
    # Start
    banner()
    names_of_process = True
    all_process = []
    count_prc=0
    print("[+] Type Process Name and Press -Enter-\nFor End Process Names Press -00-")
    while names_of_process :
        process_names = str(input("PROCESS NAME * %s:"%(count_prc)))
        count_prc += 1
        all_process.append(process_names)
        if process_names == "00":
            names_of_process = False
        else:
            pass
    all_process.pop(-1) # it was delete end index "00"
    print("Process :"+str(all_process))
    # Go To Main Processing
    count_arrival = True
    count_arrival_time = len(all_process)
    list_arrival_time = []
    while count_arrival:
        for prc_v in range(count_arrival_time):
            arrival_times = str(input("[*]Arrival time for {%s}:"%(all_process[prc_v]))) # "prc_v" mean process value
            list_arrival_time.append(arrival_times)
            if len(list_arrival_time) >= count_arrival_time:
                count_arrival = False
            else:
                pass
    
    # Now We Should set CPU Time in program
    count_cpu_time = True
    list_cpu_time = []
    while count_cpu_time:
        for cpu_v in range(len(all_process)):
            cpu_time_value = str(input("[#]CPU TIME for {%s}:"%(all_process[cpu_v]))) # "cpu_v" mean cpu value
            list_cpu_time.append(cpu_time_value)
            if len(list_cpu_time) >= len(all_process):
                count_cpu_time = False
            else:
                pass
    
    for arr_id in range(len(list_arrival_time)): # Set arrival time value to integer
        list_arrival_time[arr_id]=int(list_arrival_time[arr_id])
        
    for cpu_id in range(len(list_cpu_time)): # Set Cpu time value to integer
        list_cpu_time[cpu_id]=int(list_cpu_time[cpu_id])
    
    # Good, set requirments values
    # all_process       = process names
    # list_arrival_time = arrival times
    # list_cpu_time     = cpu times
    # ... 
    
    all_process_count = len(all_process)
    list_cpu_sum = sum(list_cpu_time)
    
    sum_wating_job = []
    end_job = [] 
    first_end = []
    average_list = []
    average_list1 = []
    all_end_list = []
    all_arrival_list = []
    
    try:
        fatime = min(list_arrival_time) # First Arrival Time 
        try:
            fctime = list_cpu_time[fatime] # First CPU Time
        except:
            fctime = 0
    except:
        fatime = 0
    
    end_time = fatime + fctime
    
    for first_come in range(len(all_process)):
        first_arrival_time = min(list_arrival_time) # First Arrival Time  
        first_index = list_arrival_time.index(first_arrival_time) 
        
        prc_job = all_process[first_index] # First Process ID 
        first_cpu_time = list_cpu_time[first_index] # First CPU Time 
        
        first_end.append(fatime) 
        end_time_true = first_end[0] + first_cpu_time 
        fatime = end_time_true 
        x_y1 = "-"*50
        info = f"""
              {x_y1}
              Process:{prc_job}
              Arrival Time:{first_arrival_time}
              CPU Time:{first_cpu_time}
              END:{end_time_true}"""
        print(str(info))
        end_job.append(end_time_true)
        all_end_list.append(end_time_true) 
        all_arrival_list.append(first_arrival_time)
        
        # Now We Should Reset Values
        list_arrival_time.pop(first_index) 
        all_process.pop(first_index) 
        list_cpu_time.pop(first_index)
        first_end.pop(0) 
        first_start_job = 1
        # Finish ...sd
        #################################################
        throughput = all_process_count / list_cpu_sum # 1
    for xxx in range(len(end_job)):
        result_mines = end_job[xxx] - all_arrival_list[xxx]
        average_list.append(int(result_mines)) 
    average_return_time = sum(average_list) / all_process_count # 2
    ###############################################################
    end_job.pop(-1) # Delete End Index
    all_arrival_list.pop(0) #
    for wait_time in range(all_process_count - 1):
        # result of { 'End jobs' Mines 'arrival times'}
        end_ = int(end_job[wait_time])
        arr_ = int(all_arrival_list[wait_time])
        result_mines1 = (end_ - arr_)
        sum_wating_job.append(int(result_mines1))
    all_jobs = int(all_process_count)
    final_result = int(sum(sum_wating_job)) / all_jobs # 3
    ###############################################
    x_y = "="*30
    info2 = f"""
        {x_y}
        Throughput:{throughput}
        Average Return Time:{average_return_time}
        Average Wating Time:{ final_result}
        {x_y}
        """
    print(info2)
    print("Count All jobs:" + str(all_process_count))
    
    inp = input("Press Enter to Exit\nPress 1 to Reload")
    if inp == "1":
        import os
        try:
            os.system("cls")
        except:
            os.system("clear")            
        main()
    else:
        pass
main()
def get_wating():
    end_job.pop(-1) # Delete End Index
    arrival_times.pop(0) #
    for wait_time in range(all_process):
        # result of { 'End jobs' Mines 'arrival times'}
        result_mines1 = int(end_job[wait_time]) - int(arrival_times[wait_time])
        sum_wating_job.append(int(result_mines1))
    all_jobs = int(len(all_process))
    final_result = int(sum(sum_wating_job)) / all_jobs
        
    
    
    
    
    
    
    
    
    