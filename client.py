import socket
import argparse


def send_hello(my_socket):
    my_socket.sendall('cs5700fall2022 HELLO chen.jiazhe\n'.encode(encoding='UTF-8'))


def calculation(my_expression):
    my_expression = my_expression[:-2]
    my_expression_list = my_expression.split(' ')
    output = 0
    count = 0
    expression_stack = []
    while count <= len(my_expression_list):
        if my_expression_list[count] == '(':
            count += 1
        elif my_expression_list[count] == ')':
            number_b = int(expression_stack.pop())
            operator = expression_stack.pop()
            if (operator == '+' or operator == '-' or operator == '*' or
                    operator == '//' or operator == '<<^'):
                number_a = int(expression_stack.pop())
                if operator == '//' and number_b == 0:
                    return 'error'
                else:
                    if operator == '+':
                        output = number_a + number_b
                    elif operator == '-':
                        output = number_a - number_b
                    elif operator == '*':
                        output = number_a * number_b
                    elif output == '//':
                        output = number_a // number_b
                    else:
                        output = (number_a << 13) ^ number_b
            else:
                output = int(operator)
            expression_stack.append(str(output))
            count += 1
        else:
            expression_stack.append(my_expression_list[count])
            count += 1
    return int(expression_stack.pop())


def send_error(my_socket):
    my_socket.sendall('cs5700fall2022 ERR #DIV/0\n')


def send_result(my_socket, result):
    my_socket.sendall('cs5700fall2022 STATUS {output}\n'.format(output=result))


def get_expression(message):
    message_list = message.split(str=' ')
    if message_list[1] == 'BYE':
        print(message_list[2])
        return ''
    elif message_list[1] == 'EVAL':
        return message_list[2]


def main():
    parser = argparse.ArgumentParser(description='CS5700 Project 1')
    # initiate a parser
    parser.add_argument('--port', '-p', required=True, type=int, default=27995, help='Port of the Server')
    parser.add_argument('-s', required=True, action='store_true', help='Encrypted Socket Connection')
    parser.add_argument('--hostname', nargs=1, help='Name of the Host')
    parser.add_argument('--username', nargs=1, help="Northeastern Username")
    args = parser.parse_args()
    print(args)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.AF_INET means it is an ipv4 connection, socket.SOCK_STREAM means it is a streaming socket.
    # note that this socket is a TCP socket for now.
    my_socket.connect(("project1.5700.network", args.port))
    # 27995 is the default port for the client.
    send_hello(my_socket)

    message = 'start'
    while message != '':
        message = str(my_socket.recv(64))
        print(message)

        # # socket.recv() receives the message. there is an argument for the size of each data chunk.
        # if len(message) <= 0:
        #     break
        # my_expression = get_expression(message.decode("utf-8"))
        # # message.decode() choose the format to decode the message.
        # if my_expression != '':
        #     result = calculation(my_expression)
        #     if result == 'error':
        #         send_error(my_socket)
        #     else:
        #         send_result(my_socket, result)
        # else:
        #     break


if __name__ == '__main__':
    main()
