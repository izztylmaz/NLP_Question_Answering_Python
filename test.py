from multiprocessing import Process
import time
from os.path import join
from jpype import JClass, getDefaultJVMPath, shutdownJVM, startJVM

COUNT = 5000000

zemberek_path: str = join('..', '..', 'Dependencies', 'Zemberek-Python', 'bin', 'zemberek-full.jar')

def test():
    try:
        startJVM(
            getDefaultJVMPath(),
            '-ea',
            f'-Djava.class.path={zemberek_path}',
            convertStrings=False
        )
        shutdownJVM()
        print("done")
    except:
        print("Error")


if __name__ == '__main__':
    start = time.time()
    p_list = []
    p_list.append(Process(target=test))
    p_list.append(Process(target=test))


for _ in p_list:
    _.start()

for _ in p_list:
    _.join()

end = time.time()
print("Time taken in seconds -", end - start)