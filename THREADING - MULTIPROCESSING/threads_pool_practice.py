import time
import concurrent.futures

start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) # so this returns the return value and waits to print till the first is fully executed

    # this returns a future object which runs when and does not print the retuen statement until it reaches f.result
    '''
    result = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(result):
        print(f.result())
    '''
    
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 3)} second(s)')