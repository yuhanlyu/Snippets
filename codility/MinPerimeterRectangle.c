#include <stdio.h>
#include <math.h>

int solution(int N);
int solution(int N)
{
    for (int i = sqrt(N); i > 0; --i)
        if (N % i == 0)
            return 2 * (i + (N / i));
}

int main(void)
{
    printf("%d\n", solution(30));
}
