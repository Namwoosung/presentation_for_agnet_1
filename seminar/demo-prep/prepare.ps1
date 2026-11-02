param([switch]$Install, [string]$PythonPath)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$venvPath = Join-Path $projectRoot '.venv'
$vendorPath = Join-Path $projectRoot 'vendor'
$hermesPath = Join-Path $vendorPath 'hermes-v0.22.5'
Write-Output '고정 버전 준비: PydanticAI Core 2.61.0 / Hermes v0.22.5'
Write-Output "새 격리 환경: $venvPath"
Write-Output "새 소스 복제: $hermesPath"
Write-Output '기존 Hermes 홈·Memory·DB·전역 Python을 수정하지 않습니다. 모델 호출은 하지 않습니다.'
if (-not $Install) { Write-Output '계획만 출력했습니다. 설치하려면 -Install -PythonPath <python.exe>를 명시하세요.'; exit }
if (-not $PythonPath -or -not (Test-Path -LiteralPath $PythonPath)) { throw '유효한 -PythonPath가 필요합니다.' }
if ((Test-Path -LiteralPath $venvPath) -or (Test-Path -LiteralPath $hermesPath)) { throw '대상 환경/소스가 이미 있습니다. 기존 내용을 확인하세요. 덮어쓰지 않습니다.' }
& $PythonPath -m venv $venvPath
if ($LASTEXITCODE -ne 0) { throw 'venv 생성 실패' }
$venvPython = Join-Path $venvPath 'Scripts\python.exe'
& $venvPython -m pip install 'pydantic-ai==2.61.0'
if ($LASTEXITCODE -ne 0) { throw '고정 패키지 설치 실패. 최신 버전으로 대체하지 않았습니다.' }
New-Item -ItemType Directory -Path $vendorPath -Force | Out-Null
& git clone --depth 1 --branch v0.22.5 'https://github.com/NousResearch/hermes-agent.git' $hermesPath
if ($LASTEXITCODE -ne 0) { throw '고정 Hermes 태그 복제 실패. 기존 설치를 사용하지 않았습니다.' }
Write-Output '패키지 설치와 소스 복제 완료. Hermes 의존성·Backend·모델 설정·관찰기는 별도 검증이 필요합니다.'
Write-Output 'SEMINAR_PYTHON과 HERMES_SOURCE를 위 경로로 지정하고 doctor를 다시 실행하세요.'
