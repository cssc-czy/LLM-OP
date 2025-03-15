tools = [
    {
        "type": "function",
        "function": {
            "name": "exec",
            "description": "执行单行Linux shell命令，返回执行命令的输出",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "需要执行的单行命令",
                    }
                },
                "required": ["command"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "baidu_search",
            "description": "使用百度引擎在网络上给定的查询内容，返回搜索结果列表，列表格式为JSON",
            "parameters": {
                "type": "object",
                "properties": {
                    "context": {
                        "type": "string",
                        "description": "具体的搜索内容，请精确描述",
                    }
                },
                "required": ["context"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "url_2_text",
            "description": "获取url对应页面的内容，并将对应HTTP报文返回，你可以考虑进入页面里的其他链接或就页面内容进行思考",
            "parameters": {
                "type": "object",
                "properties": {
                    "context": {
                        "type": "string",
                        "description": "url地址，请完整无误地提供",
                    }
                },
                "required": ["context"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "download_and_extract",
            "description": "根据给定的URL地址下载文件，返回下载文件的保存路径",
        },
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "需要下载的文件的URL地址",
                },
                "save_dir": {
                    "type": "string",
                    "description": "下载文件的保存文件夹路径，如果文件夹不存在将创建该文件夹",
                }
            },
            "required": ["url", "save_dir"]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "向指定文件中写入给定文本内容",
        },
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "需要写入的文件路径",
                },
                "content": {
                    "type": "string",
                    "description": "需要写入的文本内容",
                }
            },
            "required": ["file_path", "content"]
        }
    },

]

