import sys

if __name__ == "__main__":

    for line in sys.stdin:
        data  = line.split()
        sys.stdout.write("{}\t{}\t1\n".format(data[0], data[2]))
