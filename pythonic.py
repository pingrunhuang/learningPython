'''
this script records all the use cases that I think are pythonic
'''

# use enumerate to get the index along with the value
L = [i*i for i in range(5)]
for index, value in enumerate(L, 1):
    print(index, ':', value)

# 2 ways of reversing a list
for item in L[::-1]:
    print(item)
for item in reversed(L):
    print(item)

# use any
def has_primary_key(rows):
    return any(row[1] == 0 and row[9] == 'yes' for row in rows)
def has_primary_key(rows):
    for row in rows:
        if row[1] == 0 and row[9] == 'yes':
            return True
    return False

# how to raise exception while print error
# raise SystemExit('Failed!')

# use ConfigParser to get and set configuration

# how to use kwargs
def func(*args, **kwargs):
    # 3306 is the default value
    port = kwargs.get('port', 3306)

# list.pop() to get and delete value

# defaultdict : if the key is not in the dict
def defaultDictImpl(pairs):
    from collections import defaultdict
    d = defaultdict(list)
    for key, value in pairs:
        d[key] = value

# counter : same use case as defaultdict while count most common 3 and
def get_most_common(pairs):
    from collections import Counter
    counter = Counter()
    for key, value in pairs:
        counter.update([key, value])

    # get the 3 most common value
    for key, value in counter.most_common(3):
        print(key, value)


# write a monitor system with nametuple
def my_monitor(disk_name):
    from collections import namedtuple
    DiskDevice = namedtuple('DiskDevice', 'major_number, minor_number, '
                            'device_name, read_count, read_merged_count, '
                                          'read_sections, time_spent_reading, write_count, write_merged_count, '
                                          'write_sections, write_sections,write_sections, write_sections, '
                                          ' weighted_time_spent_doing_io')
    with open('/proc/diskstats') as file:
        for line in file:
            if line.split()[2] == disk_name:
                return DiskDevice(*(line.split()))



# consumer-producer with multithreading in python


# transform if a then b else c 
x = "result1" if 2 > 1  else "result2"


class my_class():
    def __str__(self):
        print('this is used when using str(object)')
    def __repr__(self):
        print("this is used when user type the object in the interactive mode")
    # use ''.join() to join all the item in a collection into one long string


