float 属性(浮动)
    float: left | right | none | inherit(从父标签继承 float 属性的值) ;

clear 属性(清除浮动)
    clear: left | right | both | none |inherit(从父标签继承 clear 属性的值);

清除浮动——为浮动的父类增加一个类 .clearfix 
```javascript
.clearfix:after{
    content:"";       /* after 是一个伪类，必须加 content 属性*/
    display:block;    /* after 是一个行内标签，虚转换成块级标签*/
    clear:both;       /* 清除浮动*/
    height:0;         /* 高度为0*/
    cverflow:hidden;  /* 超出部分隐藏*/
}
```