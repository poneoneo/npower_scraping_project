# WebScraping and Data Analysis on Youtube Channels

## Project Description

This project uses Playwright to automate the scraping of videos from a specific YouTube channel. The collected data is then analyzed and visualized using pandas and datahorse. The goal is to gather information about the videos such as title, publication date, and view count, and then analyze and visualize this data by describing wich chart you are excpecting to see.

## Objective

The objective of this project is to demonstrate the use of web scraping to gather information from the internet, specifically from a YouTube channel, and to extract valuable insights from the collected data.

## Installation

### Prerequisites

    - Python 3.10 or higher
    - [uv](https://docs.astral.sh/uv/) An extremely fast Python package and project manager, written in Rust.

### Installation Steps

1. Clone the project repository:
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```
#### With Uv
Uv is an incredibly fast and powerful python package manager and I highly recommend using it both to install this project and to build your own. However, if you're not comfortable with this kind of tool or if you prefer to use pip then you can go directly to the [pip](#with-pip) section.
   1. Install Uv:
        - - MacOs and Linux.
           - Use curl to download the script and execute it with sh:
             ```bash
                 curl -LsSf https://astral.sh/uv/install.sh | sh
           ```
        - - Windows 
          -  Use PowerShell to download and execute the script:
                ```powershell
                powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.18/install.ps1 | iex"
             ```
   2. Create virtualenv and install all required dependencies:
        ```bash
            uv sync
        ```
   3. Activate virtualenv : 
        ```bash
            source .venv/bin/activate or venv\Scripts\activate "for windows"
        ```
#### With pip

1. Create and activate a virtual environment:

   ##### MacOS and Linux
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

   ##### Windows
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```

  1. Install all required dependencies  :
      ```bash
        pip install -r requirements.txt
      ```

## Usage


### Data Scraping

