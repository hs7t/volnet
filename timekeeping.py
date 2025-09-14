import datetime

def dateFromYMD(input: str):
    return datetime.datetime.strptime(input, "%y-%m-%d").date()