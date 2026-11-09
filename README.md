# 开始

> 推荐使用的skill


## 全局配置
### claude code
```txt
~/.claude/
├── CLAUDE.md
├── rules/
│   ├── architecture.md
│   └── clean-code.md
└── skills/
    └── architecture-review/
        └── SKILL.md
```

### codex
```txt
project/
├── AGENTS.md                 # 项目级 Agent 指令，可提交到 Git
├── .codex/
│   ├── config.toml           # 模型、审批策略、沙箱、MCP 等配置
│   ├── rules/                # 命令执行与安全规则
│   │   └── default.rules
│   ├── skills/               # 项目级 Skill，每个 Skill 一个子目录
│   │   └── review/
│   │       ├── SKILL.md
│   │       ├── scripts/
│   │       └── references/
│   ├── agents/               # 自定义子代理配置
│   │   └── reviewer.toml
│   └── mcp/                  # MCP 服务器配置，可选
│       └── servers.toml
├── .agents/
│   └── skills/               # 也可放在这里，方便团队复用
│       └── deploy/
│           └── SKILL.md
```


## 项目级别

1. 在项目根目录中创建 `.agents/skills` 文件夹。
2. 将喜欢的skill整个目录复制到`.agents/skills`下。