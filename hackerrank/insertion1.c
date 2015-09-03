void insertionSort(int ar_size, int ar[]) {
    int temp = ar[ar_size - 1], i;
    for (i = ar_size - 1; i > 0 && ar[i - 1] > temp; --i) {
        ar[i] = ar[i - 1];
        for (int j = 0; j < ar_size; ++j)
            printf("%d ", ar[j]);
        puts("");
    }
    ar[i] = temp;
    for (int j = 0; j < ar_size; ++j)
        printf("%d ", ar[j]);
    puts("");    
}
