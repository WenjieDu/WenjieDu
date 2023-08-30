"""
Update JSON config file of downloads badge for Shields.io custom endpoint badge to use.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

import json

import requests

if __name__ == "__main__":
    pepy_api_url = "https://api.pepy.tech/api/v2/projects/"

    for project_name in ["pypots", "tsdb", "pycorruptor"]:
        with open(f"./figs/projects/{project_name}_downloads.json", "r") as f:
            shields_endpoint = json.load(f)

        request_url = pepy_api_url + project_name
        total_downloads = requests.request("GET", request_url).json()["total_downloads"]
        abbr_total_downloads = round(total_downloads / 1000)
        shields_endpoint["message"] = f"{abbr_total_downloads}k"

        with open(f"./figs/projects/{project_name}_downloads.json", "w") as f:
            json.dump(shields_endpoint, f)
