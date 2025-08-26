import pygame as pg

# 初始化pg
pg.init()

# 创建一个窗口
window = pg.display.set_mode((800,600))

# 设置窗口标题
pg.display.set_caption('hello.pygame')

# 设置窗口颜色
window.fill((227,227,227)) # 也可以字符设置

# ///////////在这里放置绘图代码/////////




# ///////////////////////////////////

# 更新窗口
pg.display.update()

# 暂停，让我看见窗口
pg.time.wait(5000)

# 清理，退出pg
pg.quit()
