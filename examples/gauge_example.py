import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Gauge
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

TEST_GAUGE_DATA = [{"type": "目标A", "value": 0.6}]

c = (
    Gauge()
    .set_data(data=[opts.BaseDataOpts(id_="id0", values=TEST_GAUGE_DATA)])
    .set_gauge_spec(
        category_field="type",
        value_field="value",
        outer_radius=0.8,
        inner_radius=0.5,
        start_angle=-180,
        end_angle=0,
    )
)
c.render("gauge_example.html")
