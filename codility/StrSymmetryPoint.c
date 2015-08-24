#include <stdio.h>
#include <string.h>

int solution(char *S);
int solution(char *S)
{
    int length = strlen(S);
    if (length % 2 == 0)
        return -1;
    for (int left = 0, right = length - 1; left < right; ++left, --right)
        if (S[left] != S[right])
            return -1;
    return length / 2;
}

int main(void)
{
    printf("%d\n", solution("racecar"));
    printf("%d\n", solution("x"));
}
