import random
import time
import types

def stress_test(fun):
    if not isinstance(fun, types.FunctionType):
        print("Function must be of type function")
        return

    print("Generating random numbers...")
    input1 = sorted([random.randint(1, 10000) for _ in range(125)], reverse=True)
    input2 = sorted([random.randint(1, 10000) for _ in range(250)], reverse=True)
    input3 = sorted([random.randint(1, 10000) for _ in range(500)], reverse=True)
    input4 = sorted([random.randint(1, 10000) for _ in range(1000)], reverse=True)
    input5 = sorted([random.randint(1, 10000) for _ in range(2000)], reverse=True)
    input6 = sorted([random.randint(1, 10000) for _ in range(4000)], reverse=True)
    input7 = sorted([random.randint(1, 10000) for _ in range(8000)], reverse=True)
    input8 = sorted([random.randint(1, 100000) for _ in range(16000)], reverse=True)
    input9 = sorted([random.randint(1, 100000) for _ in range(32000)], reverse=True)
    input10 = sorted([random.randint(1, 100000) for _ in range(64000)], reverse=True)
    input11 = sorted([random.randint(1, 1000000) for _ in range(128000)], reverse=True)
    input12 = sorted([random.randint(1, 1000000) for _ in range(256000)], reverse=True)
    input13 = sorted([random.randint(1, 1000000) for _ in range(512000)], reverse=True)
    input14 = sorted([random.randint(1, 10000000) for _ in range(1024000)], reverse=True)




    inputs = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13, input14]
    total_times = []

    for i in range(len(inputs)):
        start_time = time.time()
        print(f"Running stress test {i + 1}...")
        fun(inputs[i])
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_times.append(elapsed_time)

        print(f"Time taken on stress test {i + 1} ({len(inputs[i])} items): {elapsed_time:.6f} seconds")

    return [[125, 250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000], total_times]
