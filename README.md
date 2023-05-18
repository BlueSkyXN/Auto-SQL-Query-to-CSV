# 基本介绍
GitHub仓库 @BlueSkyXN
： https://github.com/BlueSkyXN/Auto-SQL-Query-to-CSV


自动化核心文件：Auto-SQL-Query-to-CSV.exe 

可执行文件的Linux系统是无后缀的、Windows是EXE的、Python源码在仓库

Action自动编译/打包后的应用程序在每个Action的单次WorkFlows执行中的Summary中的Artifacts工件里面

## 文件编码提示

由于Linux和很多程序默认使用UTF8，而Windows默认文件编码是ANSI（GBK），因此某些情况下可能有问题，所以也额外写了个 UTF8格式转ANSI格式的工具（一般来说支持CSV和TXT，BAT等格式目前不支持该功能也可以通过Windows记事本另存为/Notepad3/EditPlus/VSCode等软件来实现。

# Auto-SQL-Query-to-CSV
这里以Windows环境下的 Auto-SQL-Query-to-CSV.exe为例，本案例基于0.6版本

- [-q] [--query] 指定查询语句存放的文件的路径位置
- [-i] [--input] [--info] 指定存放数据库连接信息的文件的路径位置
- [-o] [--output] 指定输出文件的路径位置，包括文件名
- [-c] [--encoding] 指定输出文件的编码，可选 ANSI、UTF8/UTF-8；支持首字母A/U并兼容大小写
- [-s] 获取输入文件的模板，可不用这个参数

## 使用参考

```E:\SQL\Auto-SQL-Query-to-CSV.exe -q E:\SQL\PySQL-Q.txt -i E:\SQL\PySQL-Info.txt -o E:\Output-Q.csv```

# UTF8-to-ANSI_CSV
这里以Windows环境下的 UTF8-to-ANSI_CSV.exe为例，本案例基于0.6版本

- [-i] [--input] 指定存放数据库连接信息的文件的路径位置
- [-o] [--output] 指定输出文件的路径位置，包括文件名

正常情况下该程序不会在终端打印输出信息

## 使用参考

```E:\SQL\UTF8-to-ANSI_CSV.exe -i E:\SQL\PySQL-Q1.txt -o  E:\SQL\PySQL-Q2.txt```