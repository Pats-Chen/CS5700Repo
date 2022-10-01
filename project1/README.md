## Student Information

Name: Jiazhe Chen, NUID: 002162461  

## High-level Approach

I used Python for the client file. The basic idea is to use the "socket" and "ssl" library to establish a TLS socket connection to the server first, then use the "argparse" library to build a commandline interface.  

The file "client" is a Python script file that can be executed under the WSL Ubuntu environment. In this file, I created several functions to make make every part of the whole logic separated into independent pieces, so that I can find bugs more easily if there is any.  

The "evaluate" function handles the evaluation logic of every single operation of the message received. It takes 3 strings and will return 1 string as the result.  

The "calculation" function handles the logic to transfer the message received into stacks, so that it can be calculated from the very inside and then the outside of every pair of brackets. It will return a string as the final answer of the message. If there is a divide by zero error, then it will return the word "ZeroDivisionError" as the result.  

"send_hello", "send_error" and "send_result" are used to send corresponding messages to the server. All messages need to be send in the form of bytes, instead of strings.  

The "main" function is the main part of the script file. It handles all other parts that do not belong to any other functions. In this function, a commandline interface is built first. Then a TLS connection socket wrapped in the default SSL context is used to create a connection with the server. After that, a hello message will be sent to the server. If the server got the hello message successfully, then it will start to send "EVAL" messages. The socket instance will receive the data chunk from the server, and then concatenate data chunks together to form the whole message received. It will then check to see if this is an ending message with "BYE" in it. If so, it will close the connection. If there is no "BYE" in it, then it will start to parse the message, calculate it, and then use the result obtained for corresponding sending functions.  

## Challenges Faced

There are several challenges that I have faced when trying to finish this project. First of all, I have no previous computer network programming experience, so I don't know where to start. I don't know which library to use, and I don't know anything about the big picture of the project. The description given on the course website is not enough for me because of this.  

After I managed to figure out the big picture, there is another challenge that I faced. Since the server side is not written by me, it is hard to figure out what is the server doing at some particular time. This is important because I need to know if the error message is coming from the bugs in my code, or it shows because I didn't understand the specs of the messages. This is also closely related to the last challenge that I faced when debugging.  

Lastly, when I tried to debug, I realized that I have no previous experience on how to write test cases for a computer network program, and the server will not send the same message twice or more times to let me figure out what is going on in my script file. So in the end, I chose to execute my script file multiple times every time I changed anything to see if it works properly. This was very time-consuming, but I don't know how to do this properly for now. I have also written some simple test cases that can be solved easily to verify the logic of the arithmetic calculation part. It is hard to verify messages that come from the server because I can't calculate them in an easy way to ensure that there is no calculation mistake in my test case.

## Methods to Test the Code

As I mentioned in the previous part, I executed my script file multiple times every time I changed anything to see if it works properly. Whenever there is an error, I try to print out all intermediate variables that I used to see what is going on in the process. As for the calculation and evaluation part, I know how to debug this one. So I executed my script file multiple times to get some test case messages from the server, and then I wrote a test script file to test and debug the calculation and evaluation part. Since I am not given the correct answer that I should be sending, I wrote some simple test case for the debugging process and I also used some of the messages that I obtained from the server in my previous attempts as test cases. It is worth mentioning that setting multiple checkpoints in the debug mode is very useful when I was trying to debug the whole script file. Developers should be careful when calling the function that can pop up items from stacks in an unexpected order.