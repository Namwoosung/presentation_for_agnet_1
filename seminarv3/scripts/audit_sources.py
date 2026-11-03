from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from html.parser import HTMLParser
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
URLS={
'H-ARCH':'https://hermes-agent.nousresearch.com/docs/developer-guide/architecture',
'H-LOOP':'https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop',
'H-PROMPT':'https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly',
'H-SESSION':'https://hermes-agent.nousresearch.com/docs/user-guide/sessions',
'H-MEMORY':'https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what',
'H-SKILL':'https://hermes-agent.nousresearch.com/docs/user-guide/features/skills',
'H-TOOLS':'https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime',
'H-DELEGATE':'https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns',
'C':'https://code.claude.com/docs/en/how-claude-code-works',
'C-MEM':'https://code.claude.com/docs/en/memory',
'C-SKILL':'https://code.claude.com/docs/en/skills',
'C-POLICY':'https://code.claude.com/docs/en/permissions',
'C-HOOK':'https://code.claude.com/docs/en/hooks',
'C-SANDBOX':'https://code.claude.com/docs/en/sandboxing',
'C-SUB':'https://code.claude.com/docs/en/sub-agents',
'C-TEAM':'https://code.claude.com/docs/en/agent-teams',
'P-AGENT':'https://pydantic.dev/docs/ai/core-concepts/agent/',
'P-TOOLS':'https://pydantic.dev/docs/ai/tools-toolsets/tools/',
'P-ADV':'https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/',
'P-OUTPUT':'https://pydantic.dev/docs/ai/core-concepts/output/',
'P-DEPS':'https://pydantic.dev/docs/ai/core-concepts/dependencies/',
'P-DEFER':'https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools/',
'P-HARNESS':'https://pydantic.dev/docs/ai/capabilities/overview/',
'O':'https://openai.github.io/openai-agents-python/running_agents/',
'O-ORCH':'https://openai.github.io/openai-agents-python/multi_agent/',
'O-GUARD':'https://openai.github.io/openai-agents-python/guardrails/',
'O-HITL':'https://openai.github.io/openai-agents-python/human_in_the_loop/',
'S':'https://platform.claude.com/docs/en/agent-sdk/overview',
'S-MCP':'https://platform.claude.com/docs/en/agent-sdk/custom-tools',
'S-POLICY':'https://platform.claude.com/docs/en/agent-sdk/permissions',
'G':'https://google.github.io/adk-docs/runtime/',
'G-EVENT':'https://google.github.io/adk-docs/events/',
'G-STATE':'https://google.github.io/adk-docs/sessions/',
'G-WORKFLOW':'https://google.github.io/adk-docs/agents/workflow-agents/',
'M':'https://learn.microsoft.com/en-us/agent-framework/overview/',
'M-MIDDLE':'https://learn.microsoft.com/en-us/agent-framework/agents/middleware/',
'M-WORKFLOW':'https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/',
'M-CHECKPOINT':'https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/checkpoints',
'DEPLOY':'https://docs.vllm.ai/en/latest/features/tool_calling/'
}
class Extract(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.skip+=1
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip and data.strip():self.parts.append(data.strip())
def fetch(item):
 key,url=item
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:raw=r.read();final=r.url
  txt=raw.decode('utf-8','replace');p=Extract();p.feed(txt);clean='\n'.join(p.parts)
  (ROOT/'evidence/sources'/f'{key}.txt').write_text(clean,encoding='utf-8')
  return key,dict(url=final,status='FETCHED',sha256=hashlib.sha256(raw).hexdigest(),chars=len(clean))
 except Exception as e:return key,dict(url=url,status='FETCH_FAILED',error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=8) as pool: result=dict(pool.map(fetch,URLS.items()))
 for key,repo in [('H-SRC','NousResearch/hermes-agent'),('P-SRC','pydantic/pydantic-ai'),('S-SRC','anthropics/claude-agent-sdk-python')]:
  try:
   with urlopen(Request(f'https://api.github.com/repos/{repo}/commits/HEAD',headers={'User-Agent':'Codex'}),timeout=20) as r:sha=json.load(r)['sha']
   result[key]={'url':f'https://github.com/{repo}/tree/{sha}','commit':sha,'status':'PINNED_COMMIT'}
   paths={'H-SRC':['run_agent.py','agent/conversation_loop.py','agent/tool_executor.py','model_tools.py'], 'P-SRC':['pydantic_ai_slim/pydantic_ai/_agent_graph.py','pydantic_ai_slim/pydantic_ai/agent/__init__.py'], 'S-SRC':['src/claude_agent_sdk/_internal/transport/subprocess_cli.py']}[key]
   for path in paths:
    with urlopen(f'https://raw.githubusercontent.com/{repo}/{sha}/{path}',timeout=25) as r:raw=r.read()
    (ROOT/'evidence/sources'/f"{key}-{path.replace('/','_')}").write_bytes(raw)
  except Exception as e:result[key]=dict(status='FETCH_FAILED',error=str(e))
 (ROOT/'docs/source-map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:v['status'] for k,v in result.items()},indent=2))
