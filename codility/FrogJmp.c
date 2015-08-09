#include <stdio.h>

int solution(int X, int Y, int D)
{
    return X == Y ? 0 : ((Y - X) - 1) / D + 1;
}

int main(void)
{
    printf("%d\n", solution(10, 85, 30));
    printf("%d\n", solution(10, 40, 30));
    printf("%d\n", solution(10, 10, 30));
    return 0;
}
