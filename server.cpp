#include <iostream>
#include "SDL.h"

int main()
{
    std::cout << "hello test server" << std::endl;
    Uint16 port = (Uint16)strtol( 7000, NULL, 0);
    Server s(port);
    TCPsocket sock;
    std::cout << sock << std::endl;
    return 0;
}