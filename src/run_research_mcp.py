"""Launch the unchanged course MCP with private environment and a redacted audit.

Generated integration glue. The API functions themselves remain course code.
HW1_ENV_FILE is optional; no credential is stored in this repository.
"""
from __future__ import annotations
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
private = os.environ.get('HW1_ENV_FILE')
if private:
    for line in Path(private).read_text(encoding='utf-8-sig').splitlines():
        if line.strip() and not line.startswith('#') and '=' in line:
            name, value = line.split('=', 1)
            if name in {'OPENALEX_API_KEY', 'OPEN_ALEX'}:
                os.environ[name] = value.strip().strip('"')

spec = importlib.util.spec_from_file_location('course_research_mcp', ROOT/'src/research_mcp.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
original_http = module._http_json
audit_path = ROOT/'evidence/research_api_calls.jsonl'

def audited_http(url, params, accept='application/json', timeout=60):
    public = {k:v for k,v in params.items() if k.lower() not in {'api_key','key','token'}}
    entry = {'started_at_utc':datetime.now(timezone.utc).isoformat(),
             'method':'GET', 'url':url, 'params':public}
    try:
        data = original_http(url, params, accept, timeout)
        entry.update(status='success', response=data)
        return data
    except Exception as exc:
        # Exception strings can contain request URLs with keys: retain only the type.
        entry.update(status='error', error_type=type(exc).__name__)
        raise
    finally:
        entry['ended_at_utc'] = datetime.now(timezone.utc).isoformat()
        audit_path.parent.mkdir(exist_ok=True)
        with audit_path.open('a',encoding='utf-8') as f:
            f.write(json.dumps(entry,ensure_ascii=False)+'\n')

module._http_json = audited_http
if __name__ == '__main__':
    if '--selftest' in sys.argv:
        raise SystemExit(module._selftest())
    module.mcp.run()
