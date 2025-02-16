import unittest

from pyvchart import options as opts
from pyvchart.charts import Area
from pyvchart.commons.utils import JsCode

TEST_AREA3D_DATA = [
    {"type": "Nail polish", "country": "Africa", "value": 4229},
    {"type": "Nail polish", "country": "EU", "value": 4376},
    {"type": "Nail polish", "country": "China", "value": 3054},
    {"type": "Nail polish", "country": "USA", "value": 12814},
    {"type": "Eyebrow pencil", "country": "Africa", "value": 3932},
    {"type": "Eyebrow pencil", "country": "EU", "value": 3987},
    {"type": "Eyebrow pencil", "country": "China", "value": 5067},
    {"type": "Eyebrow pencil", "country": "USA", "value": 13012},
    {"type": "Rouge", "country": "Africa", "value": 5221},
    {"type": "Rouge", "country": "EU", "value": 3574},
    {"type": "Rouge", "country": "China", "value": 7004},
    {"type": "Rouge", "country": "USA", "value": 11624},
    {"type": "Lipstick", "country": "Africa", "value": 9256},
    {"type": "Lipstick", "country": "EU", "value": 4376},
    {"type": "Lipstick", "country": "China", "value": 9054},
    {"type": "Lipstick", "country": "USA", "value": 8814},
    {"type": "Eyeshadows", "country": "Africa", "value": 3308},
    {"type": "Eyeshadows", "country": "EU", "value": 4572},
    {"type": "Eyeshadows", "country": "China", "value": 12043},
    {"type": "Eyeshadows", "country": "USA", "value": 12998},
    {"type": "Eyeliner", "country": "Africa", "value": 5432},
    {"type": "Eyeliner", "country": "EU", "value": 3417},
    {"type": "Eyeliner", "country": "China", "value": 15067},
    {"type": "Eyeliner", "country": "USA", "value": 12321},
    {"type": "Foundation", "country": "Africa", "value": 13701},
    {"type": "Foundation", "country": "EU", "value": 5231},
    {"type": "Foundation", "country": "China", "value": 10119},
    {"type": "Foundation", "country": "USA", "value": 10342},
    {"type": "Lip gloss", "country": "Africa", "value": 4008},
    {"type": "Lip gloss", "country": "EU", "value": 4572},
    {"type": "Lip gloss", "country": "China", "value": 12043},
    {"type": "Lip gloss", "country": "USA", "value": 22998},
    {"type": "Mascara", "country": "Africa", "value": 18712},
    {"type": "Mascara", "country": "EU", "value": 6134},
    {"type": "Mascara", "country": "China", "value": 10419},
    {"type": "Mascara", "country": "USA", "value": 11261},
]

c = (
    Area(
        render_opts=opts.RenderOpts(
            is_disable_dirty_bounds=True,
            options3d_opts=opts.Render3DOpts(
                is_enable=True,
                is_enable_view_3d_transform=True,
                center={"x": 500, "y": 250},
            ),
        ),
    )
    .set_3d_mode()
    .set_data(data=[opts.BaseDataOpts(values=TEST_AREA3D_DATA)])
    .set_xy_field(x_field_name="type", y_field_name="value")
    .set_z_field(field_name="country")
    .set_area_spec()
    .set_global_options(
        is_stack=False,
        series_field="country",
        legend_opts=[
            opts.BaseLegendOpts(is_visible=True, position="middle", orient="bottom")
        ],
        axes_opts=[
            opts.BaseAxesOpts(mode="3d", orient="bottom"),
            opts.BaseAxesOpts(mode="3d", orient="left"),
            opts.AxesBandOpts(
                base_axes_opts=opts.BaseAxesOpts(
                    mode="3d",
                    orient="z",
                    label=opts.AxesLabelOpts(is_visible=True),
                    grid=opts.AxesGridOpts(is_visible=True),
                    width=600,
                    height=200,
                    depth=200,
                ),
            ),
        ],
        crosshair_opts=opts.CrossHairOpts(
            x_field=opts.CrossHairFieldOpts(is_visible=False)
        ),
        title_opts=opts.TitleOpts(
            is_visible=True,
            text="Unstacked area chart of cosmetic products sales",
        ),
    )
)
c.render("area3d_example.html")
