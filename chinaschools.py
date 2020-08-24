# @File  : chinaschools.py
# @Author: Qiao
# @Date  : 2019/8/5
# @Desc  :


import fire
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import COORDINATES
def geo(cities, values, type) -> Geo:
    return (
        Geo()
        .add_schema(maptype="china")
        .add(
            "",
            [(c, v) for c, v in zip(cities, values) if c in COORDINATES],
            type_=type,
            symbol_size=5,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(min_=1, max_=50),
            title_opts=opts.TitleOpts(title="中国大学分布图"),
        )
    )
def load_data(file):
    data = pd.read_csv(file, sep="\t", header=None, encoding="utf-8")
    data.columns = ("university", "city")
    return data
def main(type, file="university.txt"):
    data = load_data(file)
    counter = data.city.value_counts()
    cities = [str(x) for x in counter.index.values]
    values = [int(x) for x in counter.values]
    c = geo(cities, values, type)
    c.width = "1200px"
    c.height = "900px"
    c.render("university.html")
if __name__ == "__main__":
    fire.Fire(main)