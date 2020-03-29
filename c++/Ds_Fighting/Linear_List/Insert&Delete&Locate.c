// DS_01_linearTable.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#define MaxSize 500
#define InitSize 1000
using namespace std;
typedef struct // static define
{
    int data[MaxSize];
    int length;
}SqList;
typedef struct // dynamic define
{
    int* data;
    int length;
}sqList;
bool ListInsert(SqList& L, int i, int e);
bool ListDelete(SqList& L, int i, int& e);
int LocateElem(SqList& L, int e);
int main()
{
    /*  Dynamic: definition solution：
    sqList L;
    L.data = new int[InitSize];
    L.length = 0;
    */
    // static：
    SqList L;
    L.length = 0;
    int i;
    cout << "operation 1: Insert(0 - 1008), maxsize is 500. So overflow." << endl;
    for (i = 0; i < 1009; ++i) // 固定插入到队头，插入1000个数
        ListInsert(L, 1, i);
    cout << "After insert, L.length is: " << L.length << endl;
    for (i = 0; i < 5; ++i)
        cout << L.data[i] << endl;
    cout << "operation 2: Delete(1 - 100), Notice this is position" << endl;
    int DeleteRecv = -1;
    for (i = 1; i <= 100; ++i) // 固定队头出队，删除100个。
        ListDelete(L, 1, DeleteRecv);
    cout << "After Delete, L.length is: " << L.length << endl;
    cout << "Del : " << DeleteRecv << endl;
    for (i = 0; i < 5; ++i)
        cout << L.data[i] << endl;
    cout << "operation 3: Locate, Notice this is also position" << endl;
    for (i = 399; i > 395; --i)
        cout << i << " is on the position " << LocateElem(L, i) << endl;
    cout << "-1 is on the position " << LocateElem(L, -1) << endl;
    /*
    SqList L;
    cin >> L.data[0] >> L.data[1];
    cout << L.data[0] << endl << L.data[1] << endl;
    cout << L.length << endl;
    */
}
bool ListInsert(SqList& L, int i, int e) // i:位置
{// index : i - 1
    if (i < 1 || i > L.length + 1)
        return false;
    if (L.length >= MaxSize)
        return false;
    for (int j = L.length; j >= i; j--)
        L.data[j] = L.data[j - 1];
    L.data[i - 1] = e;
    L.length++;
    return true;
}
bool ListDelete(SqList& L, int i, int &e)
{ // valid i : [1, L.Length]
  // index : [0, L.Length - 1], i = index + 1;
    if (i < 1 || i > L.length)
        return false;
    e = L.data[i - 1];
    for (int j = i; j < L.length; j++)
        L.data[j - 1] = L.data[j];
    L.length--;
    return true;
}
int LocateElem(SqList& L, int e)
{
    if (L.length == 0)
        return false;
    for (int i = 0; i < L.length; i++)
        if (L.data[i] == e)
            return i + 1;
    return -1; // not found
}
// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧:
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
