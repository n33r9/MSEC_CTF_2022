#include <stdio.h>
#include <stdlib.h>

unsigned short sum(unsigned short arr[], unsigned short do_dai_mang) {
    unsigned short sum = 0;
    for (int i = 0; i < do_dai_mang; i++) {
        if (arr[i] == 0)
            return sum;

        sum += arr[i];
    }

    return sum;
}

unsigned short read_short() {
    char buffer[8];
    fgets(buffer, sizeof(buffer), stdin);
    return (unsigned short)atoi(buffer);
}

void win() {
    system("cat flag.txt");
    return;
}

int main()
{
    unsigned short do_dai_mang;
    puts("Do dai mang ban muon:");
    do_dai_mang = read_short() + 2;
    unsigned short* arr = (unsigned short*)malloc(do_dai_mang);
    puts("Gia tri ngau nhien da duoc sinh ra");
    unsigned short hang_rao_bao_ve = (unsigned short)rand();
    printf("%hu\n",hang_rao_bao_ve);
    arr[do_dai_mang - 2] = hang_rao_bao_ve;
    arr[do_dai_mang - 1] = (unsigned short)rand();
    printf("%hu\n", arr[do_dai_mang -1]);
    for (unsigned short i = 0; i < (unsigned short)(do_dai_mang - 2); i++) {
        printf("Arr[%d] = ", i);
        arr[i] = read_short();
        if (arr[i] == 0) {
            arr[i] = 0;
            break;
        }
    }

    if (hang_rao_bao_ve != arr[do_dai_mang - 2]) {
        // Bạn muốn overflow hả :D
        puts("Ban muon overflow voi toi ha, :D quay lai va nghi tiep di");
        return -1;
    }

    unsigned short tong_gia_tri = sum(arr, do_dai_mang - 2);
    printf("Tong cua ban la: %hu\n", tong_gia_tri);
    if (tong_gia_tri != arr[do_dai_mang - 1]) {
        puts("Thu lai di bro");
    }
    else {
        win();
    }

    return 0;
}