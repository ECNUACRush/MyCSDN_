# 					  CPP LEARNING NOTES

#### 定义字符数组：用char和string  分别定义如下形式的：

`//char *Day[] = {"MON","TUE","WED","THU","FRI","SAT","SUN"};
	string Day[] = {"MON","TUE","WED","THU","FRI","SAT","SUN"}`

`string Day[7] = {"MON","TUE","WED","THU","FRI","SAT","SUN"};`;`

那么使用的时候，可以直接用Day[0]来替代“MON”。



#### 字符串数组使用注意：

如上所示，我们显然可以观察到字符串数组和字符串的区别：

两者的定义如下：

```c++
string s1 = "";
string s1[可选] = {"ab","cd","ef","gh","ij"};
```

这里对比很明显，字符串数组无论是否注明其容量，都应该加上[]，表示这是多个字符串组成的字符串数组。

那么现在有这样一个问题：如果我们试图取到‘a’或者‘c’这样的每个字符数组的一个元素，该如何取呢？

显然这样的代码是ojbk的：

```c++
string temp;//工具人字符串
string ans;// answer string
string s1[5] = {"ab","cd","ef","gh","ij"};
for(int i = 0; i < 5; ++i)
	temp = s1[i],
	ans += temp[0];

```

这样的优点是easy，但是多引入了工具人字符串导致空间浪费，操作也略显繁琐。不妨优化如下：

```c++
string ans;// answer string
string s1[5] = {"ab","cd","ef","gh","ij"};
for(int i = 0; i < 5; ++i)
	ans += s1[i][0];
