无人机地面站开发项目 - 第一周
 
项目简介
 
本项目为无人机地面站系统的基础开发工程，第一周完成开发环境搭建、个人代码仓库初始化，以及基础遥测数据解析工具开发；支持 CSV 格式无人机遥测数据的统计分析，可输出核心飞行指标的 JSON 结果文件。
 
环境要求
 
- Python 3.12（当前开发使用版本）

- VSCode 代码编辑器

- Git 版本控制工具

- 兼容系统：Windows / Linux / macOS
 
 
 
一、环境安装说明
 
1. Python 3.12
 
- 安装方式：从 Python 官网 下载 3.12.x 稳定版安装包，安装时勾选 Add Python to PATH

- 验证命令：
 

- 说明：当前阶段脚本仅使用 Python 标准库（ csv  /  json ），无需额外安装第三方依赖。
 
2. VSCode
 
- 安装方式：从 VSCode 官网 下载对应系统安装包，默认路径安装即可

- 推荐配套插件：Python（微软官方）、GitLens、JSON Tools
 
3. Git
 
- 安装方式：从 Git 官网 下载安装包，默认配置完成安装

- 验证命令：
 
- 基础配置（首次使用需执行）：
 
 
二、仓库与运行说明
 
仓库初始化
 

代码提交与推送
 

遥测解析脚本使用
 
 parse_telemetry.py ：读取 1000 行 CSV 遥测数据，计算平均高度、最大速度、最低电量，输出到  result.json 。
 
1. 输入要求

- 将待解析文件命名为  telemetry.csv ，放在项目根目录

- CSV 首行表头需包含： timestamp,altitude,speed,battery 

-  altitude ：飞行高度，单位 m

-  speed ：飞行速度，单位 m/s

-  battery ：剩余电量，单位 %

2. 运行命令
 

3. 输出结果
运行完成后，根目录生成  result.json 
