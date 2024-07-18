卷积常见参数关系
输出大小 = (n + 2p - f) / s + 1
其中：n 是输入大小，p 是 padding，f 是 filter size，s 是 stride（步长）

padding:
如果想让输出大小与输入大小相同，可以设置:
p = (f - 1) / 2 （当 stride = 1 时） 
