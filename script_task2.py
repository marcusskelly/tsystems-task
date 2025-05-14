#!/usr/bin/env python3

import os
import sys
import requests

NETBOX_URL = os.getenv("NETBOX_URL", "http://localhost:8000")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN", "f98d3432b51a4d0b09c47ba0cd4f6091f387d3e7") 

HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def get_sites_by_status(status):
    
    url = f"{NETBOX_URL}/api/dcim/sites/?status={status}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to connect to NetBox API: {e}")
        sys.exit(1)

    data = response.json()
    results = data.get("results", [])

    if not results:
        print(f"No sites found with status '{status}'.")
        return

    print(f"Sites with status '{status}':")
    for site in results:
        print(f"- ID: {site['id']}, Name: {site['name']}, Status: {site['status']['value']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python query_sites.py <status>")
        print("Example: python query_sites.py active")
        sys.exit(1)

    status = sys.argv[1].lower()
    valid_statuses = {"active", "planned"}

    if status not in valid_statuses:
        print(f"[ERROR] Invalid status '{status}'. Valid options: {', '.join(valid_statuses)}")
        sys.exit(1)

    get_sites_by_status(status)


main()