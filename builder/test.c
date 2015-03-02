/* Test program to check that autogenerated code compiles and links */

/* Dummy functions to take place of MIN */

#include "gen.h"

void min_tx_frame(uint8_t id, uint8_t payload[], uint8_t control)
{
}

void min_rx_byte(uint8_t byte)
{
}

uint8_t uart_receive_ready(void)
{
}

void uart_receive(uint8_t *p, uint8_t n)
{
}

/* Callback */
void min_unpack_frame_f8(uint8_t buf[], uint8_t contro)
{
}

void main(void)
{
    get_s1();
    get_s2();
    get_s3();

    min_input();
    min_output();


}