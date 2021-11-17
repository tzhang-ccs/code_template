#include <sys/time.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    struct timeval tv1,tv2;
    int rc;
    float runtime;

    gettimeofday(&tv1, NULL);
    sleep(20);
    gettimeofday(&tv2, NULL);
    
    runtime=(tv2.tv_usec - tv1.tv_usec)/1000000 + (tv2.tv_sec - tv1.tv_sec);

    printf("runtime = %.2fs\n", runtime);
    return 0;
}
