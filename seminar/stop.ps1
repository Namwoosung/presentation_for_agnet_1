$pidFile = Join-Path $PSScriptRoot '.server.pid'
if (-not (Test-Path -LiteralPath $pidFile)) { Write-Output '이 실행기로 시작한 서버가 없습니다.'; exit }
$savedPid = [int](Get-Content -LiteralPath $pidFile)
$processInfo = Get-CimInstance Win32_Process -Filter "ProcessId = $savedPid"
$expectedScript = Join-Path $PSScriptRoot 'scripts\serve.mjs'
if ($processInfo -and $processInfo.CommandLine.Contains($expectedScript)) { Stop-Process -Id $savedPid; Write-Output '발표 서버를 종료했습니다.' }
elseif ($processInfo) { throw 'PID가 다른 프로세스를 가리킵니다. 자동 종료하지 않습니다.' }
Remove-Item -LiteralPath $pidFile
