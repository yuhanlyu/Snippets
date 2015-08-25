#include <stdio.h>

int solution(int N);
int solution(int N)
{
    int answer = 0;
    for (; N > 0 && (N & 1) == 0; N >>= 1) ;
    for (int gap = 0; N > 0; N >>= 1) {
        if ((N & 1) == 0)
            ++gap;
        else { 
            if (gap > answer)
                answer = gap;
            gap = 0;
        }
    }
    return answer;
}

int main(void)
{
    printf("%d\n", solution(9));
    printf("%d\n", solution(20));
    printf("%d\n", solution(15));
}
