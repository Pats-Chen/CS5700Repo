## Student Information

Name: Jiazhe Chen, NUID: 002162461  

## High-level Approach

I used Python for the web crawler file. The basic idea is to use the "socket" and "ssl" library to establish an HTTPS socket connection to the website server first, then use the cookies and csrf middleware token obtained to log in and traverse the whole website. Two HTML parsers from the "html" library are also used to parse the information obtained from the website during the traversing process. The "argparse" library is used to build a command-line interface.  

The file "webcrawler" is a Python script file that can be executed under the WSL Ubuntu environment. In this file, I created several functions to make every part of the whole logic separated into independent pieces so that I can find bugs more easily if there are any.  

The "get_cookie" function is used to obtain cookies and the csrf middleware token on the target website. It takes 1 socket instance and 2 strings as input, and will return 1 string message as the output.  

The "post_request" function handles the logic to log in to the target website so that all pages available to the user can be traversed later. It takes 1 socket instance and 7 strings as input, and will return 1 string message as the output.  

The "redirect_request" function handles the logic to redirect to a new page on the target website after the log in process. It is used when performing the traversing process through the whole website. It takes 1 socket instance and 4 strings as input, and will return 1 string message as the output.  

The "message_parser" function handles the logic to parse the string message obtained from any one of the 3 functions mentioned above. It is used to find out the key information within the string message, such as the HTTP status, the cookies, or the new link to redirect to. It takes 1 string as the input and will return 1 Python dictionary instance as the output.  

The "main" function is the main part of the script file. It handles all other parts that do not belong to any other functions. In this function, a command-line interface and an HTTPS connection socket instance wrapped in the default SSL context are used to create a connection with the server of the target website first. Then a "GET" HTTP request will be sent to obtain all key information needed in the log-in process. After that, a "POST" HTTP request will be sent to let the user log in to the website. More "GET" requests will also be sent during the traversing process after the log-in request has been received by the server of the website successfully. A token finder and a flag finder, which is the subclass of the "HTMLparser" class, are also instantiated to obtain the corresponding token and secret flags. During the traversing process, 5 HTTP status codes are handled accordingly to let the web crawler traverse the whole website without errors. Once all 5 secret flags are collected, the process will stop and print out all of them as the output.  

## Challenges Faced

There are several challenges that I have faced when trying to finish this project. First of all, even though we have discussed the HTTP protocol in previous lectures, I still spend quite some time to be familiar with the format of HTTP requests. The website that we should use seems to only accept requests that are following a certain format, so I have to repeatedly work on some try-and-error process to find out the correct format that is allowed by the server of the website.  

After I managed to figure out the correct format, there is another challenge that I faced. The description of the project mentioned that our script file should be able to handle cookie management when connecting to the server. Even though I understand that this means that I should use cookies that I found from the initial request, I did not notice that I also need to check the content of the messages sent back from the server, because there is hidden information that I should use during the log-in process. As a result, I was not able to set the hidden information correctly, and the server did not allow me to log in for quite a long time. I took some time discussing this issue with the teaching assistants and my classmates on Piazza, and I eventually managed to find out what was wrong with my log-in process.  

The last challenge that I faced in this project is that after I logged in successfully to the website, I realized that I don't know how to handle an HTTP redirect response properly, so I spent some time searching for useful resources online as well as using the developer tool provided by Chrome browser to understand what should I do next. It turned out that this is relatively easy to solve, and after that, all I need to do is to run the script file several times to test for minor bugs within the file and fix them.  

## Methods to Test the Code

This project is hard to test, mainly because we are not supposed to use any other websites to test our code. Plus, there is no calculation logic part that can be tested in some separated environment, as we have encountered in project 1. Therefore, I have to execute my script file multiple times every time I changed anything to see if there is anything wrong within. Whenever there is an error, print out all intermediate variables that I used to see what was going on in the process. It is worth mentioning that setting multiple checkpoints in the debug mode is very useful when I was trying to debug the whole script file. I have also tried to use try-and-catch phrases to catch potential errors that will not let the script file stop instantly, but will still let the web crawler behave in unexpected ways. I gradually started to learn what is a good practice for a network programming developer to conduct during his working process.  