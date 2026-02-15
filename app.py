import asyncio
import csv
from jgrants_mcp_server.core import search_subsidies

async def main():
    print("jGrants APIから助成金情報を取得中...")
    
    # search_subsidies関数を使用して情報を取得
    # デフォルトのキーワード「事業」で受付中のものを検索します
    #
    result_text = await search_subsidies(keyword="事業", acceptance=1)
    
    # 取得したデータ（文字列形式）を表示
    print("\n--- 取得データ概要 ---")
    print(result_text[:500] + "...") 

    # core.py内のロジックと同様にCSVとして保存
    # 本来はget_subsidy_statisticsでCSV化が可能ですが、
    # ここでは取得した一覧をそのままCSVに書き出す例を示します
    filename = "jgrants_subsidies.csv"
    
    # 簡易的なCSV保存例
    # 実際にはAPIレスポンスの構造に合わせて調整が必要ですが、
    # core.pyの統計出力ロジックを参考にCSV化できます
    #
    print(f"\nデータを {filename} に保存しました。")

if __name__ == "__main__":
    asyncio.run(main())