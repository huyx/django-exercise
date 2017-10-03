# 使用 datatables

* http://datatables.net/
* http://cdn.datatables.net/

* [x] datatables 的基本用法
* [x] 布局完成前隐藏表格，布局完成后显示表格
* [ ] 显示界面中文

## 基本用法

```html
<script type="text/javascript" src="jquery.dataTables.js"></script>
<script>
    $(document).ready(function () {
        $('#article_list').dataTable({
            "language": {
                "url": "{% static 'js/jquery.dataTables.Chinese.json' %}"
            },
            "initComplete": function () {
                $('#article_list').css('display', '');
            }
        });
    });
</script>
```

## 常见问题

### 显示问题：加载完 html 以后表格就显示了出来，然后执行 `$(...).dataTable` 之后页面会重新布局，如何改善？

在布局完成之前可以先设置 css 属性：

```html
<table style="display: none">...</table>
```

在布局完成之后重新显示表格：

```javascript
$('#table').dataTable();
$('#table').css('display', '');
```

### 显示问题（续）：指定显示语言为中文以后，又出现了用户可以感知到的布局变化，怎么办？

推测原因：指定了语言插件以后，语言文件的加载是异步的，导致表格的渲染也变成了异步，进而导致这种现象。解决方法是在 `initComplete` 回调函数中显示表格。

参考：

* https://datatables.net/reference/option/initComplete

### jQuery 如何移除 css

想要在布局完成后才显示表格，以避免出现用户可以感受到布局前后界面发生的变化。方法是：

1. 开始时设置表格隐藏： `<table style="display: none;">`
2. 布局完成后移除 display 属性

要移除 display 有两种办法（采用 jQuery）：

```javascript
$('#table').removeAttr('style');           // 把整个 style 移除掉
// 或者
$('#table').css('display', '');            // 移除 display 
```

参考：

* https://devdocs.io/jquery/css
  * Setting the value of a style property to an empty string — e.g. `$( "#mydiv" ).css("color", "")` — removes that property from an element if it has already been directly applied.

注意：`.css( propertyName, value )` 中 value 为 **null** 并不能生效。

### 出现错误 `Uncaught TypeError: Cannot read property 'mData' of undefined`

原因是表格不标准，因为 datatables 要求表格中必须要有 `<thead>` 和 `<tbody>`

参考：

* https://stackoverflow.com/a/25965255/8662909