```

非常简洁，这样其实是把s1当成一个二维数组来看，第一维对应的是字符串的序号，第二维是每个字符串中对应的位置。

#### 关于字符数组以及memset，memcpy，'\0'的理解。

[字符串替换](https://acm.ecnu.edu.cn/problem/3445/)：题目来源于2017.11程序设计基础月考。

说来惭愧，两年半前的题目现在自己做来都有一些不易；But must believe that it's never too late to learn。只要有收获就是好的！加油。

##### 题目描述：

###### 样例

Input

```
iamstupid stupid clever
```

Output

```
iamclever
```

##### 分析：

此题由于给好了函数模板，函数头如下：`void replace(char s[], char x[], char y[])`

其中s，x，y分别是原串，目标串，替换后的串。

在replace函数内试图对s直接进行替换是非常难的：

1. 首先要对s进行遍历，找到替换位置。
2. 找到要替换的位置后，分三种情况替换：
   - 同样长度，直接替换即可。
   - y比x长，那么y要占用一部分s的其他位置，相应的，所有后面的字符需要先依次后移若干位。
   - x比y长，那么替换后会出现空的位置，要将后面的所有字符依次前移若干位。
3. 不难发现，这样会非常非常非常麻烦。即使是一个数据结构老手，也不愿选择这样的笨方法。即便你成功的进行了替换+移位+替换+……。就成功了吗？并没有，替换后的串影响了长度，首先导致外圈的遍历循环不准确。

所以我们选择引入一个char temp[3 * N + 1]，其空间是与s保持一致的。其实这里题目做了一个保证：经过若干次替换以后，s的长度也没有超过上限。不过想了想，反正最后是要用s的范围去输出的，既然已经给定了最大的s，那么我们定义同大小的temp也没有问题。

1. 有temp之后就简单了很多。同样遍历s，每一个i都进行一轮嵌套循环，判断接下来n个字符是否组成了x，如果组成了：那么就temp += y，i += strlen（x）即可。如果没有组成，那么就temp += s[i]。思路还是非常之简单的。

2. 在最后复制的时候有很大名堂：

   ```c++
   Case1：
   memset(temp,0,N*3+1);
   memset(s, 0, N*3+1);
   memcpy(s, temp, k);
   Case2：
   s[k] = '\0';
   ```

   case1和case2在效果上完全一致。

   Case1：`memcpy(s, temp, k);` 这个函数在目标区域没有值的时候会很好的起作用，而如果目标区域已经occupied，那么会从前开始进行替换。那么我们显然不希望temp比s短的时候，最后temp后面接上了原来s的部分。所以必须要先使用 `memset(temp,0,N*3+1);memset(s, 0, N*3+1);`  ，这两步都是必须的，第一个memset是为了保证temp里面不会出现奇怪的字符。

   Case2：驾轻就熟的用法。其实temp的前半部分是我们自己加进去的，所以当然可以保证没有问题，那么memcpy又必然能成功的将其复制到s的前半部分，那么我们直接给s[k] = '\0'，强行结束字符串，使得后面的部分被截断即可。

   ​         

#### isalpha()语法:

头文件：#include <ctype.h>

函数原型： int isalpha( int ch ); 
功能：如果参数是字母字符，函数返回非零值，否则返回零值。

`char c; scanf( "%c", &c ); if( isalpha(c) ) printf( "You entered a letter of the alphabet\n" );`

 isdigit(int c)宏 ：

头文件：#include <ctype.h>

定义函数：int isdigit(int c);

函数说明：检查参数 c 是否为阿拉伯数字0 到9。

返回值：若参数c 为阿拉伯数字，则返回true，否则返回null(0)。

附加说明：此为宏定义，非真正函数。

#### string和char的一些问题：

https://www.nowcoder.com/pat/6/problem/4044 一道题。

```c++
char s1[105],s2[105];
//char ans_s1[105],ans_s2[105];
string ans_s1="",ans_s2="";
else if(s1[i] == 'B' && s2[i] == 'C')cnt1++,ans_s1 += s1[i];
```

注意以上，定义两个char数组。s1[105]，是可以对其中的单个字符进行比对的，直接用“==”进行比较即可，但是不可以用字符串的“+=”来操作字符数组。

这里我的原来意思是：先输入一个整数N，然后类似于行，每次输入两个字符分别到两个字符串里，但是报错：段错误（segmentation fault），可见字符串的输入和字符数组还是有一定区别。那么建议以后这种分段、分批次输入时候还是以字符数组为准。

#### scanf和cin输入的一点问题：

在c++中频繁使用cin进行输入。但是scanf也有其特有之处。

首先：scanf/printf的效率高于cin/cout

此外，不妨看以下输入格式：

##### **输入例子:**

```
5 
John 2001/05/12
Tom 1814/09/06
Ann 2121/01/30
James 1814/09/05
Steve 1967/11/20
```

这里显然想到人名用string来存，方便操作。而后面的部分，如果用字符串进行存储，会比较麻烦。麻烦来自于以下几方面: 首先，字符串中不易于比大小等等，不方便操作。其次，把字符转变为数字也是很麻烦的过程。最后，此处长度固定，但不排除各部分长度不固定的情况。综上所述我们希望分部分提取到int类型变量中，那么这里存在问题：如果用cin读入，如：

`int i = 0;
    cin >> s[i].year >> s[i].month >> s[i].day;
    cout << s[0].year << endl << s[0].month << endl << s[0].day;
    return 0;`

经过测试，除了第一个数可以被正确读入之外，别的两个变量都被保存成了0，而这显然不是我们需要的。

所以容易想到以下写法：

`scanf("%d/%d/%d",&s[i].year,&s[i].month,&s[i].day);
    cout << s[0].year << endl << s[0].month << endl << s[0].day;`

经过测试，这样的代码是可以正确读入的！

总结：在用空格（' '）或者换行符（'\n'）进行分割输入的时候，我们用cin即可。而如果是其他各种各样的符号进行的分割，那么显然该使用scanf。

#### string ：insert函数的一些用法：

我们知道，如果对一个字符串做操作，常用的方法有用‘+’‘-’运算符。也可以用其他的操作函数，今天来介绍一个insert：

包含在头函数：#include<iostream>中

void insert（int pos，string）

function：在pos之前进行插入string值。

note：注意由于第二个类型是string，也即插入的只能是“xxx”内容，所以即使是单个字符‘x’，也必须写成“x”才能进行插入。

`string a = "abcdefghi";
    a.insert(1,"hellao");
    cout << a;`

//answer：ahellaobcdefghi

#### 关于四舍五入处理，以及double类型输出：

题干描述如下：

<!--**输入描述:**

```
输入在一行中顺序给出2个整数C1和C1。注意两次获得的时钟打点数肯定不相同，即C1 < C2，并且取值在[0, 107]
```

##### **输出描述:**

```
在一行中输出被测函数运行的时间。运行时间必须按照“hh:mm:ss”（即2位的“时:分:秒”）格式输出；不足1秒的时间四舍五入到秒。
```

##### **输入例子:**

```
123 4577973
```

##### **输出例子:**

```
12:42:59
```

-->

我的代码如下：

`int main(){
    double C1,C2;
    int gap;
    scanf("%lf%lf",&C1,&C2);//lf
    gap = (C2 - C1) / 100 + 0.5;
    printf("%02d:%02d:%02d",gap / 3600, gap % 3600 / 60, gap % 60);
	return 0;
}`

注意到以下几点：

1：取出小时，分钟，秒数，分别用gap / 3600，gap % 3600 /60，以及gap % 60.我们首先明白，对于“%”符，必须用int类型操作，double是没有这样的运算符的（除非进行重载）。那么gap必然是int类型的，显然用（C2-C1）/100可以得到秒数，但这里的秒数可能会被忽略小数点后的位数，题干中要求四舍五入，所以我们选择定义double类型的c2和c1，在给其+0.5，用int类型的gap进行强制类型转换，即可达成目的；深度思考：如果是需要无条件舍去，那么可以定义int类型的c1和c2。

2：输出！！！由于每一位可能都不足2位，即会出现9：9：32这样的输出，显然是不合规范的，那么按照我们既定的规则，应该输出09：09：32，即要用%02d进行补全位数，这样的操作经常被我忘记，反省！

3：关于double和float在scanf和print里面的一些note：我之前是不太清楚的，这次借用了以下代码进行调试：`double a,b;
    scanf("%lf%lf",&a,&b);
    printf("%lf  %lf\n",a,b);
    //printf("%f%f",&c,&d);
	return 0;`

得出结论：对于double 和 float，虽然我们一般建议只用double，但是float有时也会使用。

1：无论使用哪一个，对应的区别只在于scanf，当用double，scanf必用%lf进行占位，用float则必用%f，不然会报错。

2：对于printf，使用%f和%lf目前没发现大的区别。

3：建议全用double，双精度，那么scanf直接全用%lf，printf也全用%lf，这是我目前认为最为保守的方法。



### 大数加法&减法&乘法&除法

#### 	大数加法：the first step

首先是最简单的部分。

### 进制转换问题（A到B进制转换）

`string s = "0123456789abcdefghijklmnopqrstuvwxyz";`

<!--1：这里实现的是10进制到D进制的转换，D的范围是基于s里面的字符数的，我们的ep中有36个元素，那么最大可以转换到36进制，经过测试没有问题，2：之后再去分析R进制到D进制（情况2）以及转到非常高的进制（如2333，情况3）。 -->

`int main(){
    int A,B,D,add,i=0;
    int a[MAXN] = {0};
    cin >> A >> B >> D;
    add = A + B;
    while(add / D)//提前结束一轮，所以最后i的值也不用减，很完美
        a[i++] = add % D, add /= D;
    a[i] = add;
    while(i >= 0)
        cout << s[a[i--]];
	return 0;
}`

### 数据结构part

#### 链表：

最常见的数据结构当然是链表，所以不妨我们先来学习一下。





### STL Learning

#### Intro:

Standard Template Library：标准模板库。

##### 优势：

C++ STL的优势：提供了多种方便的容器，并且封装了复杂的数据结构算法&数据结构操作：vector封装数组，list封装链表，map和set封装二叉树。

此外这些封装以成员函数的方式提供常用操作：插入、排序、删除、查找等。

##### Set

set--关联式容器。set作为一个容器也是用来存储同一数据类型的数据类型，并且能从一个数据集合中取出数据，在set中每个元素的值都唯一，而且系统能根据元素的值自动进行排序。应该注意的是set中数元素的值不能直接被改变。C++ STL中标准关联容器set, multiset, map,  multimap内部采用的就是一种非常高效的平衡检索二叉树：红黑树，也成为RB树(Red-Black  Tree)。RB树的统计性能要好于一般平衡二叉树，所以被STL选择作为了关联容器的内部结构。

###### 特点：

1. Set中元素自动排好序（sorted）
2. Set中无重复元素
3. Set封装的是红黑树，非常高效的平衡二叉树。

###### 具体效率：

以查找为例，Set查找2个元素要1次，4个2次，8个3次，即log2（n）次。对数级别的效率。1024 - 10次，10000也仅仅需要14次。故效率非常之高。

###### 常见成员函数：

- begin()		  返回第一个元素的迭代器

- end()             返回最后一个元素的迭代器

- clear()           删除set容器里面的所有元素

- empty()        判断set容器是否为空

- max_size()   返回set容器可能包含的元素的最大个数

- size()             返回当前set容器的元素个数

- rbegin()        返回最后一个元素的迭代器 

- rend()           返回第一个元素的迭代器

- count()         返回元素的个数（1或者0）

  <!--经过我的测试，rbegin和begin 分别是两个方向的趋势，一定都是开始，即使我们用迭代器it，it也只能++，然后正向的结尾一定是end，逆向则是rend-->

------

###### 示例程序：

Note：要使用set模板，必先包含<set>头函数。

> 以下代码引用自https://blog.csdn.net/byn12345/article/details/79523516
>
> [2020/2/11]: https://blog.csdn.net/byn12345/article/details/79523516	"C++中set用法详解"

基本使用：

```c++
#include <iostream>
#include <set>
//typedef long long ll;
#define ll long long
using namespace std;

