# Small helper to install ursina into the project venv and run the 3D prototype.
# Usage: Open PowerShell and run this script (no activation required).

$python = 'C:/Users/klara/repos/klara_testapp/.venv/Scripts/python.exe'

if (-not (Test-Path $python)) {
    Write-Error "Python executable not found at $python. Ensure the project venv exists."
    exit 1
}

Write-Host "Using Python: $python"

Write-Host "Upgrading pip, setuptools, wheel..."
& $python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing ursina (if not already installed)..."
& $python -m pip install ursina

Write-Host "Starting gui3d.py... (close the window to return)"
& $python C:/Users/klara/repos/klara_testapp/gui3d.py
