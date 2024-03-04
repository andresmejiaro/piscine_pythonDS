import time

s = time.time()
s

print(
    f'Seconds sice January 1, 1970 {
        s:.4f} or {
            s:.2E} in scientific notation')
print(f'{time.strftime("%b %d 20%y", time.localtime())}')
