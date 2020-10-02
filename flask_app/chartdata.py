from datetime import datetime
from config import log_time_format, graph_time_format

def graph_data(file_dir) -> list:

    num_of_people = []
    date_time = []
    with open(file_dir, "r") as f:
        l = f.readlines()
        l = [i.rstrip("\n") for i in l if i != "\n"]
        for i in l:
            num_of_people.append(int(i.split(",")[0]))
            date_time.append(_trancate_time(i.split(",")[1]))
        graph_data_list = {"label": date_time, "val": num_of_people}
    return graph_data_list

def _trancate_time(time) -> str:
    datetime_time = datetime.strptime(time, log_time_format)
    str_time = datetime.strftime(datetime_time, graph_time_format)
    return str_time
