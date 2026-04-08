
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

def main() -> None:
    out = Path('out/openapi-to-markdown.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        'repository': 'Seppmail-OpenAPI',
        'script': 'openapi-to-markdown.py',
        'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'note': 'Starter example maintained by Synedat Group GmbH for the SEPPmail ecosystem. Adapt authentication, endpoints and validation logic for your environment.',
        'steps': ['pre-check', 'read-only validation', 'evidence export'],
    }
    out.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    print(out)

if __name__ == '__main__':
    main()
