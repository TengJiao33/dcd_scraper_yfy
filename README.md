
# 汽车垂直网站评论数据爬虫集合

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个用于从主流汽车垂直网站（如懂车帝、汽车之家等）爬取指定车型用户口碑、评论等公开数据的Python爬虫项目集合。

## 📖 项目简介

本项目包含一系列独立的爬虫脚本，每个脚本针对一个特定的车型或网站。主要目的是为了学习和研究网络数据爬取技术，以及对收集到的数据进行后续的分析。所有爬取的数据均会以 `.csv` 格式保存在本地。

## ✨ 功能特点

- **多数据源支持**: 已包含针对**懂车帝**、**汽车之家**等网站的爬虫。
- **目标车型明确**: 提供了针对**丰田凯美瑞**、**特斯拉Model 3**、**比亚迪汉**、**吉利星越**等多款热门车型的爬取脚本。
- **健壮的错误处理**: 脚本中包含了基本的异常捕获和超时处理，能应对一些常见的网络问题。
- **数据持久化**: 爬取结果可直接保存为 `.csv` 文件，方便使用Excel、Pandas等工具进行后续数据分析。
- **配置简单**: 核心参数（如车型ID、爬取页数）在脚本内有清晰的注释，方便修改和扩展。

## 📂 项目结构

```

.
├── 比亚迪汉ev爬取1.py     \# 爬取比亚迪汉EV评论的脚本
├── 懂车帝tesla\_model3\_API调用.py  \# 爬取特斯拉Model 3评论的脚本
├── 凯美瑞爬取1.py         \# 爬取丰田凯美瑞评论的脚本
├── 星越爬取1.py           \# 爬取吉利星越评论的脚本
├── 汽车之家.py            \# 针对汽车之家的通用爬虫框架（示例）
├── ...                   \# 其他爬虫脚本
├── requirements.txt      \# 项目依赖库列表
├── .gitignore            \# Git忽略文件配置
└── README.md             \# 你正在阅读的这个文件

````

## 🚀 安装与使用

请确保你的电脑已经安装了 `Python 3.8` 或更高版本。

**1. 克隆项目到本地**

```bash
git clone [https://github.com/你的用户名/你的仓库名.git](https://github.com/你的用户名/你的仓库名.git)
cd 你的仓库名
````

**2. 创建并激活虚拟环境 (推荐)**


  - **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
  - **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

**3. 安装依赖库**

本项目依赖 `requests` 和 `pandas` 等库。我们已经将它们记录在 `requirements.txt` 文件中。

```bash
pip install -r requirements.txt
```

*(如果还没有 `requirements.txt` 文件，可以通过 `pip freeze > requirements.txt` 命令生成)*



脚本运行结束后，你会在项目根目录下找到一个名为 `dcd_camry_reviews_final_robust.csv` (或类似名称) 的文件，其中包含了所有爬取到的数据。

## ⚙️ 如何配置

每个爬虫脚本的核心参数都集中在文件的头部或 `if __name__ == "__main__":` 部分，方便用户自定义。

以 `凯美瑞爬取1.py` 为例，你可以轻松修改以下参数来爬取其他车型或调整爬取范围：

```python
# --- 主程序入口 ---
if __name__ == "__main__":
    # 您只需修改下面这两行即可切换目标车型
    CAR_NAME = "camry"  # 车型名称，用于保存文件名
    SERIES_ID = "535"     # 丰田凯美瑞的车系ID (需要从懂车帝网站URL中查找)
    
    # 您也可以按需修改希望爬取的总页数
    TOTAL_PAGES_TO_SCRAPE = 500

    scrape_dcd_reviews_robust(CAR_NAME, SERIES_ID, max_pages=TOTAL_PAGES_TO_SCRAPE)
```

## ⚠️ 注意事项

  - 本项目仅用于个人学习和技术研究，请勿用于任何商业用途。
  - 请遵守目标网站的 `robots.txt` 协议，尊重网站的版权和数据隐私。
  - 请不要进行过于频繁的请求，以免对目标网站服务器造成不必要的负担。若因使用不当造成任何后果，开发者概不负责。
  - 网站的页面结构或API可能会随时变更，届时爬虫脚本可能需要进行相应的维护和更新。


```
```
