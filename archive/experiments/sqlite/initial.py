import sqlite3
import sys
import os # 新增 os 模組用於刪除檔案

# --- 1. 數據庫設定與準備 ---
DB_NAME = 'ai_project.db'

# 數據
SALES_DATA = [
    ('Angelo', 'Tiramisu', '2025-10-18', 2, 120.00),
    ('Jane', 'Cheesecake', '2025-10-18', 1, 95.00),
    ('Angelo', 'Brownie', '2025-10-19', 3, 45.00),
    ('Mary', 'Tiramisu', '2025-10-19', 1, 120.00),
    ('Jane', 'Brownie', '2025-10-20', 4, 45.00),
    ('David', 'Cheesecake', '2025-10-20', 2, 95.00),
    ('Tom', 'Cookie', '2025-10-21', 5, 20.00) 
]
CUSTOMER_DATA = [
    ('Angelo', 'North', 'Gold'),
    ('Jane', 'South', 'Silver'),
    ('Mary', 'North', 'Normal'),
    ('David', 'South', 'Normal'),
    ('Susan', 'East', 'Gold')
]

# --- 關鍵修正：在運行前刪除舊的 DB 檔案 ---
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
    print(f"已刪除舊資料庫檔案: {DB_NAME}")


def setup_database(conn):
    """創建並填充兩個表格：dessert_sales 和 customer_info"""
    cursor = conn.cursor()

    # 創建訂單表 (dessert_sales)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dessert_sales (
            sale_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            dessert_item TEXT NOT NULL,
            sale_date TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );
    """)
    cursor.executemany("""
        INSERT INTO dessert_sales (customer_name, dessert_item, sale_date, quantity, price)
        VALUES (?, ?, ?, ?, ?)  
    """, SALES_DATA)

    # 創建客戶資訊表 (customer_info)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_info (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL UNIQUE,
            region TEXT NOT NULL,
            vip_level TEXT DEFAULT 'Normal'
        );
    """)
    cursor.executemany("""
        INSERT INTO customer_info (customer_name, region, vip_level)
        VALUES (?, ?, ?) 
    """, CUSTOMER_DATA)

    conn.commit()
    print("--- 數據庫設置完成：兩個表格已準備好 ---")

# --- 2. SQL 查詢執行函數 ---

def run_sql_query(conn, sql_query):
    """執行 SQL 查詢並打印結果"""
    print(f"\n執行 SQL: \n{sql_query.strip()}")
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()

        if results:
            print("\n--- SQL 查詢結果 ---")
            header = " | ".join(columns)
            separator = "-" * len(header)
            
            print(header)
            print(separator)
            for row in results:
                print(" | ".join(map(str, row)))
            print(f"({len(results)} rows)")
        else:
            print("\n--- 查詢結果為空 ---")

    except sqlite3.OperationalError as e:
        print(f"\n--- 錯誤 (OperationalError) --- \n{e}")
    except Exception as e:
        print(f"\n--- 發生未預期錯誤 --- \n{e}")

# --- 3. 挑戰 SQL 語句 (模擬 RIGHT JOIN) ---

CHALLENGE_12B_SQL = """
SELECT 
    T2.customer_name, 
    T1.dessert_item, 
    T2.vip_level
FROM 
    customer_info AS T2  -- 主表：所有客戶
LEFT JOIN 
    dessert_sales AS T1  -- 副表：訂單數據
ON 
    T2.customer_name = T1.customer_name;
"""


# --- 4. 主執行邏輯 ---
if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DB_NAME)
        setup_database(conn)
        
        # 運行今天的挑戰 (撈出所有客戶，無論是否有訂單)
        run_sql_query(conn, CHALLENGE_12B_SQL)
        
    except Exception as e:
        print(f"致命錯誤：{e}")
        sys.exit(1)
    finally:
        if 'conn' in locals() and conn:
            conn.close()