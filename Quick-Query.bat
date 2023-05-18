@echo off

set SCRIPT_PATH=E:\Quick\SQL\Auto-SQL-Query-to-CSV.exe
set SQL_QUERY_PATH=E:\Quick\SQL\PySQL-Query.txt
set DB_INFO_PATH=E:\Quick\SQL\PySQL-Info.txt
set OUTPUT_PATH=E:\Quick\Output-Quick.csv
set ENCODING=ANSI

echo 目前的运行配置如下：
echo 当前调用的可执行文件路径：%SCRIPT_PATH%
echo 输入查询语句的文件路径：%SQL_QUERY_PATH%
echo 输入数据库配置信息的文件路径：%DB_INFO_PATH%
echo 输出文件的计划存储路径：%OUTPUT_PATH%
echo 输出文件的预设文件编码路径：%ENCODING%
echo 接下来开始进行查询并输出结果到指定文件
echo 可执行文件运行的LOG：【
echo.
"%SCRIPT_PATH%" -q "%SQL_QUERY_PATH%" -i "%DB_INFO_PATH%" -o "%OUTPUT_PATH%" -c %ENCODING%

echo 】

echo 查询和输出文件的任务已完成！
echo 输出文件路径：%OUTPUT_PATH%

echo 正在打开输出文件目录...
cd /D "%~dp0"
explorer /select,"%OUTPUT_PATH%"

echo 正在打开输出文件...
start "" /D "%~dp0" "%OUTPUT_PATH%"

echo 3秒后自动关闭本窗口
timeout /t 3 >nul
exit