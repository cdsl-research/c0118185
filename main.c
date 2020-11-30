//https://blog.csdn.net/bian_cheng_ru_men/article/details/81476998?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/ip_icmp.h>
#include <netinet/ip.h>
 
 
int main() {
  int sfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
  if(sfd < 0)
  {
    perror("socket");
    return 1;
  }
  
  int opt = 1;
  setsockopt(sfd, IPPROTO_IP, IP_HDRINCL, &opt, sizeof(opt));
 
  char buf[1500];
  while(1)
  {
    memset(buf, 0x00, sizeof(buf));
    int ret = read(sfd, buf, 1500);
    if(ret <= 0)
    {
      break;
    }
 
    struct iphdr* pip = (struct iphdr*)(buf);
    struct in_addr ad;
 
    ad.s_addr = pip->saddr;
    //printf("protocol: %hhd, %s <-----> ", pip->protocol, inet_ntoa(ad));
    printf("数据报为%s <===>",inet_ntoa(ad));
    ad.s_addr = pip->daddr;
    printf("%s\n", inet_ntoa(ad));
 
  }
  return 0;
}

int gettimeofday(struct timeval *tv, struct timezone *tz)；//获取的时间为微秒级的，big存放在tv中。
struct timeval {
               time_t      tv_sec;     /* seconds */
               suseconds_t tv_usec;    /* microseconds */
 
};这是一个线程安全的函数。


struct hostent *gethostbyname(const char *name);     //函数返回给定主机名的hostent类型的结构。
 struct hostent {
               char  *h_name;            /* official name of host */
               char **h_aliases;         /* alias list */
               int    h_addrtype;        /* host address type */
               int    h_length;          /* length of address */
               char **h_addr_list;       /* list of addresses */
}


unsigned short chksum(unsigned short* addr, int len)   //校验和
{
  unsigned int ret = 0;
  
  while(len > 1)
  {
    ret += *addr++;
    len -= 2;
  }
  if(len == 1)
  {
    ret += *(unsigned char*)addr;
  }
 
  ret = (ret >> 16) + (ret & 0xffff);
  ret += (ret >> 16);
  
  return (unsigned short)~ret;
}