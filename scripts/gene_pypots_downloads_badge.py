"""
Update JSON config file of PyPOTS downloads badge for Shields.io custom endpoint badge to use.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

import json

import requests

if __name__ == '__main__':
    pepy_api_url = "https://api.pepy.tech/api/v2/projects/pypots"

    with open("./figs/projects/pypots_downloads.json", 'r') as f:
        shields_endpoint = json.load(f)

    total_downloads = requests.request("GET", pepy_api_url).json()["total_downloads"]
    abbr_total_downloads = round(total_downloads / 1000)
    shields_endpoint["message"] = f"{abbr_total_downloads}k"

    with open("./figs/projects/pypots_downloads.json", 'w') as f:
        json.dump(shields_endpoint, f)
