"""
This script utilize the package GSBG to generate citation badges for my profile and articles on Google Scholar.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

from time import sleep

import gsbg

badge_saving_path = "figs/citation_badges"

link_dict = {
    "wdu": {
        "link": "https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en",
        "link_type": "profile",
    },
    "saits": {
        "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:Y0pCki6q_DkC",
        "link_type": "article",
    },
    "jocn2021": {
        "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:zYLM7Y9cAGgC",
        "link_type": "article",
    },
}


for item in link_dict:
    gsbg.gene_citation_badge_svg(
        link_dict[item]["link"],
        link_dict[item]["link_type"],
        svg_name=item,
        path_to_save=badge_saving_path,
    )
    sleep(10)
