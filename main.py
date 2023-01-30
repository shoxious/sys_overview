import time
import psutil

def main():
    while True:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        output = "\rCPU: {:.1f}% | RAM: {:.1f}%".format(cpu, memory)
        print(output, end="")
        time.sleep(1)

if __name__ == '__main__':
    main()
