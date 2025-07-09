import requests
import pandas as pd
import time
import random
from datetime import datetime

def scrape_dcd_reviews_robust(car_name, series_id, max_pages=50, city_name="杭州"):
    """
    从懂车帝平台爬取指定车系的评论数据（健壮版，能处理数据缺失问题）。
    """
    print(f"开始爬取车型: {car_name}, 车系ID: {series_id}")
    
    base_url = "https://www.dongchedi.com/motor/pc/car/series/get_review_list"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': f'https://www.dongchedi.com/auto/series/score/{series_id}'
    }

    all_data = []

    for i in range(1, max_pages + 1):
        params = {
            'series_id': series_id,
            'page': i,
            'size': 20,
            'city_name': city_name,
            'sort_by': 'default'
        }
        
        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            if not data.get('data') or not data['data'].get('review_list'):
                print(f"第 {i} 页没有更多评论了，爬取结束。")
                break

            review_list = data['data']['review_list']
            print(f"成功获取第 {i} 页数据，包含 {len(review_list)} 条评论。")

            for review in review_list:
                if not isinstance(review, dict):
                    print(f"警告：在第 {i} 页发现一条格式错误的评论，已跳过。")
                    continue

                user_info = review.get('user_info') or {}
                buy_car_info = review.get('buy_car_info') or {}
                score_info = review.get('score_info') or {}
                motor_auth_info = user_info.get('motor_auth_show_info') or {}

                create_timestamp = review.get('create_time')
                publish_date = datetime.fromtimestamp(create_timestamp).strftime('%Y-%m-%d') if create_timestamp else None
                
                rating_score = score_info.get('score')
                final_rating = rating_score / 100.0 if rating_score is not None else None

                extracted_review = {
                    '评论ID': review.get('gid_str'),
                    '用户昵称': user_info.get('name'),
                    '用户ID': user_info.get('user_id'),
                    '用户认证信息': motor_auth_info.get('auth_v_desc'),
                    '发布日期': publish_date,
                    '点赞数': review.get('digg_count_en'),
                    '评论数': review.get('comment_count_en'),
                    '评论正文': review.get('content'),
                    '购买车型': buy_car_info.get('car_name'),
                    '购买地点': buy_car_info.get('location'),
                    '裸车价格': buy_car_info.get('price'),
                    '综合评分': final_rating
                }
                all_data.append(extracted_review)

            sleep_time = random.uniform(1.5, 3.5)
            print(f"暂停 {sleep_time:.2f} 秒...")
            time.sleep(sleep_time)

        except requests.exceptions.RequestException as e:
            print(f"请求第 {i} 页时发生网络错误: {e}")
            break
        except Exception as e:
            print(f"处理第 {i} 页数据时发生未知错误: {e}")
            break
            
    df = pd.DataFrame(all_data)
    output_filename = f"dcd_{car_name}_reviews_final_robust.csv"
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"\n爬取完成！共获取 {len(all_data)} 条评论，数据已保存至 {output_filename}")

# --- 主程序入口 ---
if __name__ == "__main__":
    # 您只需修改下面这两行即可切换目标车型
    CAR_NAME = "camry"  # 车型名称，用于保存文件名
    SERIES_ID = "535"     # 丰田凯美瑞的车系ID
    
    # 您也可以按需修改希望爬取的总页数
    TOTAL_PAGES_TO_SCRAPE = 500

    scrape_dcd_reviews_robust(CAR_NAME, SERIES_ID, max_pages=TOTAL_PAGES_TO_SCRAPE)