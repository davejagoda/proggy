/* cc whoami.m -framework Foundation -o whoami */

#import <Foundation/Foundation.h>

int main(void)
{
  NSLog(@"NSUserName == %@",NSUserName());
  NSLog(@"NSFullUserName == %@",NSFullUserName());
  return 0;
}
