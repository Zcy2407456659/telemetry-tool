# 导入Python自带的两个工具：csv用来读表格，json用来存结果
import csv
import json

# 配置：输入文件名、输出文件名、最多读多少行
INPUT_CSV = "telemetry.csv"    # 要读的CSV文件名
OUTPUT_JSON = "result.json"    # 要生成的结果文件名
MAX_ROWS = 1000                # 最多读取1000行数据

def main():
    # 先准备几个变量，用来存统计结果
    height_sum = 0.0      # 高度的总和，最后用来算平均值
    data_count = 0        # 已经读了多少行数据
    max_speed = -float("inf")  # 最大速度，先设成无穷小
    min_battery = float("inf") # 最低电量，先设成无穷大

    # 打开CSV文件，开始逐行读
    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        # 按表头读取，这样可以直接用列名取数据
        reader = csv.DictReader(f)
        for row in reader:
            # 读够1000行就停下来
            if data_count >= MAX_ROWS:
                break

            # 从当前行里取出高度、速度、电量，从文字转成数字
            height = float(row["alt_m"])
            speed = float(row["speed_mps"])
            battery = float(row["battery_pct"])

            # 更新统计数据
            height_sum = height_sum + height
            data_count = data_count + 1
            if speed > max_speed:
                max_speed = speed
            if battery < min_battery:
                min_battery = battery

    # 计算平均高度
    if data_count > 0:
        avg_height = height_sum / data_count
    else:
        avg_height = 0

    # 把结果整理成固定格式
    result = {
        "average_height": round(avg_height, 2),   # 平均高度，保留2位小数
        "max_speed": round(max_speed, 2),         # 最大速度
        "min_battery": round(min_battery, 2)      # 最低电量
    }

    # 把结果写到 result.json 文件里
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # 在黑窗口里打印一下结果，方便你看
    print(f"处理完成，一共读取了 {data_count} 行数据")
    print("统计结果：", result)

# 程序从这里开始运行
if __name__ == "__main__":
    main()