int main(){
     set<ll> s;
     s.insert(1);
     s.insert(2);
     s.insert(3);
     s.insert(1);
     cout<<"set 的 size 值为 ："<<s.size()<<endl;
     cout<<"set 的 maxsize的值为 ："<<s.max_size()<<endl;
     cout<<"set 中的第一个元素是 ："<<*s.begin()<<endl;
     cout<<"set 中的最后一个元素是:"<<*s.end()<<endl;
     s.clear();
     if(s.empty())
     {
         cout<<"set 为空 ！！！"<<endl;
     }
     cout<<"set 的 size 值为 ："<<s.size()<<endl;
     cout<<"set 的 maxsize的值为 ："<<s.max_size()<<endl;
     return 0;
}

```

<!--经过测试，用set集成int和longlong都没有问题，集成string和char类型时有点小问题，另外一定要记得多使用begin和end。使用前面要加*符。此外，可能因为ll每个数字更占空间，max_size()集成的最大元素个数明显少于int。-->

使用迭代器进行迭代遍历：

```c++
int main(){
     set <ll> s;
     for(int i = 0; i < 10; i += 2)
        s.insert(i);
     set <ll> ::iterator it;
    //set <ll> ::iterator i;
    //auto it = s.begin();
     for(it = s.begin(); it != s.end(); ++it)
        //if(*it >= 5)
            printf("%d\n",*it);
     for(auto i = s.rbegin(); i != s.rend(); ++i)
         printf("%d\n",*it);
     while(it != s.end())
         cout << *it++ << endl;
     for(auto it : f)
         cout << it << endl;
    /*
    注：用for做范围循环时候，不用指针，也不用it++的操作，直接定义迭代器然后 i ： f即可。
    但是不难发现，这样很难做精准控制。比如我们期望的输出是 1 2 3 4 5然后换行，最后一个数据
    后面不要加' '。那么这样的话，用for范围循环是难以控制的，需要使用迭代器进行操作。
    */
     return 0;
}
```

```cpp

