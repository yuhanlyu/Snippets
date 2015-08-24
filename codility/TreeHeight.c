#include <stdio.h>
struct tree {
    int x;
    struct tree * l;
    struct tree * r;
};

int solution(struct tree *T);
int solution(struct tree *T)
{
    int result = 0;
    if (T->l) {
        int t = solution(T->l);
        if (t + 1 > result)
            result = t + 1;
    }
    if (T->r) {
        int t = solution(T->r);
        if (t + 1 > result)
            result = t + 1;
    }
    return result;
}

int main(void)
{
}
