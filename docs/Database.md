基于 Uni-app + Supabase（底层为 PostgreSQL）的技术栈，并结合 MVP 阶段的核心需求（合唱团管理、权限隔离、云端简谱发布、实时拉取），我为您设计了以下 4 张核心业务数据表。

在 Supabase 架构中，由于其原生自带 auth.users 表处理手机号/微信登录授权，我们的业务表将基于该授权表进行扩展。

1. 用户信息扩展表 (profiles)
存储团员或队长的基础个人信息。

字段名	数据类型	主外键/约束	描述
id	uuid	主键 (关联 auth.users.id)	用户全局唯一ID，与系统认证表绑定
avatar_url	text	可空	用户微信头像链接
nickname	varchar(50)	非空	用户昵称或真实姓名
created_at	timestamptz	默认 now()	账号注册时间
2. 合唱团信息表 (choirs)
用于定义和管理“合唱团”这个核心组织容器。

字段名	数据类型	主外键/约束	描述
id	uuid	主键	合唱团全局唯一ID
name	varchar(100)	非空	合唱团名称
invite_code	varchar(20)	唯一约束 (Unique)	用于微信群分享裂变的加团邀请码
owner_id	uuid	外键 (关联 profiles.id)	创建者（总队长）的ID
created_at	timestamptz	默认 now()	合唱团创建时间
3. 合唱团成员关联表 (choir_members)
解决“谁在哪个合唱团、是什么身份、唱哪个声部”的 RBAC（基于角色的访问控制）问题。

字段名	数据类型	主外键/约束	描述
id	uuid	主键	关系记录唯一ID
choir_id	uuid	外键 (关联 choirs.id)	所属合唱团ID
user_id	uuid	外键 (关联 profiles.id)	团员的用户ID
role	varchar(20)	非空，默认 'member'	角色权限枚举：'admin' (队长), 'member' (普通团员)
voice_part	varchar(20)	可空	团员所属声部枚举：'Soprano', 'Alto', 'Tenor', 'Bass' 等
joined_at	timestamptz	默认 now()	加入合唱团的时间
设计约束补充：需在 choir_id 和 user_id 上建立 联合唯一索引 (Unique Index) ，确保一个用户在一个合唱团中只有一条身份记录。

4. 云端简谱主数据表 (scores)
这是 MVP 的核心资产表，摒弃传统的 PDF 文件存储，转而使用 JSON 格式存储乐谱的结构化数据。

字段名	数据类型	主外键/约束	描述
id	uuid	主键	曲谱唯一ID
choir_id	uuid	外键 (关联 choirs.id)	该曲谱所属的合唱团
title	varchar(200)	非空	歌曲名称
bpm	integer	默认 120	全局默认播放速度（节拍/分钟）
base_key	varchar(10)	默认 '1=C'	全局默认调号
score_data	jsonb	非空	核心字段 ：以 JSONB 格式存储的所有声部音符、歌词、时值及排版数据
last_updated_by	uuid	外键 (关联 profiles.id)	最后修改该曲谱的队长ID
updated_at	timestamptz	默认 now()	最后更新时间，用于触发客户端同步
产品与技术设计理由说明：
为什么采用 jsonb 存储简谱数据 (score_data)？

性能与传输 ：传统关系型数据库如果把每个音符存成一行数据，一首歌会产生数千条记录，查询极慢。PostgreSQL（Supabase 的底层）对 jsonb 有着极其强悍的原生支持。将整首歌的数字简谱结构（JSON Schema）作为一个 JSON 对象存储，客户端只需一次 API 请求即可拉取完整对象。

实时协同就绪 ：队长在编辑器里修改了某一个小节，前端将最新的 JSON 数据保存到 score_data 字段。Supabase 的 Realtime Broadcast 服务监听到该行记录 updated_at 的变化后，可以通过 WebSocket 瞬间将新的 JSON 对象推送到所有在线团员的设备上，实现秒级同步。

基于 Row Level Security (RLS) 的天然安全隔离

采用 Supabase 的核心优势是你可以直接在数据库层写安全策略（RLS）。

例如，针对 scores 表，我们可以直接配置策略：“只有 choir_members 表中对应 choir_id 且 role 为 'admin' 的用户，才能执行 UPDATE / DELETE 操作”；“ role 为 'member' 的用户只能执行 SELECT 操作”。这让你在无需编写任何后端 API 接口的情况下，完美实现了坚如磐石的权限隔离。

针对微信裂变的 invite_code

choirs 表中的 invite_code 配合微信小程序的 shareMiniProgram 接口，可以直接生成带参数的卡片分享到微信群。团员点击卡片后，前端读取参数并自动向 choir_members 写入一条 role='member' 的记录，极大缩短了用户的加团路径。