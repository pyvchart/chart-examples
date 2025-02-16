import unittest

from pyvchart import options as opts
from pyvchart.charts import Venn
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType


TEST_VENN_DATA = [
    {"sets": ["A"], "value": 8},
    {"sets": ["B"], "value": 10},
    {"sets": ["C"], "value": 12},
    {"sets": ["A", "B"], "value": 4},
    {"sets": ["A", "C"], "value": 4},
    {"sets": ["B", "C"], "value": 4},
    {"sets": ["A", "B", "C"], "value": 2},
]


c = (
    Venn()
    .set_data(data=[opts.BaseDataOpts(values=TEST_VENN_DATA)])
    .set_venn_spec(
        category_field="sets",
        value_field="value",
    )
    .set_global_options(
        series_field="sets",
        legend_opts=[
            opts.BaseLegendOpts(is_visible=True, position="middle", orient="bottom"),
        ],
    )
)
c.render("venn_example.html")
