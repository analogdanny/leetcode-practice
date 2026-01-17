
#include <stack.h>
#include <string.h>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        map<char,char> brackets;
        brackets['{']='}';
        brackets['[']=']';
        brackets['(']=')';

        stack<char> st;
        char top;

        if(s.length() % 2 != 0)
            return false;

        for(int i = 0; i < s.length(); i++)
        {
            if(!st.empty()) top = st.top();
            
            if( (s[i] == '{') || (s[i] == '[') || (s[i] == '(') )
                st.push(brackets[s[i]]);
                /*
                    i = 0    st = }  <-top
                    i = 1    st = },]  <-top
                    i = 3    st = },)  <-top
                */
            else if (top == s[i])
                st.pop();
                /*
                    i = 2    st = }
                    i = 4    st = )
                */
            else return false;
        }

        if(st.empty()) return true;
        else return false;

    }
};
