#include <stdio.h>

int solution(char *S);
int solution(char *S)
{
    int count = 0;
    for (int i = 0; S[i] != '\0'; ++i) {
        count += (S[i] == '(' ? 1 : -1);
        if (count < 0)
            return 0;
    }
    return count == 0;
}

int main(void)
{
    char s1[] = "(()(())())";
    char s2[] = "())";
    printf("%d\n", solution(s1));
    printf("%d\n", solution(s2));
}
