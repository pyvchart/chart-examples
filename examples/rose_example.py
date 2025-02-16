from pyvchart import options as opts
from pyvchart.charts import Rose
from pyvchart.globals import ChartType


TEST_ROSE_DATA = [
    {"value": "159", "type": "Tradition Industries"},
    {"value": "50", "type": "Business Companies"},
    {"value": "13", "type": "Customer-facing Companies"},
]


c = (
    Rose()
    .set_data(data=[opts.BaseDataOpts(values=TEST_ROSE_DATA)])
    .set_rose_spec(
        outer_radius=0.8,
        inner_radius=0.2,
        category_field="type",
        value_field="value",
        label_opts=opts.LabelOpts(
            is_visible=True,
        ),
    )
    .set_global_options(
        series_field="type",
    )
)
c.render("rose_example.html")
