爬取知乎答案图片（已失效）
由于知乎反扒策略更新，现已失效，记录下思路，以后可能会重构。

进入问题后，先打开发者工具，然后一再向下拉，知乎会动态加载更多答案，这时在开发者工具中找到answer相关请求，其中包含了回答相关内容，在请求头中找到真是url和请求相关参数，用python进行模拟。