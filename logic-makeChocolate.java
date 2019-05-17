/*
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always 
use big bars before small bars. Return -1 if it can't be done.

makeChocolate(4, 1, 9) → 4
makeChocolate(4, 1, 10) → -1
makeChocolate(4, 1, 7) → 2
*/


public int makeChocolate(int small, int big, int goal) {

  if (big*5==goal) return 0;
  if (big*5>goal){
    int x = goal-((7/5)*5);
    if (x<=small && x>=0){
      return (x);
    } else{
      if (small >= goal) return goal;
    }
  }
  if (big*5 < goal)
    {if ((goal-big*5) <= small) return goal-big*5;}
  return -1;

}