# this is just for practice and we do not use multiprocessing for I/O bound processes but for CPU bound processes
import time
import concurrent.futures

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)
        '''
        result = [executor.submit(do_something, sec) for sec in secs]
        for f in concurrent.futures.as_completed(result):
            print(f.result())
        '''
        
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 3)} second(s)")