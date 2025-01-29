# Obsidian双向链接转mkdocs
插件：[mkdocs-obsidian-bridge](https://github.com/GooRoo/mkdocs-obsidian-bridge)

😢 遇到分隔符的问题，在issue里有人提出来了，但暂时没有解决

💓 推荐插件：[mkdocs-obsidian-support-plugin](https://github.com/ndy2/mkdocs-obsidian-support-plugin)

- 支持 obsidian 的 callout 转为 mkdocs-material 的 admonition
- 支持 obsidian 的 comment 转为 mkdocs-material 的 comment
- 支持 obsidian 的双向链接
- 支持 obsidian 多 tab 转 mkdocs-material 的多 tab
- ……

# 自动目录生成
插件：[MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

目标：obsidian在docs目录下创建的一级文件夹作为网站顶端导航，二级目录作为一级目录的子内容，例如AI下有CV，有NLP……，二级目录里包含一系列文件，中间用Section分割
## 使用方式
### 自定义导航
在根目录下创建.pages文件，使用nav属性来排布顺序和子目录
