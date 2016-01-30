@echo off
cd..

for /R _repo %%f in (*.zip) do del /q "%%~ff"
cd _tools
C:\Python27\python.exe generate_repo.py
cd..
echo F | xcopy "_repo\Andy.repository\Andy.repository-1.0.zip" "F:\_Github\_AndyRepo\Andy.repository.zip" /cherkyi