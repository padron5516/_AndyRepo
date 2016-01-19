@echo off
cd..

for /R _repo %%f in (*.zip) do del /q "%%~ff"
cd _tools
C:\Python27\python.exe generate_repo.py
cd..
echo F | xcopy "_repo\Andy.repository\Andy.repository-0.0.1.zip" "F:\_Github\_AndyRepo\repository.Andy.zip" /cherkyi