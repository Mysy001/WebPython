网页基本结构
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>网站名称</title>
    <meta name="keywords" content="关键词">
    <meta name="description" content="网页描述">
    <link rel="stylesheet" href="">
    <style>
        嵌入样式代码
    </style>
    <script>
            嵌入 JaveScript 代码
    </script>
</head>

<body>
    网站基本内容
</body>

</html>
```

div 标签布局页面代码
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>div 布局</title>

</head>

<body>
    <div class="header"></div>
    <div class="nav"></div>
    <div class="banner"></div>
    <div class="section">
        <div class="news"></div>
        <div class="article"></div>
        <div class="aside"></div>
    </div>
    <div class="footer"></div>
</body>

</html>
```

结构标签
    <div>          用于页面模块划分
    <header>       定义文档的页眉，通常包含一些引导和导航信息
    <nav>          页面导航的链接组
    <section>      用来定义文档中的节
    <article>      特殊的 <section> 标签，代表一个独立的、完整的相关内容块
    <aside>        可以包含在 <article> 标签、整个页面或站点的附属信息部分
    <footer>       用于定义 <section>、<article>或网页的页脚
    <hgroup>       将一系列的标题标签包裹起来
    <figure>       一段独立的内容一般表示文档的一个独立单元
    <figcaption>   为 <figure> 添加描述信息

HTML5 文本标签
    <h1> 到 <h6>     标题标签
    <p>              段落标签
    <span>           行内标签，本身没有任何含义和样式
    <br>             换行

短语标签
    <abbr>           缩写，用于显示文本的缩写，配置 title 属性
    <b>              加粗
    <cite>           引文或参考，文本通常倾斜显示
    <cote>           代码，文本通常使用等宽字体
    <dfn>            术语定义，文本通常倾斜显示
    <em>             强调，文本通常倾斜显示
    <i>              倾斜
    <kbd>            输入文本，用于显示要用户输入的文本，文本通常用等宽字体显示
    <mark>           记号文本，文本高亮显示
    <samp>           示例文本，用于显示程序的示例输出结果，文本通常显示未等宽字体
    <small>          小文本，用小字号显示的免责声明
    <strong>         强调文本，文本通常加粗显示
    <sub>            下标
    <sup>            上标
    <var>            变量文本，用于显示变量或程序的输出结果，文本通常倾斜显示

特殊字符
    "               &quot;
    '               &apos;
    &               &amp;
    <               &it;
    >               &gt;
    ￥              &yen;
    空格            &nbsp;

网页注释
    <!--注释内容-->

CSS注释
    /*注释的内容 */

CSS3 文本属性
    font-family:字体;                         设置文字字体
    font-size:尺寸;                           设置文字大小
    font-style:normal | italic | oblique      设置文字倾斜(显示正常 | 斜体显示 | 倾斜文本)
    font-weight:bold | 100~900;               设置文字粗体
    color:颜色;                                设置文字颜色
    text-align:;                              设置文本水平对齐方式
    text-indent:;                             设置段落首行缩进
    line-height:;                             调整行高
    text-shadow:;                             文本阴影属性
    background-color:;                        背景颜色
    background-image:;                        背景图片
    

