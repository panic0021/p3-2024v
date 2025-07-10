from sys import stderr
from pathlib import Path
from time import perf_counter
from datetime import datetime
import functools

def get_csv_data_size(fpath):
    from pandas import read_csv

    try:
        df = read_csv(fpath)
    except OSError as err:
        stderr.write(f"Error while trying to read data from file {fpath}:\n{err}\n")
        return None
    else:
        nrow, ncol = df.shape
        return nrow * ncol

def get_text_data_size(fpath):
    try:
        with open(fpath, 'r') as fobj:
            return len(fobj.readlines())
    except OSError as err:
        stderr.write(f"Error while trying to read data from file {fpath}:\n{err}\n")
        return None

def add_to_log(line):
    log_fpath = Path.cwd().parent / 'results' / 'execution_log.txt'

    writting_mode = 'a'
    if not log_fpath.exists():
        writting_mode = 'w'

    try:
        with open(log_fpath, writting_mode) as fobj:
            fobj.write(line + '\n')
    except OSError as err:
        stderr.write(f"Error while trying to write to the log file {log_fpath}:\n{err}\n")


def execution_logger(func):
    @functools.wraps(func)
    def wrapper_execution_logger(*args, **kwargs):

        function_name = func.__name__

        fpath = args[0]
        data_size = 'NA'
        if fpath.suffix == '.csv':
            csv_data_size = get_csv_data_size(fpath)
            if csv_data_size:
                data_size = csv_data_size
        elif fpath.suffix == '.txt':
            txt_data_size = get_text_data_size(fpath)
            if txt_data_size:
                data_size = txt_data_size
        else:
            stderr.write(f"Unexpected file type ({fpath.suffix}) passed to the function ({function_name}); "
                         f"skipping computation of the data size\n")

        function_call_dt = datetime.now()

        function_start_time = perf_counter()

        value = func(*args, **kwargs)

        exec_time = (perf_counter() - function_start_time) * 1000

        to_log = f"{function_name}|{function_call_dt}|{exec_time}|{data_size}"
        add_to_log(to_log)

        return value
    return wrapper_execution_logger


# if __name__ == '__main__':
#
#     tmp = Path.cwd() / 'airline_reviews.csv'
#     print(tmp)
#     print(tmp.name)
#     print(tmp.suffix)