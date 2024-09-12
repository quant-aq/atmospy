"""
Daily Average Ozone
===================

_thumb: .8, .8
"""

import atmospy

atmospy.set_theme()

# Load the example dataset
df = atmospy.load_dataset("us-ozone")

# Select a single location
single_site_ozone = df[df["Local Site Name"] == df["Local Site Name"].unique()[0]]

atmospy.calendarplot(
    data=single_site_ozone,
    x="Timestamp Local",
    y="Sample Measurement",
    freq="day",
    cbar=False,
    height=2.5,
    linewidths=0.1,
)
