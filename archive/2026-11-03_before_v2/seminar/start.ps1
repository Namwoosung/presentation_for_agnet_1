param([int]$Port = 4173, [switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$seminarRoot = $PSScriptRoot
$nodeCommand = Get-Command node -ErrorAction SilentlyContinue
$nodePath = if ($nodeCommand) { $nodeCommand.Source } else { Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' }
if (-not (Test-Path -LiteralPath $nodePath)) { throw 'Node.js 20 이상을 설치하거나 PATH에 추가하세요.' }
$env:PORT = "$Port"
$url = "http://127.0.0.1:$Port"
$ready = $false
try { $page = Invoke-WebRequest -Uri $url -TimeoutSec 2; $ready = $page.Content.Contains('Agent Framework · Inside the Runtime') } catch {}
if (-not $ready) {
    if (Test-Path -LiteralPath (Join-Path $seminarRoot '.server.pid')) {
        $savedPid = Get-Content -LiteralPath (Join-Path $seminarRoot '.server.pid')
        $existing = Get-Process -Id $savedPid -ErrorAction SilentlyContinue
        if ($existing) { throw '이전 서버 프로세스가 있습니다. stop.ps1 실행 후 다시 시작하세요.' }
    }
    $serverPath = Join-Path $seminarRoot 'scripts\serve.mjs'
    $process = Start-Process -FilePath $nodePath -ArgumentList @('"' + $serverPath + '"') -WorkingDirectory $seminarRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $seminarRoot 'server.log') -RedirectStandardError (Join-Path $seminarRoot 'server-error.log')
    Set-Content -LiteralPath (Join-Path $seminarRoot '.server.pid') -Value $process.Id
    for ($attempt = 0; $attempt -lt 20; $attempt++) {
        Start-Sleep -Milliseconds 250
        if ($process.HasExited) { throw '서버 실행 실패. server-error.log를 확인하세요.' }
        try { $page = Invoke-WebRequest -Uri $url -TimeoutSec 1; if ($page.StatusCode -eq 200) { $ready = $true; break } } catch {}
    }
}
if (-not $ready) { throw "서버에 연결할 수 없습니다: $url" }
Write-Output "발표: $url"
if (-not $NoBrowser) { Start-Process $url }
