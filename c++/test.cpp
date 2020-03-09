string line,t;
vector<string>s;
getline(cin, line);
stringstream linestream;
linestream << line; //linestream.str(line); 这种写法也是可行的 相当于把line传入到了stream中
while(linestream >> t) s.push_back(t);
