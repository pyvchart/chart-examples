from pyvchart import options as opts
from pyvchart.charts import Bar3D

TEST_BAR3D_DATA = [
    {"month": "Monday", "sales": 22},
    {"month": "Tuesday", "sales": 13},
    {"month": "Wednesday", "sales": 25},
    {"month": "Thursday", "sales": 29},
    {"month": "Friday", "sales": 38},
]

c = (
    Bar3D(
        render_opts=opts.RenderOpts(
            dom="123",
            options3d_opts=opts.Render3DOpts(is_enable=True),
        )
    )
    .set_data(
        data=[
            opts.BaseDataOpts(
                id_="bar3DData",
                values=TEST_BAR3D_DATA,
            )
        ],
    )
    .set_bar3d_spec(
        bar3d_opts=opts.Bar3DOpts(
            style=opts.BaseStyleOpts(
                length=20,
            ),
            state=opts.BaseStateOpts(
                selected_opts=opts.BaseStyleOpts(
                    stroke="#000",
                ),
            ),
        ),
    )
    .set_xy_field(x_field_name="month", y_field_name="sales")
    .set_global_options(
        axes_opts=[
            opts.AxesBandOpts(
                base_axes_opts=opts.BaseAxesOpts(
                    orient="bottom",
                    tick=opts.AxesTickOpts(tick_size=20),
                    mode="3d",
                ),
            ),
            opts.AxesLinearOpts(
                base_axes_opts=opts.BaseAxesOpts(
                    orient="left",
                    tick=opts.AxesTickOpts(tick_size=20),
                    mode="3d",
                ),
            ),
        ]
    )
)

c.render("bar3d_example.html")
