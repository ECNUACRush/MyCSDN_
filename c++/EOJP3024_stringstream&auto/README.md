# 					StringStream使用强化

### 核心代码：

```cpp
void solve()/* Define function solve() to process one case of the problem    */
{
    string s, t;
    set<string> ss;
    getline(cin, s);
    for(auto &i : s)
        if(!isalpha(i)) i = ' ';
    stringstream stream(s);
    while(stream >> t)
        ss.insert(t);
    auto x = ss.begin();
    cout << *x;
    while(++x != ss.end())
        cout << ' ' << *x;
    cout << endl;
    return ;
}
```

#### 题干

提取英文文本中的单词，重复出现的单词只取一个，把它们按照字典顺序排序，建立为一个单词表。

例如：英文文本如下：

ask not what your country can do for you,ask what you can do for your country.

提取的非重复单词为：

ask not what your country can do for you

排序后建立的单词表为：

ask can country do for not what you your

#### 注意：

(1) 单词与单词之间用空格或标点符号（逗号 (,)，句号 (.), 惊叹号 (!), 问号 (?)）分隔。

(2) 提取的单词只包含 26 个英文字符。
输入格式

第 1 行：一个整数 T (1≤T≤10) 为问题数。

接下来 T 行，每行输入一段文本，文本长度不超过 500 个字符。

文本由空格，逗号 (,)，句号 (.)， 惊叹号 (!)，问号 (?) 以及 26 个小写英文字符组成。
输出格式

对于每个问题，输出一行问题的编号（0 开始编号，格式：case #0: 等）。

然后对应每个问题 , 在一行中输出建立的单词表，单词与单词之间用一个空格分隔。最后一个单词后面没有空格。

#### 样例

```cpp
##### Input

3
ask not what your country can do for you,ask what you can do for your country.
no enthusiasm forever,no unexpected happening of surprising and pleasing so,only silently ask myself in mind next happiness,when will come?
let us go! let us go!a things.

###### Output

case #0:
ask can country do for not what you your
case #1:
and ask come enthusiasm forever happening happiness in mind myself next no of only pleasing silently so surprising unexpected when will
case #2:
a go let things us
```

