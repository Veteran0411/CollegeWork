#include<stdio.h>
int main(){
    #if __STDC__==0
    printf("cc is not ansi c compliant");
    #else
    printf("%s compiled at %s:%s. this statement is at line. %d\n",__FILE__,__DATE__,__TIME__,__LINE__);
    #endif
    return 0;
}