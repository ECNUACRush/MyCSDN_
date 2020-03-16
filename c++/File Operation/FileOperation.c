#include <bits/stdc++.h>

using namespace std;
void readTxt(string file)
{
    ifstream ifs;
    ifs.open(file);   			//将文件流对象与文件关联起来，如果已经关联则调用失败
    assert(ifs.is_open());   	//若失败,则输出错误消息,并终止程序运行

    string s;
    while(getline(ifs,s))		//行分隔符可以显示指定，比如按照分号分隔getline(infile,s,';')
    {
        cout<<s<<endl;
    }
    ifs.close();             	//关闭文件输入流
}

int main()
{
    string file = "Input.txt";
    readTxt(file);
    return 0;
}