/*
    NO.1
    Set重构
    sort 是不能用来直接对 set进行排序的。
*/
//排序题 EOJ 2975
//要求：按个位大小升序排，相同则按本身大小升序排
#include<bits/stdc++.h>
using namespace std;
struct cmp{
	bool operator()(const int&i1, const int&i2)
	const {
		if (i1 % 10 == i2 % 10)
			return i1 < i2;
		return i1 % 10 < i2 % 10;
	}
};
int main() {
	int t, n, tmp; cin >> t;
	for (int q = 0; q < t; q++) {
		cin >> n;
		set<int, cmp>f;
		while (n--) 
			cin >> tmp, f.insert(tmp);
		printf("case #%d:\n", q);
        for(auto i : f)
            cout << i << ' ';
        cout << endl;
	}
}
```



##### Stack

###### 一些特点：

话不多说直接上代码进行测试：

```C++
#include <iostream>
#include <stack>
using namespace std;
int main() {
  stack<int> check;
  //cout << check.top() << endl;
  for(int i = 10; i < 20; ++i)
    {   
        // cout << " 1 check.top() is " << check.top() << endl; 出错，第一个元素调用不了top()
        check.push(i);
        cout << " 1 check.top() is " << check.top() << endl;
    }
  for(int i = 0; i < 10; ++i)
    {
        cout << " 2 check.top() is " << check.top() << endl;
        check.pop();
      //cout << " 2 check.top() is " << check.top() << endl; 仍然出错，最后一个元素已经NULL了
    }
    if(check.empty())
        cout << "mission complete";
  return 0;
}
//输出：
 1 check.top() is 10
 1 check.top() is 11
 1 check.top() is 12
 1 check.top() is 13
 1 check.top() is 14
 1 check.top() is 15
 1 check.top() is 16
 1 check.top() is 17
 1 check.top() is 18
 1 check.top() is 19
 2 check.top() is 19
 2 check.top() is 18
 2 check.top() is 17
 2 check.top() is 16
 2 check.top() is 15
 2 check.top() is 14
 2 check.top() is 13
 2 check.top() is 12
 2 check.top() is 11
 2 check.top() is 10
