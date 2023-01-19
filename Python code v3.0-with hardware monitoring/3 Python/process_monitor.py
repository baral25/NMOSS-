import psutil
import time 
from prettytable import PrettyTable
# Fetch the last 10 processes from available processes
print("----Processes----")
process_table = PrettyTable(['PID', 'PNAME', 'STATUS','CPU', 'NUM THREADS'])
for process in psutil.pids()[-20:]:

        # While fetching the processes, some of the subprocesses may exit 
        # Hence we need to put this code in try-except block
        try:
            p = psutil.Process(process)
            process_table.add_row([
                str(process),
                p.name(),
                p.status(),
                str(p.cpu_percent())+"%",
                p.num_threads()
                ])
              
        except Exception as e:
            pass
print(process_table)
  
    # Create a 1 second delay
time.sleep(1)