# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
import jieba

def CountVectEng():

    cv = CountVectorizer()
    data = cv.fit_transform(
        ["live on the earth,life on the free,i like spring", "live on the moon,life on the happy,you like summer"])

    print(cv.get_feature_names())  # 所有的词，重复的只看作一次，对单个英文字母不统计，a,b,c没有分类意义
    print(data)  # 每个词在每篇文章中出现的次数
    return None


def CountVectChinese():

    cv = CountVectorizer()
    data = cv.fit_transform(
        ["人生 苦短，我用 python", "路漫漫 其修远兮,吾将上下 而求索"])
    print(cv.get_feature_names())
    # ['python', '人生', '其修远兮', '吾将上下', '我用', '而求索', '苦短', '路漫漫']
    print(data.toarray())
    return None


def CountVectCh():

    lis = [
        "2019年12月2日，知名媒体人剩闲小师傅特意从朋友处看到了发过来的人民日报直播专访胡歌的视频，胡歌在专访中宣传自己的新电影《南方车站的聚会》，并且表达来的一些作为演员的心得观念",
        "胡歌直言：创造型快乐才能持续成长。“经历了人生当中的挫折，不能仅仅只是再红一次。如果要继续做演员，至少我不能重复。",
        "胡歌在早些年前经历了一次车祸，生死只在一线之间，然而上天给了他生的机会，重新回过来头来想，这第二次生命，再继续前面的道路，做演员，做一名优秀的演员，而且让自己还能红一次，"
        "那么意义就不仅仅于此，而是要在电影中诠释不同的角色，正所谓记住我演的角色，但是可以忘记胡歌"
    ]
    data_list = []
    for info in lis:
        data_list.append(" ".join(list(jieba.cut_for_search(info))))

    cv = CountVectorizer()
    data = cv.fit_transform(data_list)
    print(cv.get_feature_names())
    # ['12', '2019', '一些', '一名', '一次', '一线', '上天', '不仅', '不仅仅', '不同', '不能', '专访', '之间', '二次', '人民', '人民日报', '人生', '仅仅', '仅仅只是', '仅只', '他生', '优秀', '但是', '作为', '再红', '创造', '创造型', '前面', '剩闲', '南方', '发过', '发过来', '只是', '可以', '回过', '如果', '媒体', '宣传', '师傅', '年前', '并且', '当中', '心得', '忘记', '快乐', '意义', '成长', '我演', '所谓', '才能', '持续', '挫折', '日报', '早些', '朋友', '机会', '来头', '演员', '然而', '特意', '生命', '生死', '电影', '直播', '直言', '看到', '知名', '第二', '第二次', '经历', '继续', '而且', '而是', '聚会', '胡歌', '自己', '至少', '表达', '观念', '视频', '角色', '记住', '诠释', '车祸', '车站', '过来', '造型', '道路', '那么', '重复', '重新']

    print(data.toarray())
    return None

if __name__ == "__main__":
    CountVectEng()
    CountVectChinese()
    CountVectCh()