import os, hashlib, random, shutil, math
import time
names = os.listdir()
for name in names:
    if len(name) == 64 and not name == '8bf577c9296b57e64b23f0e0165465c8da676510b3e48cd648395888025acba8':
        print(name)
        print(os.getcwd())
        shutil.rmtree(name)
print_time = 0
files = 5
do_full = True
for n in range(files if do_full else 1):
    my_hash = hashlib.sha256(str(time.time_ns()).encode()).hexdigest()
    os.makedirs(my_hash, exist_ok=True)
    if not my_hash == '8bf577c9296b57e64b23f0e0165465c8da676510b3e48cd648395888025acba8':
        with open(os.path.join(my_hash, f'{hashlib.sha256(str(time.time_ns()).encode()).hexdigest()}'), 'w') as f:
            time_it_took = time.perf_counter()
            max_size = 100000000
            size = random.randint(0, max_size)
            size_interval = 1000000
            number_of_blocks = math.ceil(size/size_interval)
            for i in range(number_of_blocks):
                f.write(''.join([random.choice("1234567890abcdef") for n in range(size_interval)]))
                if time.time() > print_time + 1:
                    print_time = time.time()
                    print(f"[ {round(i/number_of_blocks*100, 2)}% ] Block {i} out of {number_of_blocks} with size {size_interval} written to {my_hash}")
            time_it_took = time.perf_counter() - time_it_took
            estimated_time = time_it_took * (max_size / (max_size - size))
            print(f"file writing took {round(time_it_took, 2)} seconds")
            print(f"estimated time {round(estimated_time, 2)} seconds for a full-size file")
            print(f"for a full obfuscation, it could take {round(estimated_time * files, 2)} seconds")

input('Press enter to continue...')