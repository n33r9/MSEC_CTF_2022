#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/mman.h>
#define MAX 200
#define DEFAULT_SIZE 0x1200
#define PORT 1337
#define SA struct sockaddr

char name[MAX];
char* buff;

void getdata(int connfd)
{
    char tmp[9];
    int x;
    memset(name, 0, MAX);
    char wel2[29] = "Give me the size of report:\n\x00";
    char wel[25] = "Give me your report:\n\x00";
    char wel3[20] = "Give me your name:\n\x00";
    char err[15] = "Invailid size\n\x00";
    write(connfd,wel3,sizeof(wel3)); 
    read(connfd,name,200-1);
    write(connfd,wel2,sizeof(wel2)); 
    x = read(connfd,tmp,9);
    if(x>0){
        tmp[x-1] = NULL;
    }
    else{
        write(connfd,err,sizeof(err));
        exit(1);
    }
    x = atoi(tmp);
    printf("%d",x);
    if(x<=0 || x > 0x8000){
        write(connfd,err,sizeof(err));
        exit(1);
    }
    write(connfd,wel,sizeof(wel));
    read(connfd,buff,x);    
}

void pwn(char *cmd){
    system(cmd);
}
   
int main()
{
    int sockfd, connfd, len, pid;
    struct sockaddr_in servaddr, cli;
    char msg[40] = "\nThank you for report!!\n\x00";
    buff = mmap(NULL, DEFAULT_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1,0);
   
    // socket create and verification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully created..\n");
    bzero(&servaddr, sizeof(servaddr));
   
    // assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
   
    // Binding newly created socket to given IP and verification
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
        printf("socket bind failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully binded..\n");
   
    // Now server is ready to listen and verification
    if ((listen(sockfd, 5)) != 0) {
        printf("Listen failed...\n");
        exit(0);
    }
    else
        printf("Server listening..\n");
    len = sizeof(cli);
    
    
    while(1){
        connfd = accept(sockfd, (SA*)&cli, &len);
        if (connfd < 0) {
            printf("server accept failed...\n");
            continue;
        }
        else
            printf("server accept the client %d...\n",connfd);
        if ((pid = fork()) == -1){
            printf("Error fork\n"); close(connfd); } else if(pid == 0){
            close(sockfd);
            getdata(connfd);
            write(connfd, msg, sizeof(msg));
            exit(0);
        }
        close(connfd);
    }
    close(sockfd);
}
