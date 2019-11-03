# web-application

數據科學開源工具第二次 presentation，利用 Python 寫一個獲取數據并分析數據的應用。

# 思路

1. 利用 requests 庫向 Github API 發請求
2. 獲取 requests 這個倉庫的各類信息，如 commit, issue, pull request, contributer, starer 等
3. 利用獲取的信息作圖并進行分析

# 工具

電腦系統：macOS 10.15
python 版本：3.7.4
編輯器：Visual Studio Code
版本管理工具：Git/GitKraken
請求工具：Postman

# 經驗總結

## 有部分接口需要指定 header

![require-header.jpg](material/require-header.jpg)

> To access the API, you must provide a custom media type in the Accept header

## 單個接口數據量太大

![pagination.jpg](material/pagination.jpg)

github 會通過 page 參數進行數據分頁處理，總頁數信息會放在響應的 header 中：

> Link: <https://api.github.com/user/repos?page=3&per_page=100>; rel="next",
>   <https://api.github.com/user/repos?page=50&per_page=100>; rel="last"

在請求某些大數據量的接口時，要先發送一次請求以獲取分頁信息，通過正則表達式提取頁數再進行下一次請求。

## 請求次數限制

![unauthenticated-request.jpg](material/unauthenticated-request.jpg)

github 會對未取得認證的請求進行限制，根據 IP 地址每小時只能請求 60 次。

取得認證后每小時可以請求 5000 次。

# 參考鏈接

[Github API docs](https://developer.github.com/v3/)

[requests repository](https://github.com/psf/requests)

[requests docs](https://requests.readthedocs.io)

[Google 开源项目 Python 风格规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules)