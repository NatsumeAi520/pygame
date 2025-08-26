import pygame as pg

# 初始化pg
pg.init()

# 创建一个窗口
window = pg.display.set_mode((800, 600))

# 设置窗口标题
pg.display.set_caption('hello.pygame')

# 设置窗口颜色
window.fill((227, 227, 227))  # 也可以字符设置

# ///////////在这里放置绘图代码/////////

# 绘制线
pg.draw.line(window, 'red', (50, 50), (150, 150), 5)
pg.draw.aaline(window, 'red', (50, 100), (150, 200), 1)  #用于绘制抗锯齿线

# 绘制多条线
points = [(50, 50), (700, 500), (50, 500)]
# pg.draw.lines(window,'blue',False,points) # true和false决定是否连接第一个点和最后一个点

# 绘制多边形
pg.draw.polygon(window, 'orange', points, 1)

# 绘制矩形
pg.draw.rect(window, 'red', (50, 50, 50, 50), 1, 10)  #一后面的数字用于绘制圆角矩形
pg.draw.rect(window, 'red', (50, 100, 50, 50), 1, -1, 15, 0, 0, 15)  #1后面的数字改为-1可以自己绘制圆角的方位，分别为左上右上左下右下

# 绘制圆
# 正圆
pg.draw.circle(window, 'blue', (400, 300), 50, 1)
pg.draw.circle(window, 'blue', (300, 300), 50, 0, draw_top_left=True)  # 可以决定填充哪个部分

# 椭圆
pg.draw.ellipse(window, 'yellow', (500, 500, 50, 100), 0)

# 绘制弧线


# ///////////////////////////////////

# 更新窗口
pg.display.update()

# 暂停，让我看见窗口
pg.time.wait(50000)

# 清理，退出pg
pg.quit()
