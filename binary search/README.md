作者：LightGHLi
链接：https://www.zhihu.com/question/36132386/answer/105595067
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

算法的目的是解决问题，下面以针对不下降序列a的4个问题为例，给出我认为效率较高，较为简洁的代码。
对于不下降序列a，n为序列a元素的个数，key为关键字：

1.求最小的i，使得a[i] = key，若不存在，则返回-1
int binary_search_1(int a[], int n, int key)
{
    int m, l = 0, r = n - 1;//闭区间[0, n - 1]
    while (l < r)
    {
        m = l + ((r - l) >> 1);//向下取整
        if (a[m] < key) l = m + 1;
        else r = m;
    }
    if (a[r] == key) return r;
    return -1;
}
2.求最大的i，使得a[i] = key，若不存在，则返回-1
int binary_search_2(int a[], int n, int key)
{
    int m, l = 0, r = n - 1;//闭区间[0, n - 1]
    while (l < r)
    {
        m = l + ((r + 1 - l) >> 1);//向上取整
        if (a[m] <= key) l = m;
        else r = m - 1;
    }
    if (a[l] == key) return l;
    return -1;
}
3.求最小的i，使得a[i] > key，若不存在，则返回-1int binary_search_3(int a[], int n, int key)
{
    int m, l = 0, r = n - 1;//闭区间[0, n - 1]
    while (l < r)
    {
        m = l + ((r - l) >> 1);//向下取整
        if (a[m] <= key) l = m + 1;
        else r = m;
    }
    if (a[r] > key) return r;
    return -1;
}
4.求最大的i，使得a[i] < key，若不存在，则返回-1int binary_search_4(int a[], int n, int key)
{
    int m, l = 0, r = n - 1;//闭区间[0, n - 1]
    while (l < r)
    {
        m = l + ((r + 1 - l) >> 1);//向上取整
        if (a[m] < key) l = m;
        else r = m - 1;
    }
    if (a[l] < key) return l;
    return -1;
}
实际上，对于3、4，也可以先判断解是否存在，再进行二分查找。
