import sys

if __name__ == "__main__":

    for line in sys.stdin:
        word = line.split(',')
        sys.stdout.write("{},{}\n".format(word[1].strip(),word[0]))
