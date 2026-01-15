# AI Sub-Agent Web

Simple example project that simulates an "AI sub-agent" which loads a plan and runs basic HTTP tests against a list of URLs.

## Features
- Load an agent plan from `agent.md`
- Perform simple GET requests and record status codes and response times (`runner.py`)
- Produce a small analysis report printed to stdout (`runner.py`)
- Produce JSON reports with metadata (`runner_report.py`)

## Requirements
- Python 3.8+
- requests

Install requirements:
```bash
python3 -m pip install requests
```

## Files
- `runner.py` — simple CLI that loads `agent.md`, runs tests against an embedded URL list, and prints an analysis report to stdout.
- `runner_report.py` — CLI that loads `agent.md`, accepts a newline-separated `--urls` file, runs tests, and writes a JSON report.
- `agent.md` — agent plan (keep this file and edit to change plan).
- `urls.txt` — optional list of URLs (one per line) you can create for `runner_report.py`.

## Usage

Run the simple test runner (prints plan + analysis):
```bash
cd /Users/TimRush/Documents/Code/apprenticeship/linkedin/AI_sub_agent_web
python3 runner.py
```

Run the report-style runner (produces JSON reports, accepts URL file):
```bash
cd /Users/TimRush/Documents/Code/apprenticeship/linkedin/AI_sub_agent_web
python3 runner_report.py --urls urls.txt
```

Specify plan or output path:
```bash
python3 runner_report.py --plan agent.md --urls urls.txt --output reports/my_report.json
```

## URLs file example (`urls.txt`)
Create a file named `urls.txt` with one URL per line, for example: https://google.com

## Notes
- The default plan file is `agent.md`. Keep and edit that file to change the plan.
- `runner.py` prints status codes and response times to stdout alongside a short analysis.
- `runner_report.py` creates a `reports/` directory by default and writes `report_<timestamp>.json` unless `--output` is provided.

## Contributing
Open issues or submit PRs to improve tests, reporting, or add CI.
