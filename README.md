
# NetBox Evaluation Scripts

This repository contains two scripts to interact with a NetBox instance as part of a technical assessment:

1. **Custom Script for NetBox** – Executes via the NetBox UI and filters sites by status (`active` or `planned`)
2. **Python API Script** – Queries the NetBox API to retrieve and print sites with a specific status

---

## Contents

```
.
├── script_task1.py                      
├── script_task2.py         
└── README.md
```

---

## Setup

### 1. Install NetBox

- [Official NetBox Docker setup](https://github.com/netbox-community/netbox-docker)

```
    git clone -b release https://github.com/netbox-community/netbox-docker.git
    cd netbox-docker
    tee docker-compose.override.yml 
    services:
      netbox:
        ports:
          - 8000:8080
    EOF
    docker compose pull
    docker compose up
    
    docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```

### 2. Create an API Token

In the NetBox UI:
- Go to your user account → **API Tokens**
- Generate a new token and copy it for use with the API script

### 3. Add Initial Site Data

- 2 with status `active`
- 2 with status `planned`


```yaml
- name: Site 1
  slug: site_1
  status: planned
- name: Site 2
  slug: site_2
  status: planned
- name: Site 3
  slug: site_3
  status: active
- name: Site 4
  slug: site_4
  status: active
```

---

## Task 1: Custom Script for NetBox

### File:
```
script_task1.py
```

### Features:
- Accepts a **required filter** for site status (`active` or `planned`)
- Iterates through matching sites
- Displays:
  - YAML-formatted output in the **Output field**
  - Logging entries like: `#<site_id>: <site_name> - <site_status>`

### Running the script:

1. Log in to the NetBox UI
2. Navigate to:  
   `Extras → Scripts → Add Script`
3. Upload or paste the script from `script_task1.py`
4. Execute the script and select a `Site Status` (`active`)
5. View output and logs in the UI

### Example Output:

```
#3: Site 3 - active
#4: Site 4 - active

Output:
- id: 3
  name: Site 3
  status: active
- id: 4
  name: Site 4
  status: active
```

---

## Task 2: Python Script to Query Sites Count via NetBox API

### File:
```
script_task2.py
```

### Features:
- Queries the NetBox REST API for sites matching a given status
- Displays results in the terminal
- Validates arguments and handles errors


### Running the script:
Run the script with one argument (status):
```bash
python script_task2.py active
```

### Example Output:

```
Sites with status 'active':
- ID: 3, Name: Site 3, Status: active
- ID: 4, Name: Site 4, Status: active
```

If no argument is provided:
```
Usage: python script_task2.py <status>
Example: python script_task2.py active
```

If an invalid status is provided:
```
[ERROR] Invalid status 'inactive'. Valid options: active, planned
```

---





