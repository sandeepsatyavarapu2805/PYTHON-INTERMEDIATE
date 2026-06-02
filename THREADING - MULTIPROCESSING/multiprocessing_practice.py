# this is just for practice and we do not use multiprocessing for I/O bound processes but for CPU bound processes
import multiprocessing, time

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print(f"Done Sleeping...{seconds}")

if __name__ == "__main__":
    start = time.perf_counter()

    processes = []

    for _ in range(10):
        t = multiprocessing.Process(target=do_something, args=[1])
        processes.append(t)
        t.start()

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 3)} second(s)")