mission complete
```

总结：栈顶指针一定是指向元素的。所以如果为空栈时候，绝对不能调用stack.top()，会出现段错误或是内存错误。



###### 常见成员函数：

![image-20200215104857802](C:\Users\wwwxi\AppData\Roaming\Typora\typora-user-images\image-20200215104857802.png)

###### 实例程序：

```c++
#include <cstdio>
#include <iostream>
#include <stack>
#include <string>
using namespace std;
bool match(char a, char b) {
  if ((a == '[' && b == ']') || (a == '{' && b == '}') ||
      (a == '(' && b == ')'))
    return true;
  return false;
}
int main() {
  stack<int> check;
  string Stack;
  getline(cin, Stack);
  int length = Stack.size(), i = 0;
  while (i < length) {
    if (Stack[i] == '[' || Stack[i] == '{' || Stack[i] == '(') {
      check.push(Stack[i]);
    } else {
      if(check.empty()){
        break;
      }
      else if (match(check.top(), Stack[i]))
        check.pop();
      else
        break;
    }
    i++;
  }
  if (i == length) // null : return true   not null: return false
    cout << "YES";
  else
    cout << "NO";
  return 0;
}

```



### 文件操作

#### Freopen用来读&写

需要的头函数为<cstdio>

使用freopen以后，则不用再从命令行读入，而是相当于把命令行的数据提前存到了文件里，再进行读文件写文件了。

```c++
  freopen("D:\\test2\\pipei34.in","r",stdin);
  freopen("D:\\test2\\pipei344.txt","w",stdout);
  getline(cin, string_name);
  //cin >> a >> b;
  ……
  fclose(stdin);
  fclose(stdout);
