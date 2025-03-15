from openai import OpenAI
import json
import os
from tool_funcs import *

# 标准 OpenAI API 接口
client = OpenAI(
    api_key="sk-WfHImmxxxxxxxxxxxxOhR6",
    base_url="http://192.168.223.67:8000/v1",
)

def send_messages(messages, tools):
    response = client.chat.completions.create(
        model="QwQ-32B",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # 启用自动工具选择
    )
    return response.choices[0].message



def flow(messages, tools):
    print("等待模型响应")
    message = send_messages(messages, tools)
#     messages.append({
#     "role": message.role,
#     "content": message.content
# })
    print(f"模型>\t {message.content}")
    if len(message.tool_calls)==0:
        messages.append({'role':'system','content':"用户不需要知道如何操作，请您作为系统管理员自行查询与执行操作，若结束操作请直接返回exit"})
    for tool in  message.tool_calls:
        print(f"等待函数执行:{tool.function.name}")
        if tool.function.name == "exec":
            print(f"exec>\t {tool.function.arguments}")
        elif tool.function.name == "baidu_search":
            print(f"baidu_search>\t {tool.function.arguments}")
            messages.append({"role": "system", "content": "记住你才是系统管理员，用户不会对你的思考反馈信息，需要你独自操作"})
        elif tool.function.name == "url_to_text":
            print(f"url_to_text>\t {tool.function.arguments}")
            messages.append({"role": "system", "content": "你可以考虑进入页面里的其他链接或就页面内容进行思考，并且记住你才是系统管理员，用户不会对你的思考反馈信息，需要你独自操作"})
        func = funcs_map[tool.function.name] # 解析执行函数
        arguments = json.loads(tool.function.arguments) # 解析函数参数
        # 将函数输出添加至messages中
        res = func(**arguments)
        messages.append({"role": "tool", "tool_call_id": tool.id, "content": res})
        
    return messages
            
