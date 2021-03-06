#include <16f877a.h>

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#fuses XT, NOWDT, NOPROTECT
#use delay (clock=4Mhz)
#use rs232 (baud=9600, parity=N, xmit=pin_c6, rcv=pin_c7, bits=8)

void set_adc(void);
uint8_t read_adc_in(uint8_t channel);

void main(void)
{
    while (true)
    {
      set_adc();
      uint8_t adc1 = read_adc_in(0), adc2 = read_adc_in(1);
      printf("%u,%u\r\n", adc1, adc2);
      delay_us(10*10000);
    }
}


void set_adc(void)
{
    setup_adc_ports(all_analog);
    setup_adc(adc_clock_internal);
}

uint8_t read_adc_in(uint8_t channel)
{
    set_adc_channel(channel);
    delay_us(50);
    return read_adc();
    //val = (valint*5.0)/1023;
}

