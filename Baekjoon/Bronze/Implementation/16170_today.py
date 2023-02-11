import time
tm = time.time()
tm += 9 * 3600
tm = time.localtime(tm)
print(time.strftime('%Y', tm))
print(time.strftime('%m', tm))
print(time.strftime('%d', tm))