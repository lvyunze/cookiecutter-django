# Cookiecutter Django 模板

中文 | [English](README.md)

## 概述

这是一个用于快速创建 Django 项目的 Cookiecutter 模板,集成了最佳实践和现代化开发工作流。

## 特性

- 🚀 **快速启动**: 几秒钟内生成完整的 Django 项目结构
- 🎨 **现代化技术栈**: 预配置 Django 最佳实践
- 👥 **用户管理**: 内置自定义用户模型和认证系统
- 🔒 **安全性**: 开箱即用的安全配置
- 📦 **静态文件**: 组织良好的静态文件结构 (CSS, JS)
- 🎯 **管理界面**: 自定义 Django 管理后台模板
- 🔐 **双因素认证**: 可选的 2FA 支持模板
- ⚙️ **环境变量**: 支持 `.env` 文件进行配置管理

## 项目结构

```
{{cookiecutter.project_name}}/
├── static/                 # 静态文件 (CSS, JS)
│   ├── css/
│   └── js/
├── templates/              # HTML 模板
│   ├── admin/             # 自定义管理后台模板
│   ├── two_factor/        # 双因素认证模板
│   └── base.html          # 基础模板
├── users/                  # 用户应用
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── {{cookiecutter.project_name}}/  # 主项目配置
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .env.example
```

## 环境要求

- Python 3.8+
- pip
- cookiecutter

## 安装使用

### 1. 安装 Cookiecutter

```bash
pip install cookiecutter
```

### 2. 生成项目

```bash
cookiecutter https://github.com/lvyunze/cookiecutter-django
```

或者如果你已经克隆了本仓库到本地:

```bash
cookiecutter /path/to/cookiecutter-django
```

### 3. 按照提示输入

系统会提示你输入:
- **project_name**: 你的项目名称 (例如: "我的超棒项目")

模板会自动生成具有适当结构的项目。

## 生成后配置

生成项目后:

### 1. 进入项目目录

```bash
cd <your_project_name>
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Windows 系统: venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件填入你的配置
```

### 5. 执行数据库迁移

```bash
python manage.py migrate
```

### 6. 创建超级用户

```bash
python manage.py createsuperuser
```

### 7. 启动开发服务器

```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000` 查看你的应用。

## 自定义配置

### 模板变量

模板使用自定义的 Jinja2 分隔符以避免与 Django 模板冲突:

- 变量: `<< variable >>`
- 块: `<<% block %>>` 
- 注释: `<<# comment #>>`

### 不渲染的文件

以下文件类型会直接复制而不进行 Jinja2 渲染:
- JavaScript 文件 (*.js)
- CSS 文件 (*.css)
- 压缩文件 (*.min.js, *.min.css)
- 图片文件 (*.jpg, *.jpeg, *.png, *.gif, *.svg, *.ico)
- 字体文件 (*.woff, *.woff2, *.ttf, *.eot)

## 内置应用

### Users 应用

自定义用户应用包含:
- 继承 Django AbstractUser 的自定义用户模型
- 用户管理后台配置
- 可随时自定义扩展

## 开发

### 生成前钩子

`hooks/pre_gen_project.py` 脚本会在项目生成前运行,用于验证输入并执行必要的设置。

## 最佳实践

本模板遵循 Django 最佳实践:

- ✅ 从一开始就使用自定义用户模型
- ✅ 基于环境的配置管理
- ✅ 组织良好的静态文件和模板
- ✅ 合理的应用结构
- ✅ 配置好的安全设置
- ✅ 可直接部署

## 贡献

欢迎贡献! 请随时提交 Pull Request。

## 许可证

本项目采用 MIT 许可证。

## 支持

如果遇到任何问题或有疑问,请在 GitHub 上提交 issue。

---

**祝编码愉快!** 🎉
