.col-xs- 超小屏幕 手机 (<768px)

.col-sm- 小屏幕 平板 (≥768px)

.col-md- 中等屏幕 桌面显示器 (≥992px)

.col-lg- 大屏幕 大桌面显示器 (≥1200px)
################################################
引用bootstrap必须要做的事：
1.将下载好的bootstrap和jquery放入项目中。
2.在一个要引用的html中，写这么几句话
    1.在head标签中写：
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <link rel="stylesheet" href="css/bootstrap.min.css"/>
    2.在body中写：
        <script src="js/jQuery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>

就算开启了调试模式，改过代码以后，想看效果，最好重新加载项目

遇到了一个非常不可思议的问题，新建的html，继承base.html都是可以引用bootstrap的样式的，但是一旦将详细话题的
程序复制到该页面，该页面马上就不能链接到bootstrap的样式了，就变成了纯文本了。




关于项目：
    1.自定义的样式文件都在css/myself.css中。
