相对定位(标签相对自己自标准流的位置，以左上角为起点，进行垂直或水平方向的偏移)
    position:relative;
    top:20px;
    left:30px;

绝对定位(参照已定位的父级/主父级/body标签的最左上角来定义)
    position:absolute;
    top:20px;
    left:30px;

层级(用来设置标签的堆叠顺序，仅对定位标签有效)
    z-index:数值;

CSS3的过渡动画
    变换的属性名称(单独指定标签的哪些属性改变时执行过渡)
        transition-property:none | all | 任意标签属性;
    过渡持续时间(单位为 秒或毫秒)
        transition-duration:持续时间;
    过渡速率变化(逐渐变慢、加速然后减速、匀速、加速、减速)
        transition-timing-function:ease | ease-in-out | linear | ease-in | ease-out;

CSS3的2D变形
    位移函数
        transform:translate(x,y);
    缩放函数(标签根据中心原点进行缩放，默认值为1)
        transform:scale(x,y);
    旋转函数(设定的角度使标签根据原点进行旋转)
        transform:rotate(deg);
    倾斜函数
        transform:skew(x,y);
    变形原点(中心位置,默认位置是50% 50%)
        transform-origin:left bottom | 0% 100%;

CSS3的3D变形
    3D位移
        transform:translate3d(x,y,z);