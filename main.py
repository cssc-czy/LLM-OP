from flow import flow
from tool_discribes import tools

system = {"role": "system", "content": "你是一个windows系统管理员，你可以执行cmd命令，\
     你可以搜索网络上的信息，你可以获取url对应页面的内容，并将对应HTTP报文返回，\
     你可以考虑进入页面里的其他链接或就页面内容进行思考，现在你需要针对用户的请求进行操作 \
     在开始操作之前，你可以先调用exec函数，执行查看系统相关情况的命令，如果你想结束所有操作，请直接输出 “exit”"}

messages = [
    system,
    {"role": "user", "content": "你好，系统上有一个名字为test的conda环境，请帮我在其中安装版本为2.2.1的pytorch，再写一个测试pytorch是否正常使用cuda代码脚本并执行"},
]
num=0
while 'exit' not in messages[-1]['content'].split('think')[-1]:
    num += 1
    if num % 5 == 0:
        messages += [system]
    messages = flow(messages, tools)
    print(f"==========================第{num}轮思考与操作=================================")

