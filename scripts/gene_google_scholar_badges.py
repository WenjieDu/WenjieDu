"""
Hey, congrats! You find this script to help you generate your citation badges!
You've almost done the job. Just read and follow the instructions below.

This script helps generate citation badges for profiles and articles on Google Scholar.
It works with the GitHub workflow ../.github/workflows/gene_citation_badges.yml
to run and update the badges automatically under the directory ../figs/citation_badges.
Therefore, you don't need to run this script manually. All the steps you need to do are:

1. fork this repository to your own GitHub account;
2. replace the links in the dictionary `link_dict` below with your own links;
3. keep this script, the workflow yml, and the directory ../figs/citation_badges. Others can be removed;
4. please star this repository and GSBG https://github.com/WenjieDu/GSBG if you find them useful. Thanks!

"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

from time import sleep

import gsbg

badge_saving_path = "figs/citation_badges"

link_dict = {

    # "name_of_this_svg_to_be_saved": {
    #     "link_type": "profile",  # the type of this link, can be "profile" or "article"
    #     "link": "past your link here",  # the link of GoogleScholar item to be parsed
    # },

    # belows are my examples

    "wdu": {
        "link_type": "profile",
        "link": "https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en",
    },
    "saits": {
        "link_type": "article",
        "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:Y0pCki6q_DkC",
    },
    "jocn2021": {
        "link_type": "article",
        "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:zYLM7Y9cAGgC",
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
