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

  1. Install UV in your PC:
     #### MacOs and Linux
      - Use curl to download the script and execute it with sh:
          ```bash
              curl -LsSf https://astral.sh/uv/install.sh | sh
          ```
      - If your system doesn't have curl, you can use wget:
          ```bash
              wget -qO- https://astral.sh/uv/install.sh | sh
          ```

      - Request a specific version by including it in the URL:
          ```bash
              curl -LsSf https://astral.sh/uv/0.5.18/install.sh | sh
          ```
     #### Windows
      - Use PowerShell to download and execute the script:
          ```powershell
          powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.18/install.ps1 | iex"
          ```
  2. clone the project repository and cd into the cloned directory:
      ```bash
      git clone https://github.com/poneoneo/npower_scraping_project
      cd npower_scraping_project
      ```

  3. Create and activate virtual environnement then install all required dependencies in a single line command :
      ```bash
        uv sync
      ```

## Usage

### Data Scraping