```

> r 打开只读文件，该文件必须存在。
> r+ 打开可读写的文件，该文件必须存在。
> w 打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件。
> w+ 打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。
> a 以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。
> a+ 以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 



### 排序

#### 桶排序：

优点：速度快，简单。

缺点：浪费空间，适用性不够广泛，只能处理数据（不能体现附加的属性等）。

闲话不多说，贴上代码：

```c++
void box_sort(int a[MAXN])
{
    int num;
    int t;
    cin >> num;
    while(num--)
    {
        cin >> t;
        a[t] ++;
    }
    for(int i = 0; i < MAXN; ++i)
        if(a[i])
            cout << i << ' ';
}
```



#### 冒泡排序：

名字最美丽的排序：bubbleSort

优点：简单，代码短且优美

缺点：时间复杂度高 O（n²）

```c++
void bubble_sort(int a[MAXN])
{
    for(int i = 0; i < MAXN - 1; ++i)
        for(int j = 0; j < MAXN - 1 - i; ++j)
            if(a[j] > a[j + 1]) // descent descend ascent ascend 
                //特点： 若想升序排，则：> 
                //降序则：<
                swap(a[j], a[j + 1]);
}
```



#### 快速排序：

最常见&最常用的排序。由C.A.R.Hoare于1962发表在Computer Journal上。

优点：效率高，时间复杂度 O(nlogn)级别。

缺点：相比于前两种较复杂，但依旧非常基础；如果原来是有序数列，那么最差的时间复杂度为O(n²)。

```c++
void quick_sort(int left, int right)
{
    if(left > right)
        return ;
    int temp = a[left];
    int i = left, j = right;
    while(i != j)
    {
        while(a[j] >= temp && j > i)
            j--;
        while(a[i] <= temp && i < j)
            i++;
        if(i < j)
        {
            swap(a[i], a[j]);
        }
    }
    a[left] = a[i];
    a[i] = temp;
    quick_sort(left, i - 1);
    quick_sort(i + 1, right);
    return ;
}
```

#### String：sort()方法排序的一些参考

我们之前知道sort可用来对string数组进行排序，实质上是对多个string进行排序。伪代码如下：

```cpp
bool cmp(string aa, string bb)
{/* sort function.

}*/
int main()
{	
    string ss[100];
    sort(s, s+100, cmp);
    return 0;
}
```

但是之前对一个单个字符串进行排序没有用过。考虑用迭代器。伪代码如下：

```cpp
bool cmp(char a, char b)
{/* sort function.

}*/
int main()
{	
    string s;
    char ss[100];
    sort(s.begin(), s.end(), cmp);
    qsort(s, strlen(ss), sizeof(ss[0]), cmp);
    return 0;
}  
```

#### Sort()与Qsort()的对比：

性能上，我们的性能测试就在下面，结论是普通的qsort大于sort。

cmp函数中，除了返回值不同以外。比较规则也刚好相反，比如我们试图降序排一个数组，那么sort的cmp中应该写x > y（注意x是前参，y是后参）。而qsort中则刚好相反的写成y > x。（但不能这么写，一定要写成y - x) 

bool类型，如果对于sort中你写成了一个减式如：y-x，细想逻辑：只有两者相等时候返回false，否则无论正负都是true显然不符合。

同样的对于int的qsort，如果你写成比较式，y > x，诚然，当y大于x的时候是会返回1，但是y < x或者y = x的时候都会返回0。就少了原来的负数。

#### 关于Qsort引发对于指针的一些理解：

```cpp
int cmp(const void *a, const void*b)
{
    int x = *(int *)a;
    int y = *(int *)b;
    return y - x;
}
int cmp(const void *a, const void*b)
{
    int* x = (int* )a;
    int* y = (int* )b;
    return *y - *x;
}
以上两种写法等价，都是进行数组的降序排序。
我们简单看一下：
(int* )a  （int*）是针对a这种无类型的指针，所以必须打括号。 这里实际上操作的还是a，最后a是地址。
这时候如果我想直接比，就用Plan1即可，再用*解引用，取出a里面的值放在x中，进行比较即可。
而如果用Plan2，int* x 这样实际上是用x来接收后面的地址，那么为了比较值仍然需要用*y和*x来解引用
    
再看一组结构体排序的实例：
typedef struct
{
    long long str;//数字本身（因为一开始想用字符串做失败了，然后中途改的，所以str和ch没有换成别的变量名）
    long long int ch;//首位数字
}number;

int cmp(const void *a, const void*b)
{   
    number* x=(number* )a;
    number* y=(number* )b;
    return (x->ch==y->ch)?(x->str>y->str):y->ch-x->ch;
}
同样是一模一样的赋值法：先解决空指针。然后x，y仍然是地址。地址的话就要用->了。
```



#### C++/JAVA 与 Python在浮点数 取余方面的小心机

总结起来其实也很简单：python尽可能让商更大，cpp和java则相反，尽可能使他小。所以看起来python的余数始终是介于0和除数之间的，符合我们数学上的逻辑。而cpp和java由于特殊的取余机制。会导致这一点不复存在。

此外还有一点：根据严格定义，小数是不可以做余数的。因为如果这样的话，我们大可以除尽。没必要留出小数了。但是在python中这是有的。比如5 % 2.3 = 0.4000000000036（浮点数误差）。

#### 性能测试：

```c++
/*
* 文件名：Sort_efficiency_test.cpp
* 版权：Copyright 2000-2001 Huawei Tech. Co. Ltd.  All Rights Reserved.
* 描述： 各种排序性能测试
* 修改人：EcnuAcRUSH
* 修改时间：2001-02-16
*/
#include <iostream>
#include <set>
#include <cstdio>
#include <ctime>
#include <algorithm>
//typedef long long ll;
#define ll long long
#define MAXN 1000009
using namespace std;
struct box_Sort
{
    int score;
    string name;
}my_Box[100];
int a[1000009];

void bubble_Sort(int scale)
{
    for(int i = 0; i < scale; ++i)
        for(int j = 0; j < scale - i; ++j)
            if(a[j] > a[j + 1])
                swap(a[j],a[j + 1]);
}


int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void box_sort(int a[MAXN])
{
    int num;
    int t;
    cin >> num;
    while(num--)
    {
        cin >> t;
        a[t] ++;
    }
    for(int i = 0; i < MAXN; ++i)
        if(a[i])
            cout << i << ' ';
}
void bubble_sort(int a[MAXN])
{
    for(int i = 0; i < MAXN - 1; ++i)
        for(int j = 0; j < MAXN - 1 - i; ++j)
            if(a[j] > a[j + 1]) // descent descend ascent ascend
                swap(a[j], a[j + 1]);
}
void quick_sort(int left, int right)
{
    if(left > right)
        return ;
    int temp = a[left];
    int i = left, j = right;
    while(i != j)
    {
        while(a[j] >= temp && j > i)
            j--;
        while(a[i] <= temp && i < j)
            i++;
        if(i < j)
        {
            swap(a[i], a[j]);
        }
    }
    a[left] = a[i];
    a[i] = temp;
    quick_sort(left, i - 1);
    quick_sort(i + 1, right);
    return ;
}
int main(){
    time_t start, over;
    double run_time;
    int i;
    int scale = 100;
    for(scale; scale <= 1e4; scale *= 10)
    {
        for(i = 0; i <= scale; i++)
            a[i] = i;
        start = clock();
        bubble_Sort(scale);
        over = clock();
        printf("bubble with %d scale lever costs %lf s\n", scale, (double)(over - start)/CLOCKS_PER_SEC);
    }
    for(scale = 100; scale <= 1e6; scale *= 10)
    {
        for(i = 0; i <= scale; i++)
            a[i] = i;
        start = clock();
        //QuickSort(0,scale);
        qsort(a, scale, sizeof(int), compare);
        over = clock();
        printf("qsort with %d scale lever costs %lf s\n", scale, (double)(over - start)/CLOCKS_PER_SEC);
    }
    for(scale = 100; scale <= 1e6; scale *= 10)
    {
        for(i = 0; i <= scale; i++)
            a[i] = i;
        start = clock();
        sort(a,a+scale,greater<int>());
        over = clock();
        printf("sort with %d scale lever costs %lf s\n", scale, (double)(over - start)/CLOCKS_PER_SEC);
    }
    for(scale = 40; scale <= 40000; scale *= 10)
    {
        for(i = 0; i <= scale; i++)
            a[i] = i;
        start = clock();
        quick_sort(0, scale);
        //qsort(a, scale, sizeof(int), compare);
        over = clock();
        printf("my_qsort with %d scale lever costs %lf s\n", scale, (double)(over - start)/CLOCKS_PER_SEC);
    }
    cout << "Mission complete";
    return 0;
}

```

输出如下：

<!--bubble with 100 scale lever costs 0.000000 s
bubble with 1000 scale lever costs 0.002000 s
bubble with 10000 scale lever costs 0.120000 s
qsort with 100 scale lever costs 0.000000 s
qsort with 1000 scale lever costs 0.000000 s
qsort with 10000 scale lever costs 0.000000 s
qsort with 100000 scale lever costs 0.006000 s
qsort with 1000000 scale lever costs 0.068000 s
sort with 100 scale lever costs 0.000000 s
sort with 1000 scale lever costs 0.000000 s
sort with 10000 scale lever costs 0.001000 s
sort with 100000 scale lever costs 0.011000 s
sort with 1000000 scale lever costs 0.132000 s
my_qsort with 40 scale lever costs 0.000000 s
my_qsort with 400 scale lever costs 0.000000 s
my_qsort with 4000 scale lever costs 0.022000 s
my_qsort with 40000 scale lever costs 1.767000 s
Mission complete-->

##### 关于时间测量：

我们使用头文件 <ctime> 来包含我们所需要的函数，完成计数。

```c++
	time_t start, over;
	double run_time;
		start = clock();
        function();
        over = clock();
        printf("my_qsort with %d scale lever costs %lf s\n", scale, (double)(over - start)/CLOCKS_PER_SEC);
```

 `time_t start, over`；time_t 是在<ctime>中的一个结构体。

`start = clock()`  调用这样的语句，在一段我们需要计数的函数体两端，减去之后即可得到一个点数。

但想得到用秒为单位的时间，需要先将其转化为double类型，然后与CLOCKS_PER_SEC作比，就可以得到最后的秒数了。



##### 总结：

根据数据量的增加， 我们不难发现：

qsort  >  sort  >  my_qsort = bubble

考虑原因：qsort 比 sort 更快是由于优化问题，sort并没有采用最佳最高效的排序策略，但其实也够用了。如果非要追求效率，那么使用qsort。

###### Discoveries and  Problems to be solved：

其一：虽然我们的my_qsort在思路以及排序效果上都没有问题，但是其效率很低下：4e4的数据规模居然要1.77s才能排完。

其二：bubble的确很慢，对于1e5的数据量需要11s，但由于其优美，作为教学也是ok的。

其三：后续还有选择，插入，堆排序等等。到时候在做对比。



