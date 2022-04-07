# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
def TfidfChinese():
    info_list = [
        "2019年12月2日，知名媒体人剩闲小师傅特意从朋友处看到了发过来的人民日报直播专访胡歌的视频，胡歌在专访中宣传自己的新电影《南方车站的聚会》，并且表达来的一些作为演员的心得观念",
        "胡歌直言：创造型快乐才能持续成长。“经历了人生当中的挫折，不能仅仅只是再红一次。如果要继续做演员，至少我不能重复。",
        "胡歌在早些年前经历了一次车祸，生死只在一线之间，然而上天给了他生的机会，重新回过来头来想，这第二次生命，再继续前面的道路，做演员，做一名优秀的演员，而且让自己还能红一次，"
        "那么意义就不仅仅于此，而是要在电影中诠释不同的角色，正所谓记住我演的角色，但是可以忘记胡歌"
    ]
    data_list = []
    for info in info_list:
        data_list.append(" ".join(list(jieba.cut_for_search(info))))
    tf = TfidfVectorizer()
    data = tf.fit_transform(data_list)
    print(tf.get_feature_names())
    print(data.toarray())  # 重要性
if __name__ == "__main__":
    TfidfChinese()