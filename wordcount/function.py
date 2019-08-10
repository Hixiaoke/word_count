# !/user/bin/env python
# _*_ coding:utf-8 _*_
# author:Mr.xiao
# time:2019/8/9 0009
# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('你好')
    return render(request, 'home.html')


def count(request):
    # 用户文本
    user_text = request.GET['text']
    # 总字数
    total_count = len(user_text)
    # 统计字数出现的次数
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # 选出字出现最多的次数,\指的是续行符
    sorted_dict = \
        sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

    # return HttpResponse('你好')
    # render能向html网页传递一些信息
    return render(request, 'count.html',
                  {'count': total_count, 'text': user_text,
                   'wordict': word_dict, 'sorted': sorted_dict})
