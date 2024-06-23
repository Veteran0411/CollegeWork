TW 1 unix
res=pathconf(“/”,_PC_NAME_MAX))==-1

#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199309L 
#include<iostream.h> 
#include<unistd.h> 
#include<limits.h> 
int main() 
{ 
Int ch;
int res;
cout<<“Enter the choice”;
cin>>ch;
swith(ch)
{ 
case 1: 
cout<<“Run time configuration Limits”;
if((res=sysconf(_SC_CLK_TCK))==-1) 
cout<<"System doesnot support\n"; 
else 
cout<<"Number of Clock Tick:"<<res<<endl;
if((res=sysconf(_SC_CHILD_MAX))==-1) 
cout<<"System doesnot support\n"; 
else
 cout<<"Maximum Number of Child Process that process can 
create:"<<res<<endl; 
if((res=pathconf(“/”,_PC_PATH_MAX))==-1) 
cout<<"System doesnot support\n";
 else 
cout<<"Maximum Path Length:"<<res<<endl;
if((res=pathconf(“/”,_PC_NAME_MAX))==-1) 
cout<<"System doesnot support\n"; 
else 
cout<<"Maximum No.of Character in a filename:"<<res<<endl; 
if((res=sysconf(_SC_OPEN_MAX))==-1)
 cout<<"System doesnot support\n"; 
else 
cout<<"Maximum Number of opened files per process:"<<res<<endl; 
break;
Case 2:
Cout <<“compile time configuration limits”;
Cout<<“MAX no. of child processes created by process”<<_POSIX_CHILD_MAX;
Cout<<“MAX no. of files opened by a process”<<_POSIX_OPEN_MAX;
Cout<<“MAX no. of characters allowed in a path name”<<POSIX_PATH_MAX;
Cout<<“MAX no. of characters allowed in a file name”<<POSIX_NAME_MAX;
return 0; 
}
}