import requests
import csv
import json

def fetch_jgrants_subsidies():
    url = "https://api.jgrants-portal.go.jp/exp/v1/public/subsidies"
    output_file = "subsidies_list.csv"
    
    # 仕様書に基づいた厳密なパラメータ設定
    params = {
        "keyword": "事業",
        "sort": "created_date",
        "order": "DESC",            
        "acceptance": "1"                
    }

    try:
        print(f"データを取得中...")
        response = requests.get(url, params=params)
        
        # エラー発生時に詳細を表示するための処理
        if response.status_code != 200:
            print(f"エラーが発生しました（ステータスコード: {response.status_code}）")
            print(f"詳細メッセージ: {response.text}")
            return

        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))
        
        # APIのレスポンスが直接リストではない場合を考慮
        subsidies = data if isinstance(data, list) else data.get('result', [])

        if not subsidies:
            print("条件に一致するデータがありませんでした。")
            return

        # CSV書き出し
        headers = subsidies[0].keys()
        with open(output_file, mode='w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(subsidies)

        print(f"成功！ {len(subsidies)} 件のデータを '{output_file}' に保存しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    fetch_jgrants_subsidies()