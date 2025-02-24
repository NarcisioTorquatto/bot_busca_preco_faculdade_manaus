$exclude = @("venv", "template_BotCity_Web.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "template_BotCity_Web.zip" -Force