import requests

# 提供身份資訊
str_username = "Dio"
str_password = "kim8865910"

# 直接使用身份信息进行 API 调用（GET 请求）
api_url = "http://127.0.0.1:8000/v1/api_python_api_text/"
api_data = {
    "username": str_username,
    "password": str_password,
}

api_response = requests.post(api_url, auth=(str_username, str_password))  # 傳遞訊息過去API
# 检查响应状态码
if api_response.status_code == 200:
    try:
        api_result = api_response.json()
        verification_result = api_result.get("verification_result")

        # 得到结果
        if verification_result:
            print("用户正确! OK!")
        else:
            print("用户失败! NO!")

    except requests.exceptions.JSONDecodeError:
        print("無法解析 JSON 數據")

else:
    print(f"失敗，伺服器代碼: {api_response.status_code}")





# # 構建基本認證的憑證
# credentials = f"{input_username}:{input_password}"
# base64_credentials = base64.b64encode(credentials.encode()).decode("utf-8")
#
# # 構建身份驗證頭部
# headers = {
#     "Authorization": f"Basic {base64_credentials}",
#     # 其他可能需要的頭部信息，根據 API 的要求添加
# }

# # 發起 API 請求
# api_url = "http://127.0.0.1:8000/v1/articles/"
# api_response = requests.get(api_url,)
# api_result = api_response.json()


# # 打印结果到控制台
# print("API 调用结果:")
# print(api_result)


# # 直接使用身份信息进行 API 调用（GET 请求）
# api_url = "http://127.0.0.1:8000/v1/articles/"
# api_data = {
#     "username": username,
#     "password": password,
# }
#
# api_response = requests.post(api_url, params=api_data)
# api_result = api_response.json()


# # 直接使用身份信息进行 API 调用
# sql_query = "上面的 SQL 查詢"
# sql_execution_url = "https://127.0.0.1:8000/execute_sql"
# sql_execution_data = {
#     "username": username,
#     "password": password,
#     "sql": sql_query
# }
#
# sql_execution_response = requests.post(sql_execution_url, json=sql_execution_data)
# sql_execution_result = sql_execution_response.json()
#
# if sql_execution_result["message"] == "完成測試":
#     print("SQL 查詢成功執行")
# else:
#     print("SQL 查詢執行失敗")