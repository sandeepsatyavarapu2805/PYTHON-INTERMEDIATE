import asyncio
import time

# A SYNCHRONOUS FUNCTION, This represents a heavy, old-school function with NO pause buttons.
def fry_steak():
    print("[STEAK] Started frying steak... (Sync)")
    time.sleep(3)
    print("[STEAK] Steak is perfectly cooked!")
    return "Juicy Steak"

# 2. AN ASYNC FUNCTION / COROUTINE (The Smart Cake)
async def bake_cake():
    print("[CAKE]  Mixing ingredients... (Async)")
    print("[CAKE]  Putting cake in oven. Pausing to let it bake...")

    # 'await' is the pause button. Control is handed back to the Event Loop.
    await asyncio.sleep(4)

    print("[CAKE]  Ding! Cake is done!")
    return "Chocolate Cake"

# 3. THE MAIN CONTROLLER
async def main():
    loop = asyncio.get_running_loop()
    print("--- KITCHEN OPEN ---")

    # Creating a TASK: This tells the event loop to actively start baking the cake.
    cake_task = asyncio.create_task(bake_cake())
    print("[MAIN]  Cake is now baking in the background.")
    print("[MAIN]  Let's handle the heavy sync steak safely...")

    # SAFELY RUNNING SYNC IN ASYNC:
    # We use run_in_executor to throw the function onto a separate backup thread. This returns a FUTURE (a placeholder token).
    steak_future = loop.run_in_executor(None, fry_steak)
    print("[MAIN]  Steak handed off to a backup thread. Main loop is still free!")
    print("[MAIN]  Now, we wait for both items to finish...")

    # We await the Task and the Future. Because cake paused itself and steak is on a backup thread, they run at the same time!
    cake_result = await cake_task
    steak_result = await steak_future

    print("--- KITCHEN CLOSED ---")
    print(f"Served: {cake_result} and {steak_result}")

# Start the entire engine
asyncio.run(main())