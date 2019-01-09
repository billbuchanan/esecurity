pragma solidity ^0.4.0;
contract test2{
   uint a ;
   function test2() {
       a = 1;
   }
   function val() returns(uint){
       return a;
   }  
}
contract test3 is test2{ 
    uint b = a++;
    function show() returns(uint){
        return b; 
    }
}
