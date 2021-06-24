from flask import render_template, redirect, url_for, request, send_from_directory, flash
from flask import send_from_directory


def index():

    aqh_table = 992
    scr_table = 179
    td2hap_rate = 56
    fs_table = 32

    jupyter_num={
        "9h001":1,
        "9h002":1,
        "9h000":1,
    }

    hive_table_stat = {
        "date":['2020/12','2021/01','2021/02','2021/03','2021/04','2021/05'],
        "table_ahq":[13,13,50,892,992,992],
        "table_scr":[4,21,30,163,172,179],
        "table_fs":[0,0,0,13,26,32],
        "table_9h001":[0,0,0,0,11,35],
        "table_9h002":[0,0,0,0,21,52],
        "table_9h000":[0,0,0,0,1,3],
    }

    cluster_mem = 60


    return render_template('index.html', aqh_table=aqh_table, scr_table=scr_table, td2hap_rate=td2hap_rate, fs_table=fs_table, hive_table_stat=hive_table_stat, jupyter_num=jupyter_num, cluster_mem=cluster_mem)


def hadoop_hue():
    return render_template('hadoop_hue.html')

def hadoop_jupyter():
    return render_template('hadoop_jupyter.html')

def hadoop_hivetable():
    return render_template('hadoop_hivetable.html')

def page_not_found(e):
    return render_template('404.html'), 404
