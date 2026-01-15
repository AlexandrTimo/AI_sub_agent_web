import requests
import time

class AISubAgent:
    def __init__(self, plan_path):
        self.plan_path = plan_path

    def load_plan(self):
        with open(self.plan_path, "r") as f:
            return f.read()

    def run_tests(self, urls):
        results = []

        for url in urls:
            start = time.time()
            try:
                response = requests.get(url, timeout=5)
                duration = round(time.time() - start, 2)

                status = "PASS" if response.status_code == 200 else "FAIL"

                results.append({
                    "url": url,
                    "status_code": response.status_code,
                    "response_time": duration,
                    "result": status
                })

            except Exception as e:
                results.append({
                    "url": url,
                    "error": str(e),
                    "result": "FAIL"
                })

        return results

    def analyze_results(self, results):
        report = []
        failures = 0

        for r in results:
            if r["result"] == "FAIL":
                failures += 1
                report.append(f" {r['url']} - FAILED")
            else:
                report.append(f" {r['url']} - OK ({r['response_time']}s)")

        summary = f"\nSummary: {len(results) - failures}/{len(results)} tests passed"
        return "\n".join(report) + summary


if __name__ == "__main__":
    agent = AISubAgent("agent.md")

    print("Loaded Agent Plan:")
    print(agent.load_plan())

    urls_to_test = [
        "https://google.com",
        "https://github.com",
        "https://toyota.com"
    ]

    print("\n Running tests...")
    raw_results = agent.run_tests(urls_to_test)

    print("\n Analysis Report:")
    print(agent.analyze_results(raw_results))