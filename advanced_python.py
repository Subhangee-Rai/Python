# # ASYNCIO
# import time
# import asyncio
#
# async def func1():
#     await asyncio.sleep(4)
#     print("Hello func1")
#     return "func 1"
#
# async def func2():
#     await asyncio.sleep(2)
#     print("Hello func2")
#     return "func 2"
#
# async def func3():
#     await asyncio.sleep(3)
#     print("Hello func3")
#     return "func 3"
#
# async def main():
#     # to run all functions together or parallel
#     # L = await asyncio.gather(func1(),func2(),func3())
#     # print(L)
#
#     # To run functions one after other
#     await func1()
#     await func2()
#     await func3()
#     return 3
#
# asyncio.run(main())

# -----------------------------------------------------------------------------------
# # Multithreading
# import threading
# import time
#
# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#
# # runs one after other
# # time1 = time.perf_counter()
# # func(4)
# # func(2)
# # func(1)
# # time2 = time.perf_counter()
#
# # to run in parallel : runs at once
# time1 = time.perf_counter()
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(f"Performance:{time2-time1}")


# -----------------------------------------------------------------------------------
# Multiprocessing
import multiprocessing

def funct(val):
    for i in val:
        print(f"Value is {i}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=funct, args=([20, 10],))
    p.start()
    p.join()  # This ensures the main program waits for the subprocess to finish
