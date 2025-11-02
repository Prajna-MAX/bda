import pandas as pd
import subprocess
import os

# 1️⃣ Load Excel file into DataFrame
excel_path = "processed_purchase_frequency.xlsx"
purchase_frequency = pd.read_excel(excel_path)

# 2️⃣ Save it locally as CSV
local_csv = "processed_purchase_frequency.csv"
purchase_frequency.to_csv(local_csv, index=False)

# 3️⃣ Define your target HDFS path
hdfs_dir = "/user/hadoop/purchase_frequency/"
hdfs_path = hdfs_dir + os.path.basename(local_csv)

# 4️⃣ Create HDFS directory if it doesn’t exist
subprocess.run(["hdfs.cmd", "dfs", "-mkdir", "-p", hdfs_dir], check=True)

# 5️⃣ Upload CSV to HDFS
subprocess.run(["hdfs.cmd", "dfs", "-put", "-f", local_csv, hdfs_path], check=True)

print(f"✅ File successfully uploaded to HDFS: {hdfs_path}")
print("🌐 You can now view it at:")
print(f"http://localhost:9870/explorer.html#{hdfs_path}")
