
set COMPILER="./bin/protoc.exe"
%COMPILER% --java_out=./generate/ im.proto
%COMPILER% --python_out=./generate/ im.proto
%COMPILER% --objc_out=./generate/ im.proto
%COMPILER% --js_out=import_style=commonjs,binary:./generate/ im.proto
%COMPILER% --dart_out=./generate/ im.proto --plugin "C:\Users\MSI-NB\AppData\Local\Pub\Cache\bin\protoc-gen-dart.bat"

pause
