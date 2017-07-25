def read():
    import sys
    filename = sys.argv[1]  # must pass valid file name
    with open(filename, 'rb') as hugefile:
        chunksize = 1000
        readable = ''
        # if you want to stop after certain number of blocks
        # put condition in the while
        while hugefile:
            # if you want to start not from 1st byte
            # do a hugefile.seek(skipbytes) to skip
            # skipbytes of bytes from the file start
            start = hugefile.tell()
            print("starting at:", start)
            file_block = ''  # holds chunk_size of lines
            for _ in range(start, start + chunksize):
                line = hugefile.next()
                file_block = file_block + line

            print('file_block', type(file_block), file_block)
            readable = readable + file_block
            # tell where are we in file
            # file IO is usually buffered so tell()
            # will not be precise for every read.
            stop = hugefile.tell()
            print('readable', type(readable), readable)
            print('reading bytes from %s to %s' % (start, stop))
            print('read bytes total:', len(readable))

            # if you want to pause read between chucks
            # uncomment following line
            # raw_input()


def read_streaming_data():
    import time
    import os
    import sys
    if len(sys.argv) != 2:
        print(sys.stderr, "Please specify filename to read")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(sys.stderr, "Given file: \"%s\" is not a file" % filename)
    with open(filename, 'r') as f:
        # Move to the end of file
        filesize = os.stat(filename)[6]
        f.seek(filesize)
        # endlessly loop
        while True:
            where = f.tell()
            # try reading a line
            line = f.readline()
            # if empty, go back
            if not line:
                time.sleep(1)
                f.seek(where)
            else:
                # at the end prevents print to add newline, as
                line = f.readline()
                # already read that.
                print(line)


def map_reduce():
    """
    TODO:implementation of mapreduce to read large file
    :return: 
    """
    pass


