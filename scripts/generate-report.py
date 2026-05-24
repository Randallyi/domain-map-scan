#!/usr/bin/env python3
"""
Blind Spot Scanner Report Generator

Optional helper script to format blind spot scanner output.
Reads JSON input and produces a standardized markdown report.

Usage:
    python generate-report.py < input.json > report.md
"""

import json
import sys
from datetime import datetime


def render_report(data: dict) -> str:
    """Render domain map data as markdown report."""
    
    lines = [
        f"# Domain Map: {data['domain']}",
        f"Date: {data.get('date', datetime.now().strftime('%Y-%m-%d'))}",
        f"Goal: {data['goal']}",
        "",
        "## Dimensions",
        "| Dimension | Coverage | Threshold | Status |",
        "|-----------|----------|-----------|--------|",
    ]
    
    for dim in data['dimensions']:
        coverage = dim['coverage']
        threshold = dim['threshold']
        if coverage >= threshold:
            status = "🟢"
        elif coverage >= threshold * 0.8:
            status = "🟡"
        else:
            status = "🔴"
        lines.append(
            f"| {dim['name']} | {coverage}% | {threshold}% | {status} |"
        )
    
    lines.extend([
        "",
        "## Critical Blind Spots (Top 3)",
    ])
    
    for i, blind in enumerate(data.get('blind_spots', [])[:3], 1):
        lines.append(
            f"{i}. **{blind['dimension']}**: {blind['issue']} → {blind['action']}"
        )
    
    decision = data.get('decision', {})
    go = decision.get('go', False)
    lines.extend([
        "",
        "## Launch Decision",
        f"- [{'x' if go else ' '}] GO — {decision.get('go_reason', '')}",
        f"- [{'x' if not go else ' '}] NO-GO — {decision.get('nogo_reason', '')}",
        "",
        "## Re-audit Triggers",
    ])
    
    for trigger in data.get('triggers', []):
        lines.append(f"- {trigger}")
    
    return "\n".join(lines)


def main():
    try:
        data = json.load(sys.stdin)
        print(render_report(data))
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing required field: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
