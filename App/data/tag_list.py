import requests
from utils.load_env import API_URL

def get_tag_list():
    """tagsテーブルからタグリストを取得する"""
    if not API_URL:
        print("警告: API_URLが設定されていません。.envファイルを確認してください。")
        return []
    
    try:
        response = requests.get(f"{API_URL}/tags/")
        if response.status_code == 200:
            tags = response.json()
            return [tag['name'] for tag in tags]
        print(f"警告: APIからの応答が不正です。ステータスコード: {response.status_code}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"警告: APIへの接続に失敗しました: {str(e)}")
        return []