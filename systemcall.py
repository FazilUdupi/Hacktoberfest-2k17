import fcntl, os, time

counter_file = 'my_counter.txt'

if not os.path.exists(counter_file):
   counter_file = open('my_counter.txt', 'w')
   counter_file.write('0') #Store 0 as starting number
   counter_file.close()

for i in range(15):
   counter_file = open('my_counter.txt', 'r+')
   fcntl.flock(counter_file.fileno(), fcntl.LOCK_EX)
   count = int(counter_file.readline()) + 1
   counter_file.seek(0)
   counter_file.write(str(count))
   counter_file.close()

   print('Process ID: ' + str(os.getpid()) + ', Count: ' + str(count))
   time.sleep(0.2)
