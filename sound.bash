perl -e 'use bytes; 
for($t=0;;$t++)
    { 
        print chr($t*(($t>>11|$t>>23)&85&$t>>3)); 
    }' |play -v 0.03 -t raw -b8 -r8k -e un -
#./out | play -t raw -b8 -r8k -e un -
