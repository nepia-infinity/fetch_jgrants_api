

import asyncio
from fastmcp.client import Client
import json

async def main():
    """
    JグランツMCPサーバーに接続し、補助金を検索して結果を表示するクライアントアプリケーション。
    """
    # サーバーのURL
    server_url = "http://127.0.0.1:8000/mcp"
    
    print(f"'{server_url}' のサーバーに接続します...")
    
    try:
        # 'async with' を使うと、接続と切断が自動的に管理されます。
        async with Client(server_url) as client:
            print("サーバーに接続し、ツールを呼び出します。")
            
            # --- 補助金を検索 ---
            tool_name = "search_subsidies"
            keyword_to_search = "DX"
            print(f"ツール '{tool_name}' をキーワード '{keyword_to_search}' で実行します...")
            
            # client.call() を使ってツールを実行
            search_result = await client.call(tool_name, keyword=keyword_to_search)
            
            # 結果を整形して表示
            print("\n--- 検索結果 ---")
            if search_result and search_result.get('items'):
                # 結果を見やすいようにJSON形式でインデントして表示
                print(json.dumps(search_result, indent=2, ensure_ascii=False))
                print(f"\n合計 {search_result.get('total_count', 0)} 件の補助金が見つかりました。")
            else:
                print("指定されたキーワードに一致する補助金は見つかりませんでした。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # Windows環境での非同期処理に関する注意：
    # もし `RuntimeError: Event loop is closed` のようなエラーが出る場合、
    # 以下の行のコメントを解除して試してください。
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(main())

