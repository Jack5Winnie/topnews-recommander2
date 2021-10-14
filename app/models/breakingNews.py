import pandas as pd
import datetime

def BreakingNews(hoursAgo):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(days=1)
    print("24小時 - 即時熱搜: 從 {0} 到現在 {1}".format(
        start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))
    hot_query= api.get_everything( q="NASDAQ APPLE", #category="business",
        from_param=start_time, to=end_time, page_size=50
    )
    hot_query_list= list(hot_query.items())
    hot_df = pd.DataFrame(hot_query_list)
    status = hot_df[1][0]
    totalResults = hot_df[1][1]
    df_articles = pd.DataFrame(hot_df[1][2])
    return df_articles