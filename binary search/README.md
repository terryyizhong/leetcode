作者：LightGHLi
链接：https://www.zhihu.com/question/36132386/answer/105595067
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

算法的目的是解决问题，下面以针对不下降序列a的4个问题为例，给出我认为效率较高，较为简洁的代码。
对于不下降序列a，n为序列a元素的个数，key为关键字：

<p>
	<br />
1.求最小的i，使得a[i] = key，若不存在，则返回-1<br />
int binary_search_1(int a[], int n, int key)<br />
{<br />
&nbsp; &nbsp; int m, l = 0, r = n - 1;//闭区间[0, n - 1]<br />
&nbsp; &nbsp; while (l &lt; r)<br />
&nbsp; &nbsp; {<br />
&nbsp; &nbsp; &nbsp; &nbsp; m = l + ((r - l) &gt;&gt; 1);//向下取整<br />
&nbsp; &nbsp; &nbsp; &nbsp; if (a[m] &lt; key) l = m + 1;<br />
&nbsp; &nbsp; &nbsp; &nbsp; else r = m;<br />
&nbsp; &nbsp; }<br />
&nbsp; &nbsp; if (a[r] == key) return r;<br />
&nbsp; &nbsp; return -1;<br />
}<br />
2.求最大的i，使得a[i] = key，若不存在，则返回-1<br />
int binary_search_2(int a[], int n, int key)<br />
{<br />
&nbsp; &nbsp; int m, l = 0, r = n - 1;//闭区间[0, n - 1]<br />
&nbsp; &nbsp; while (l &lt; r)<br />
&nbsp; &nbsp; {<br />
&nbsp; &nbsp; &nbsp; &nbsp; m = l + ((r + 1 - l) &gt;&gt; 1);//向上取整<br />
&nbsp; &nbsp; &nbsp; &nbsp; if (a[m] &lt;= key) l = m;<br />
&nbsp; &nbsp; &nbsp; &nbsp; else r = m - 1;<br />
&nbsp; &nbsp; }<br />
&nbsp; &nbsp; if (a[l] == key) return l;<br />
&nbsp; &nbsp; return -1;<br />
}<br />
3.求最小的i，使得a[i] &gt; key，若不存在，则返回-1<br />
int binary_search_3(int a[], int n, int key)<br />
{<br />
&nbsp; &nbsp; int m, l = 0, r = n - 1;//闭区间[0, n - 1]<br />
&nbsp; &nbsp; while (l &lt; r)<br />
&nbsp; &nbsp; {<br />
&nbsp; &nbsp; &nbsp; &nbsp; m = l + ((r - l) &gt;&gt; 1);//向下取整<br />
&nbsp; &nbsp; &nbsp; &nbsp; if (a[m] &lt;= key) l = m + 1;<br />
&nbsp; &nbsp; &nbsp; &nbsp; else r = m;<br />
&nbsp; &nbsp; }<br />
&nbsp; &nbsp; if (a[r] &gt; key) return r;<br />
&nbsp; &nbsp; return -1;<br />
}<br />
4.求最大的i，使得a[i] &lt; key，若不存在，则返回-1<br />
int binary_search_4(int a[], int n, int key)<br />
{<br />
&nbsp; &nbsp; int m, l = 0, r = n - 1;//闭区间[0, n - 1]<br />
&nbsp; &nbsp; while (l &lt; r)<br />
&nbsp; &nbsp; {<br />
&nbsp; &nbsp; &nbsp; &nbsp; m = l + ((r + 1 - l) &gt;&gt; 1);//向上取整<br />
&nbsp; &nbsp; &nbsp; &nbsp; if (a[m] &lt; key) l = m;<br />
&nbsp; &nbsp; &nbsp; &nbsp; else r = m - 1;<br />
&nbsp; &nbsp; }<br />
&nbsp; &nbsp; if (a[l] &lt; key) return l;<br />
&nbsp; &nbsp; return -1;<br />
}<br />
实际上，对于3、4，也可以先判断解是否存在，再进行二分查找。
</p>
<p>
	<br />
</p>
