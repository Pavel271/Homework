import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            file_string = file.readline()
            all_data.append(file_string)
            if not file_string:
                break

file_names = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == "__main__":
    # Линейный вызов
    start1 = datetime.datetime.now()
    for name in file_names:
        read_info(name)
    end1 = datetime.datetime.now()
    print(f'{end1 - start1} (линейный)')
    # Многопроцессный
    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.datetime.now()
        pool.map(read_info, file_names)
        end2 = datetime.datetime.now()
    print(f'{end2 - start2} (многопроцессный)')