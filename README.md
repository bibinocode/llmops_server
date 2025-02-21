# LLM_Server

- 这是一个用于LLMOps可视化平台的服务端

# 启动项目

```bash
python -m venv venv
cd venv/Scripts
activate
cd ..
cd ..
pip install -r requirements.txt
python -m app.http.app
```

## 依赖导出

```bash
pip freeze > requirements.txt
```

## 待实现功能

1. [ ] Postgres数据库接入
2. [ ] LangChain 接入
3. [ ] 记忆模块
4. [ ] 编排模块
5. [ ] 授权认证模块
6. [ ] 开放API模块
7. [ ] 插件市场模块
8. [ ] 知识库模块
9. [ ] 审核模块