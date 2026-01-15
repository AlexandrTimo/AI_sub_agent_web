import argparse
import json
import time
from pathlib import Path
from runner import AISubAgent

def load_urls_from_file(path):
    p = Path(path)
    if not p.exists():
        return []
    return [line.strip() for line in p.read_text().splitlines() if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="Example runner using the AISubAgent plan")
    parser.add_argument("--plan", default="agent.md", help="Agent plan file (default: agent.md)")
    parser.add_argument("--urls", help="Optional file with newline-separated URLs")
    parser.add_argument("--output", help="Output JSON report file (default: reports/report_<ts>.json)")
    args = parser.parse_args()

    agent = AISubAgent(args.plan)
    print("Loaded Agent Plan:")
    print(agent.load_plan())

    urls = []
    if args.urls:
        urls = load_urls_from_file(args.urls)

    if not urls:
        urls = [
            "https://example.com",
            "https://httpbin.org/status/200",
            "https://httpbin.org/status/404"
        ]

    print("\nRunning tests...")
    results = agent.run_tests(urls)

    report = {
        "plan": args.plan,
        "timestamp": int(time.time()),
        "results": results
    }

    out_path = args.output
    if not out_path:
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        out_path = reports_dir / f"report_{report['timestamp']}.json"
    else:
        out_path = Path(out_path)

    out_path.write_text(json.dumps(report, indent=2))
    print(f"\nReport written to: {out_path}")

if __name__ == "__main__":
    main()