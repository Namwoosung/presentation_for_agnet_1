import {spawnSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const probe=(bin,args)=>{const r=spawnSync(bin,args,{encoding:'utf8',timeout:10000,windowsHide:true});return r.status===0?{available:true,version:r.stdout.trim()}:{available:false,reason:r.error?.code||'not executable'};};
const pythonCandidates=[process.env.SEMINAR_PYTHON,path.join(root,'.venv','Scripts','python.exe'),path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'),'python'].filter(Boolean);
let python;for(const bin of pythonCandidates){const p=probe(bin,['--version']);if(p.available){python={path:bin,...p};break;}}
let packages={};if(python){const code="import importlib.metadata as m,json; d={};\nfor p in ['pydantic-ai','pydantic-ai-slim','hermes-agent']:\n try:d[p]=m.version(p)\n except m.PackageNotFoundError:d[p]=None\nprint(json.dumps(d))";const result=probe(python.path,['-c',code]);if(result.available)packages=JSON.parse(result.version);}
const names=['OPENAI_API_KEY','ANTHROPIC_API_KEY','OPENAI_BASE_URL','SEMINAR_MODEL','SEMINAR_DATA','HERMES_HOME','HERMES_SOURCE'];
const report={checkedAt:new Date().toISOString(),platform:process.platform,node:{path:process.execPath,version:process.version},python:python||{available:false},git:probe('git',['--version']),packages,environmentPresence:Object.fromEntries(names.map(n=>[n,Boolean(process.env[n])])),scope:'설명용 재생과 실행 준비. API 호출·기존 설치 수정 없음',notVerified:['실제 Hermes Run','실제 PydanticAI Run','Provider payload 관찰','vLLM 기능 호환','실제 데이터·예측 품질','다른 PC 실행']};
fs.mkdirSync(path.join(root,'reports'),{recursive:true});fs.writeFileSync(path.join(root,'reports','environment.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
