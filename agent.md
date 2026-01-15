# AI Sub-Agent Plan: Web Availability Test

## Goal
Check availability of given websites and analyze failures.

## Tools
- Python
- requests library

## Test Steps
1. Receive list of URLs
2. Send HTTP GET request
3. Capture status code & response time
4. Mark result as PASS or FAIL

## Analysis Rules
- Status code != 200 → FAIL
- Response time > 2s → WARNING

## Output
Human-readable test report with:
- Summary
- Failed cases
- Recommendations