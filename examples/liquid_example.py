import unittest

from pyvchart import options as opts
from pyvchart.charts import Liquid
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType


TEST_LIQUID_DATA = [{"value": 0.3}]


c = (
    Liquid()
    .set_data(data=[opts.BaseDataOpts(id_="data", values=TEST_LIQUID_DATA)])
    .set_liquid_spec(value_field="value")
    .set_global_options(
        indicator_opts=opts.IndicatorOpts(
            is_visible=True,
            title_opts=opts.IndicatorTitleOpts(
                is_visible=True,
                style=opts.BaseTitleTextStyleOpts(text="进度"),
            ),
            content_opts=opts.IndicatorContentOpts(
                is_visible=True,
                style=opts.BaseTitleTextStyleOpts(
                    text="30%",
                    base_style_opts=opts.BaseStyleOpts(fill="black"),
                ),
            ),
        ),
    )
)
c.render("liquid_example.html")
