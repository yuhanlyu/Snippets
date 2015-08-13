#include <stdio.h>
#include <string.h>

int solution(char *S);
int solution(char *S)
{
    int n = strlen(S), top = -1;
    char stack[n];
    for (int i = 0; i < n; ++i) {
        if (S[i] == '(' || S[i] == '{' || S[i] == '[')
            stack[++top] = S[i];
        else if (top == -1)
            return 0;
        else if (S[i] == ')') {
            if (stack[top--] != '(')
                return 0;
        } else if (S[i] == '}') {
            if (stack[top--] != '{')
                return 0;
        } else if (S[i] == ']')
            if (stack[top--] != '[')
                return 0;
    }
    return top == -1;
}

int main(void)
{
    char S1[] = "{[()()]}";
    char S2[] = "([)()]";
    printf("%d\n", solution(S1));
    printf("%d\n", solution(S2));
}
