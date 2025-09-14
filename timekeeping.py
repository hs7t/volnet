import datetime

def dateFromYMD(input: str):
    return datetime.datetime.strptime(input, "%Y-%m-%d").date()